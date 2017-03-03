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
	// �����ڲ�ѭ������ݹ鼸��
	int count = 0;

	public String longestPalindrome(String s) {
		c = s.toCharArray();
		endIndex = c.length - 1;
		this.getSubPalindrome(startIdnex, endIndex, s);
		System.out.println(list.get(0));
		return null;

	}
	
	/*
	 * ǰ�������α���������,��һ��Ϊstart�α겻��,end�α겻ƥ������ǰ��λ��ƥ����start��end����һλ�����ݹ�
	 */
	public void getSubPalindrome(int start, int end, String s) {

		if(start==end){
			start=start+1;
			this.getSubPalindrome(start, endIndex, s);
		}else{
			if (c[start] != c[end]) {
				// �ⲿѭ����endÿ�εݹ���ǰ��һλ
				if (count == 0) {
					end = end - 1;
					this.getSubPalindrome(start, end, s);
				} else {
					// ���й��ڲ�ѭ����end������λ��count��������0��������ǰ�ݹ�
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
