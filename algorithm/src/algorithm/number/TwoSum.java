package algorithm.number;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import algorithm.utilty.ArrayToMap;

/*
 * Requirement:
 * Give an array of Integers,return indices of the two numbers such they add up to a specific target
 * you may sssume that each input would have exactly one solution,and you may not use the same element twice
 * 
 * Example:
 * Given nums = [2, 7, 11, 15], target = 9,
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * Author: ChenBo
 * Date :2016.2.23
 */
public class TwoSum {
	public static int[] twoSum(int[] nums, int target){
		int[] result =new int[2];
		Map<Integer,Integer> maps = ArrayToMap.transfer(nums);
		int temp = 0;
		int tempIndex = 0;
		for(int i =0;i<nums.length;i++){
			temp = target - nums[i];
			if(maps.containsKey(temp)){
				result[0] = i;
				result[1] = maps.get(temp);
				return result;
			}
		}
		System.out.println("do not have matching data");
		return null;
	}
	
	public static void main(String[] args){
		int[] initNum = {2, 7, 11, 15,1,3,5,6,9,6};
		int target = 12;
		int[] result = new int[2];
		result = twoSum(initNum,target);
		System.out.println(result[0]+" "+result[1]);
	}
}
