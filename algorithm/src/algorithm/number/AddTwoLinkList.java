package algorithm.number;

import algorithm.utilty.SimpleLinkList;
import algorithm.utilty.SimpleLinkList.ListNode;
/*
 * Requirement:
 * You are given two non-empty linked lists representing two non-negative integers. 
 * The digits are stored in reverse order and each of their nodes contain a single digit. 
 * Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * 
 * Example:
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * 
 * Author:Chenbo
 * Date: 2016.2.23
 */
public class AddTwoLinkList {
	public static ListNode addTwoLinkList(ListNode l1,ListNode l2){
		ListNode pre = new SimpleLinkList().new ListNode(0);
		//Õ∑÷∏’Î
		ListNode head = pre;
		int carry = 0;
		while(l1!=null || l2 !=null || carry !=0){
			ListNode node = new SimpleLinkList().new ListNode(0);
			int sum = (l1!=null? l1.val:0) + (l2!=null? l2.val : 0) +carry;
		    carry = sum/10;
		    node.val = sum % 10;
		    pre.next = node;
		    pre = node;
		    
		    l1 = (l1 == null) ? l1 : l1.next;
            l2 = (l2 == null) ? l2 : l2.next;
		    
		}
		ListNode result = new SimpleLinkList().new ListNode(0);
		result = head.next;
		while(result!=null){
			System.out.println(result.val);
			result = result.next;
		}
		return head.next;
	}
	
	public static void main(String[] args) {
		int [] array1 = {2,4,3};
		int [] array2=  {5,6,4};
		ListNode pre1 = new SimpleLinkList().new ListNode(0);
		ListNode head1 = pre1;
		ListNode pre2 = new SimpleLinkList().new ListNode(0);
		ListNode head2 = pre2;
		for(int i =0;i<array1.length;i++){
			ListNode node1 = new SimpleLinkList().new ListNode(0);
			ListNode node2 = new SimpleLinkList().new ListNode(0);
			node1.val = array1[i];
			node2.val = array2[i];
			pre1.next = node1;
			pre1 = node1;
			pre2.next = node2;
			pre2 = node2;
		}
		addTwoLinkList(head1.next,head2.next);
	}
}


