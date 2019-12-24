import os
import re
import configparser

# defining working directory path
branch = "develop"
region = "global"
source_folder = "src"

# environment variable name to store project root folder path
source_path_env_var = "SourcePath"

# defining environment variable names for SConstruct File's build parameters
sconstruct_env_var_param_point = "point"
sconstruct_env_var_param_patch = "patch"
sconstruct_env_var_param_major = "major"
sconstruct_env_var_param_minor = "minor"

# defining environment variable names for VERSION File's build parameters
version_env_var_param_point = "ADLMSDK_VERSION_POINT"


# #SCONSTRUCT file interesting line
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
# )
def update_s_construct(file_name):
    ''' Function to update build number in SConstruct File '''
    ret_val = 0
    if update_build_number_in_file(file_name, sconstruct_env_var_param_point,
                                   sconstruct_env_var_param_point) != 0: ret_val = 1
    if update_build_number_in_file(file_name, sconstruct_env_var_param_major,
                                   sconstruct_env_var_param_major) != 0: ret_val = 1
    if update_build_number_in_file(file_name, sconstruct_env_var_param_minor,
                                   sconstruct_env_var_param_minor) != 0: ret_val = 1
    if update_build_number_in_file(file_name, sconstruct_env_var_param_patch,
                                   sconstruct_env_var_param_patch) != 0: ret_val = 1
    return ret_val


# # VERSION file interesting line
# ADLMSDK_VERSION_POINT=6
def update_version(file_name):
    ''' Function to update build number in VERSION file'''
    return update_build_number_in_file(file_name, version_env_var_param_point,
                                       version_env_var_param_point)


def update_build_number_in_file(file, build_parameter, build_number_key):
    """
    Function to update the build number in any given file w.r.t a specified build parameter.
    User can either provide the build information through specific environment variable for each
    Build parameter or can provide the same in config.properties file.
    :param file: The file path for in which Build number has to be updated
    :param build_parameter: The build parameter name as string for the specified file
    :param build_number_key: The environment variable or config file key which stores the build number
    :return: Returns 0 if build information is updated; 1 for all other conditions
    """
    version_number = 0
    source_path = ""
    flag = 0

    # defines if build number to be read from config file
    if get_config_data("General", "read_version_from_config") == 'N':

        # validates if the corresponding environment variables are defined and not empty
        if build_number_key in os.environ and os.getenv(build_number_key) is not None:

            # validates if the source path is defined in env. variable, else considers current working directory
            if source_path_env_var in os.environ and os.getenv(source_path_env_var) is not None:
                source_path = os.getenv(source_path_env_var)
            else:
                source_path = os.getcwd()

            # reads build number from env. variable
            version_number = os.getenv(build_number_key.upper())
            flag = 1
        else:
            print("no environment variable defined: " + build_number_key + " or " + source_path_env_var)
    else:
        # reads build numbers from config file & source path as current working directory
        version_number = get_config_data("AllVersion", build_number_key.lower())
        source_path = os.getcwd()
        flag = 1

    # creates a temp file to override the build number
    source_file = os.path.join(source_path, branch, region, source_folder, file)
    dest_file = os.path.join(source_path, branch, region, source_folder, file + "_temp")

    if flag == 1:
        # checks if the file is existing
        if os.path.exists(source_file) and os.path.isfile(source_file):

            # modifies the file permission to enable user read, write and execute
            os.chmod(source_file, 0o755)
            fin = open(source_file, 'r')
            fout = open(dest_file, 'w')

            # navigates through the content of the file and searches for the specified build parameter
            # if found, replaces the build number with the provided one
            # writes into the temp file
            for line in fin:
                pattern = re.sub(build_parameter + "\s*\=\s*[\d]+",
                                 build_parameter
                                 + "=" + version_number, line, flags=re.IGNORECASE)
                fout.write(pattern)
            fin.close()
            fout.close()

            # removes the original file and renames the temp file to the original file name.
            os.remove(source_file)
            os.rename(dest_file, source_file)

            # console log statement
            print("updated version '" + build_parameter +"' in file '" + source_file +"' to value :" +
                  os.getenv(build_number_key.upper()))

            return 0
        else:
            print("file not found: " + source_file)
            return 1
    else:
        return 1


def main():
    update_s_construct("SConstruct2")
    update_version("VERSION2")


def test_no_environment_variable(file_name):
    ''' Function to test when there is no environment variable defined for build number '''

    if get_config_data("General", "read_version_from_config") == 'N':
        return update_build_number_in_file(file_name, "ADLMSDK_VERSION_POINT", "InvalidVariable")
    else:
        return 1


def get_config_data(section_name, key):
    """
    Function to read config file w.r.t a given section and key
    :param section_name: The section name from where key to be searched
    :param key: the key to be read
    :return: the corresponding value of the key
    """
    config = configparser.RawConfigParser()
    print(os.getcwd())
    config.read(os.path.join(os.getcwd(), "config.properties"))

    details_dict = dict(config.items(section_name))
    if check_key_in_dict(details_dict, key) == 0: return details_dict[key]
    else: return 1


def check_key_in_dict(dict, key):
    if key in dict:
        return 0
    else:
        return 1


main()
