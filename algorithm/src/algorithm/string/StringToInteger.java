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
			//total = 10 * total + digit; �������Ҳ����!!
		}
		System.out.println(result);
		return result;
	}
	
	public byte deUnicode(){
		return 0;
	}
	public int byteConvertInt(byte[] bytes) {
	    int s = 0;
	    //&0xff�õ�������ֵ������24λ��������ԣ���8λ����ʵ�����֣�������24λ����Ϊ0��
	    int s0 = bytes[0] & 0xff;// ���λ,java��Լ�����λ�ֽڿ�ǰ
	    int s1 = bytes[1] & 0xff;
	    int s2 = bytes[2] & 0xff;
	    int s3 = bytes[3] & 0xff;
	    //intΪ32λ,s1���ư�λ�õ� 8-16λ��ֵ���Դ����� 
	    s1 <<= 8;
	    s2 <<= 16;
	    s3 <<= 24;
	    //ͨ��|���� ��4��8λ���32λ�Ķ�����  
	    s = s0 | s1 | s2 | s3;
	    System.out.println(s);
	    return s;
	}
	
	public static void main(String[] args){
		StringToInteger sti = new StringToInteger();
		sti.stringToInt("456456");
		
	}
}
