package algorithm.number;

/*
 * Reverse digits of an integer.
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 * 
 * Author:ChenBo
 * Date：2017.3.3
 */
public class ReverseNum {
	
	public static int reverse(int x){
		if(x>Math.pow(2.0, 31.0))
			return 0;
		if(x<Math.pow(2.0, -31.0))
			return 0;
		
		String s = x+"";
		char[] c = s.toCharArray();
		int result =0;
		
		for(int i=c.length;i>0;i--){
			//int b = c[i-1];  有疑问  char 7 转换为int是55  char>int
			result += Integer.parseInt(String.valueOf(c[i-1])) * (int)Math.pow(10, i-1); 
		}
		System.out.println(result);
		return result;
	}
	public static void main(String[] args){
		reverse(1234567);
	}
}
