package algorithm;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
/*
 * 实现目标字符串中a-z出现次数，并得到最大的字符
 * chenbo
 */
public class SumOfWords {

	public static Map<Character,Integer> countChars(String str){
		Map<Character,Integer> map = new HashMap<Character, Integer>();
		for(int i=0;i<str.length();i++){
			char c = str.charAt(i);
			if(map.containsKey(c)){
				int temp = map.get(c)+1;
				map.put(c, temp);
			}else{
				map.put(c, 1);
			}
		}
		return map;
		
	}
	/*
	 *这里其实也不用对map排序，当做扩展了
	 */
	public static void SortMap(Map<Character,Integer>  map){
		
		List<Map.Entry<Character,Integer>> listData = new ArrayList<Map.Entry<Character,Integer>>(map.entrySet());
		Collections.sort(listData,new Comparator<Map.Entry<Character,Integer>>(){

			@Override
			public int compare(Entry<Character, Integer> o1,
					Entry<Character, Integer> o2) {
				// TODO Auto-generated method stub
				if(o2.getValue()!=null&&o1.getValue()!=null&&o2.getValue().compareTo(o1.getValue())>0){    
	                return 1;    
	               }else{    
	                return -1;    
	               }    
			}
			
		});
		System.out.println(listData);
		System.out.println(listData.get(0));
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String character = "fsdkjfklsdjfksdlkjdsfoweiopriewfklsdkfldksaflkdsafldkfsieoirwpoiroewofkdsfksldkf";
		Map<Character,Integer> map = new HashMap<Character, Integer>();
		map = countChars(character);
		SortMap(map);
	}

}
