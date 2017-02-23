package algorithm.utilty;

import java.util.HashMap;
import java.util.Map;

public class ArrayToMap {
	private ArrayToMap(){
		
	}
	//int[] to Map
	public static  Map<Integer,Integer> transfer(int[] num){
		Map<Integer,Integer> maps = new HashMap<Integer, Integer>();
		for(int i = 1;i<num.length; i++){
			maps.put(num[i], i);
		}
		return maps;
	}
}
