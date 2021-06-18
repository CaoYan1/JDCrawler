package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 对链表进行插入排序
 * 题目 : 对链表进行插入排序
 * 思路 : 遍历链表,将当前结点移除,因为是单链表,然后正向遍历找到合适位置插入
 * @author clay
 * @date 19-2-5 17:04
 */
public class Leetcode147 {

     static public class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
     }

    public static void main(String[] args) {
        Solution s = new Leetcode147().new Solution();
        ListNode head = new ListNode(4);
        ListNode temp = head;
        head = (head.next = new ListNode(2));
        head = (head.next = new ListNode(1));
        head = (head.next = new ListNode(3));
        s.insertionSortList(temp);
        System.out.println('a');
    }

    class Solution {
        public ListNode insertionSortList(ListNode head) {
            if(head == null || head.next == null){
                return head;
            }
            ListNode cur = head.next;
            ListNode last = head;
            while(cur != null){
                ListNode temp = cur;
                cur = cur.next;
                last.next = cur;
                ListNode pos = head;
                ListNode l = null;
                while (pos != null && temp.val > pos.val && pos != cur){
                    l = pos;
                    pos = pos.next;
                }
                if(l != null){
                    l.next = temp;
                }else {
                    head = temp;
                }
                if(pos != null){
                    temp.next = pos;
                }
                if(last.next == temp){
                    last = temp;
                }
            }
            return head;
        }
    }
}
