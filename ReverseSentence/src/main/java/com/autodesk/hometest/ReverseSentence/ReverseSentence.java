package com.autodesk.hometest.ReverseSentence;

public class ReverseSentence {
	/**
	 * Method to reverse (ignoring special character position) a sentence. 
	 * <br><i>Assuming words are segregated by spaces.</i> 
	 * @param sentence <br> Sentence as string.
	 * @return Sentence with reversed words.
	 */
	public String reverseEachWordInSentence(String sentence){
		if (sentence!=null && !sentence.isEmpty() && !sentence.trim().isEmpty()){
			if (sentence.contains(" ")){
				String [] words = sentence.split(" ");
				String ret=new String();
				for (String str:words){
					ret = ret + " " + reverseStringIgnoringSpecialChar(str);
				}
				return ret.trim();
			}else{
				return reverseStringIgnoringSpecialChar(sentence);
			}			
		}else{
			System.out.println("Not a sentance; empty string.");
			return null;
		}		
	}
	
	/**
	 * Method to reverse any word ignoring special characters
	 * <br><br>Algorithm
	 * <br>------------<br>
	 * <i>1. convert input string into character array<br>
	 * 2. Traverse through the input array and copy into a temporary array
	 * if character is a digit or alphabet<br>
	 * 3. Reverse the temporary array<br>
	 * 4. Copy elements from temporary array into the input array if it is a character or a digit.</i><br>
	 * @param input <br> The word as a string (case insensitive)
	 * @return Reversed string ignoring special characters
	 */
	private String reverseStringIgnoringSpecialChar(String input) {  
		//convert input to char array and declare temporary array to 
		//extract alphabets and digits
		char[] inputArr = input.toCharArray();  
		char[] tempArr = new char[input.length()];  
		int i=0;  
		int j=0;  
		
		//copy into temporary array if char is alphabetic or digits
		for (char ch:inputArr){  
		  if(Character.isAlphabetic(ch) || Character.isDigit(ch)){  
		    tempArr[i] = ch;  
		    i++;  
		  }  
		}  
		i--;  
		
		//reverse characters in temporary array (alphabets & digits)
		while(j<i){  
		  char temp = tempArr[i];  
		  tempArr[i]= tempArr[j];  
		  tempArr[j]=temp;  
		  j++;  
		  i--;  
		}
		
		//copy temporary array into input character array if char is alphabet or digit
		for(i=0,j=0;i<input.length();i++){  
		  if(Character.isAlphabetic(inputArr[i]) || Character.isDigit(inputArr[i])){  
		    inputArr[i]= tempArr[j++];  
		  }  
		}  
		
		return new String(inputArr);  
	}  

}
