package algorithm.string;

/*
 * Implement atoi to convert a string to an integer.
 * 
 * Author:ChenBo
 * Date:2017.3.4
 */
public class StringToInteger {
	
	public int stringToInt(String s){
		byte[] bt = s.getBytes();
		char[] c = s.toCharArray();
		int result = 0,temp=0;
		for(int i=0;i<c.length;i++){
			if(result>Math.pow(2.0, 31.0))
				return 0;
			if(result<-Math.pow(2.0, 31.0))
				return 0;
			temp = ((bt[i]-'0') & 0xff);
			result += temp * Math.pow(10, bt.length-i-1);
			//total = 10 * total + digit; 这个方案也不错!!
		}
		System.out.println(result);
		return result;
	}
	
	public byte deUnicode(){
		return 0;
	}
	public int byteConvertInt(byte[] bytes) {
	    int s = 0;
	    //&0xff得到二进制值，（高24位具有随机性，低8位才是实际数字，这样高24位设置为0）
	    int s0 = bytes[0] & 0xff;// 最低位,java中约定最低位字节靠前
	    int s1 = bytes[1] & 0xff;
	    int s2 = bytes[2] & 0xff;
	    int s3 = bytes[3] & 0xff;
	    //int为32位,s1左移八位得到 8-16位的值，以此类推 
	    s1 <<= 8;
	    s2 <<= 16;
	    s3 <<= 24;
	    //通过|操作 把4组8位组成32位的二进制  
	    s = s0 | s1 | s2 | s3;
	    System.out.println(s);
	    return s;
	}
	
	public static void main(String[] args){
		StringToInteger sti = new StringToInteger();
		sti.stringToInt("456456");
		
	}
}
