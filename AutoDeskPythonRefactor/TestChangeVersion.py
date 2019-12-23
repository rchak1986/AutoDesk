import ChangeVersion
import unittest


class TestChangeVersion(unittest.TestCase):
    def test_no_file_present(self):
        self.assertEqual(ChangeVersion.update_s_construct("invalid_file"), 1)
        self.assertEqual(ChangeVersion.update_version("invalid_file"), 1)

    def test_no_environment_variable_present(self):
        self.assertEqual(ChangeVersion.test_no_environment_variable("SConstruct"), 1)

    def test_combination(self):
        self.assertEqual(ChangeVersion.update_s_construct("SConstruct"), 0)
        self.assertEqual(ChangeVersion.update_version("VERSION"), 0)

        self.assertEqual(ChangeVersion.update_s_construct("SConstruct1"), 0)
        self.assertEqual(ChangeVersion.update_version("VERSION1"), 0)

        self.assertEqual(ChangeVersion.update_s_construct("SConstruct2"), 0)
        self.assertEqual(ChangeVersion.update_version("VERSION2"), 0)

        self.assertEqual(ChangeVersion.update_s_construct("SConstruct3"), 0)
        self.assertEqual(ChangeVersion.update_version("VERSION3"), 0)


if __name__ == '__main__':
    unittest.main()