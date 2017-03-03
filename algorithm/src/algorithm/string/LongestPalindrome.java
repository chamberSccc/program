package algorithm.string;

import java.util.ArrayList;
import java.util.List;

/*
 * Given a string s, find the longest palindromic substring in s. 
 * You may assume that the maximum length of s is 1000.
 * 
 * Example:
 * Input: "babad" 
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * 
 * Author: ChenBo
 * Date:2017.3.3
 */
public class LongestPalindrome {

	public List<String> list = new ArrayList<String>();
	char[] c = null;
	int startIdnex = 0, endIndex = 0;
	// 计算内部循环往里递归几次
	int count = 0;

	public String longestPalindrome(String s) {
		c = s.toCharArray();
		endIndex = c.length - 1;
		this.getSubPalindrome(startIdnex, endIndex, s);
		System.out.println(list.get(0));
		return null;

	}
	
	/*
	 * 前后两个游标搜索数组,第一遍为start游标不动,end游标不匹配则向前进位。匹配则start与end各进一位继续递归
	 */
	public void getSubPalindrome(int start, int end, String s) {

		if(start==end){
			start=start+1;
			this.getSubPalindrome(start, endIndex, s);
		}else{
			if (c[start] != c[end]) {
				// 外部循环，end每次递归向前进一位
				if (count == 0) {
					end = end - 1;
					this.getSubPalindrome(start, end, s);
				} else {
					// 进行过内部循环，end索引复位，count计数器归0，重新向前递归
					end = end + count - 1;
					start = start-count;
					count =0;
					this.getSubPalindrome(start, end, s);
				}

			} else {
				if (end - start == 1 || end - start == 2) {
					String palinString = s.substring(start-count, end+count+1);
					list.add(palinString);
					return;
				} else {
					count = count + 1;
					end = end - 1;
					start = start + 1;
					this.getSubPalindrome(start, end, s);
				}
			}
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "ahgdsfasdsafjki";
		LongestPalindrome lpd = new LongestPalindrome();
		lpd.longestPalindrome(s);
	}

}
