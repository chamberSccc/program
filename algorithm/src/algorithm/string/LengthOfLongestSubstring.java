package algorithm.string;

/*
 * Given a string, find the length of the longest substring without repeating characters.
 * 
 * Examples:
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * Given "bbbbb", the answer is "b", with the length of 1.
 * Given "pwwkew", the answer is "wke", with the length of 3. 
 * Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 * 
 * Author:ChenBo
 * Time:2017.2.29
 */
public class LengthOfLongestSubstring {
	
	public static  int lengthOfLongestSubstring(String str){
		int length = 0,  endIndex= 0;
		StringBuilder strBuf = new StringBuilder();
		StringBuilder temp = new StringBuilder();
		char[] strChar = str.toCharArray();
		for(int i=0;i<strChar.length;i++){
			temp.append(strChar[i]);
			if(endIndex == strChar.length -1){
				break;
			}
			//abcabcbb
			for(int j=i+1;j<strChar.length;j++){
				if(temp.indexOf(String.valueOf(strChar[j]))!=-1){
					break;
				}else{
					temp.append(strChar[j]);
				}
				
			}
			if(temp.length() > strBuf.length()){
				strBuf.delete(0, strBuf.length());
				strBuf.append(temp);
			}
			temp.delete(0, temp.length());

		}
		System.out.println(strBuf.length()+strBuf.toString());
		return length;
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			String str = "pwwkew";
			lengthOfLongestSubstring(str);

	}

}
