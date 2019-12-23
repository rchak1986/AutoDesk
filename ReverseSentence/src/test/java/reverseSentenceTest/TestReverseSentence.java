package reverseSentenceTest;

import org.testng.Assert;
import org.testng.annotations.Test;

import com.autodesk.hometest.ReverseSentence.ReverseSentence;

public class TestReverseSentence {
	@Test
    public void TC01ValidateReversingValidSentence() {
		ReverseSentence rs = new ReverseSentence();
		Assert.assertTrue(rs.validateReversing("String; 2be reversed...", "gnirtS; eb2 desrever..."),"String is not reversed as Expected.");
    }
	
	@Test
	public void TC02ValidateEmptySentences(){
		ReverseSentence rs = new ReverseSentence();
		//empty string
		Assert.assertTrue(rs.validateReversing("", null),"Empty String Validation Failed");
		//null check
		Assert.assertTrue(rs.validateReversing(null, null),"Empty String Validation Failed");
		//sentence with only spaces
		Assert.assertTrue(rs.validateReversing(" ", null),"Empty String Validation Failed");
	}
	
	@Test
	public void TC03ValidateOnlySpecialCharacters(){
		ReverseSentence rs = new ReverseSentence();
		//only special characters
		Assert.assertTrue(rs.validateReversing(".#@!$%^&*();:',./`~", ".#@!$%^&*();:',./`~"),"String revarsal failed with only special charcters");
	}
	
	@Test
	public void TC04ValidateDigits(){
		ReverseSentence rs = new ReverseSentence();
		//only digits
		Assert.assertTrue(rs.validateReversing("1234567890", "0987654321"),"String revarsal failed with only digits");
		//digits with special characters
		Assert.assertTrue(rs.validateReversing("...1234567890***", "...0987654321***"),"String revarsal failed with digits & special characters");
	}
	
	@Test
	public void TC05ValidateCombination(){
		ReverseSentence rs = new ReverseSentence();
		
		Assert.assertTrue(rs.validateReversing("This is a valid string, no error found!", "sihT si a dilav gnirts, on rorre dnuof!"),"String revarsal failed combination 1");
		Assert.assertTrue(rs.validateReversing("This is a valid string, no error found! 123#", "sihT si a dilav gnirts, on rorre dnuof! 321#"),"String revarsal failed combination 2");
		Assert.assertTrue(rs.validateReversing("...456This is a valid string, no error found! 123#", "...sihT654 si a dilav gnirts, on rorre dnuof! 321#"),"String revarsal failed combination 3");
	}
	
	@Test
	public void TC06ValidatePalindromes(){
		ReverseSentence rs = new ReverseSentence();
		
		Assert.assertTrue(rs.validateReversing("Was it a car or a cat I saw?", "saW ti a rac ro a tac I was?"),"String revarsal failed; palindrome test 1");
		Assert.assertTrue(rs.validateReversing("tattarrattat", "tattarrattat"),"String revarsal failed; palindrome test 2");
		Assert.assertTrue(rs.validateReversing("123tattarrattat", "tattarrattat321"),"String revarsal failed; palindrome test 3");
		Assert.assertTrue(rs.validateReversing("123tattarrattat...", "tattarrattat321..."),"String revarsal failed; palindrome test 4");
	}
}
