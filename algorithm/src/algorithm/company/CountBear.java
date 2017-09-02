package algorithm.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;
import java.util.TreeMap;

public class CountBear {
	
	//map 小熊战斗力 和当前饥饿值
	//list m个元素  每个表示可以补充的饥饿值
	//n个小熊 m个糖
	public static void countBear(Integer bearNum,Map<Integer,Integer> map,List<Integer> powerNum){
		
		List<Integer> list1 = new ArrayList<Integer>();
		//循环map
		for (Entry<Integer, Integer> entry : map.entrySet()) {
				Integer hungryNum = entry.getValue();
				//循环吃糖补充饥饿值，如果吃饱或吃撑前，则换下一个人吃
				for(int i=0;i<powerNum.size();i++){
					System.out.println("战斗力为："+ entry.getKey().toString() + "的熊要去吃power为" 
							+ powerNum.get(i) + "的糖" );
					System.out.println("当前饥饿度为：" + entry.getValue().toString());
					if(list1.contains(i)){
						System.out.println("已被其他熊吃掉");
						continue;
					}
					Integer power = powerNum.get(i);
					
					if(hungryNum - power >= 0){
						hungryNum = hungryNum - power;
						map.put(entry.getKey(), hungryNum);
						System.out.println("吃了power为：" + entry.getValue().toString() + "的糖" );
						System.out.println("吃完饥饿度为   ：" + hungryNum );
						list1.add(i);
					}else{
						System.out.println("power为" 
								+ powerNum.get(i) + "的糖高于自己的饥饿值,不能吃" );
						continue;
					}
					System.out.println("===================================");
				}
			}
		for(Entry<Integer,Integer> entry : map.entrySet()){
			System.out.println("熊的战斗力为" + entry.getKey().toString() +"========熊的饥饿度为" 
					+ entry.getValue().toString());
		}
	}
	
	public static void main(String[] args){
		int rowIndex = 0;
		int bearNum = 0;
		int sugarNum = 0;
		Map<Integer,Integer> map = new TreeMap<Integer,Integer>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o2.compareTo(o1);
			}
		});
		List<Integer> list = new ArrayList<Integer>();
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()){
			String str = sc.nextLine(); 
			if(str.equals("quit")) break;
			//第一行输入小熊数量n和m
			if(rowIndex == 0){
				String[] strs =str.split(" ");
				if(strs.length != 2){
					System.out.println("输入格式错误，请用空格隔开");
					return;
				}else{
					bearNum = Integer.parseInt(strs[0]);
					sugarNum = Integer.parseInt(strs[1]);
				}
			}
			//第二行输入每个糖可补充的饥饿值
			else if(rowIndex==1){
				String[] strs =str.split(" ");
				for(int i=0;i<strs.length;i++){
					if(strs[i].equals("")){
						continue;
					}else{
						list.add(Integer.parseInt(strs[i]));
					}
				}
			}
			//其他行接受每个小熊的战斗力和饥饿值
			else{
				String[] strs =str.split(" ");
				if(strs.length != 2){
					System.out.println("输入格式错误，请用空格隔开");
					return;
				}else{
					map.put(Integer.parseInt(strs[0]), Integer.parseInt(strs[1]));
				}
			}
			rowIndex ++;
		}
	    Integer[] array = new Integer[list.size()];
	    array = list.toArray(array);
	    Arrays.sort(array);
	    list = Arrays.asList(array);
	    Collections.reverse(list);
	    countBear(bearNum,map,list);
	    
	}

}
