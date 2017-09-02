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
	
	//map С��ս���� �͵�ǰ����ֵ
	//list m��Ԫ��  ÿ����ʾ���Բ���ļ���ֵ
	//n��С�� m����
	public static void countBear(Integer bearNum,Map<Integer,Integer> map,List<Integer> powerNum){
		
		List<Integer> list1 = new ArrayList<Integer>();
		//ѭ��map
		for (Entry<Integer, Integer> entry : map.entrySet()) {
				Integer hungryNum = entry.getValue();
				//ѭ�����ǲ��伢��ֵ������Ա���Գ�ǰ������һ���˳�
				for(int i=0;i<powerNum.size();i++){
					System.out.println("ս����Ϊ��"+ entry.getKey().toString() + "����Ҫȥ��powerΪ" 
							+ powerNum.get(i) + "����" );
					System.out.println("��ǰ������Ϊ��" + entry.getValue().toString());
					if(list1.contains(i)){
						System.out.println("�ѱ������ܳԵ�");
						continue;
					}
					Integer power = powerNum.get(i);
					
					if(hungryNum - power >= 0){
						hungryNum = hungryNum - power;
						map.put(entry.getKey(), hungryNum);
						System.out.println("����powerΪ��" + entry.getValue().toString() + "����" );
						System.out.println("���꼢����Ϊ   ��" + hungryNum );
						list1.add(i);
					}else{
						System.out.println("powerΪ" 
								+ powerNum.get(i) + "���Ǹ����Լ��ļ���ֵ,���ܳ�" );
						continue;
					}
					System.out.println("===================================");
				}
			}
		for(Entry<Integer,Integer> entry : map.entrySet()){
			System.out.println("�ܵ�ս����Ϊ" + entry.getKey().toString() +"========�ܵļ�����Ϊ" 
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
			//��һ������С������n��m
			if(rowIndex == 0){
				String[] strs =str.split(" ");
				if(strs.length != 2){
					System.out.println("�����ʽ�������ÿո����");
					return;
				}else{
					bearNum = Integer.parseInt(strs[0]);
					sugarNum = Integer.parseInt(strs[1]);
				}
			}
			//�ڶ�������ÿ���ǿɲ���ļ���ֵ
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
			//�����н���ÿ��С�ܵ�ս�����ͼ���ֵ
			else{
				String[] strs =str.split(" ");
				if(strs.length != 2){
					System.out.println("�����ʽ�������ÿո����");
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
