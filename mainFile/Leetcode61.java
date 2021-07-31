package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 旋转链表
 * 题目 : 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
 *
 * 思路 : 将末尾k个移到开头
 *
 * @author clay
 * @date 19-3-4 09:06
 */
public class Leetcode61 {

     public class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
     }

    class Solution {
        public ListNode rotateRight(ListNode head, int k) {
            if (k == 0 || head == null || head.next == null){
                return head;
            }
            ListNode start = head, end = head, last = head;
            int size = 1;
            int length = 1;
            while (end.next != null){
                size++;
                end = end.next;
                if (length == k){
                    last = start;
                    start = start.next;
                }else {
                    length++;
                }
            }
            if (length < k){
                k = k % size;
                if (k == 0){
                    return head;
                }
                for (int i = 0; i < length - k - 1; i++){
                    start = start.next;
                }
            } else if (size == k){
                return head;
            } else {
                start = last;
            }
            ListNode ret = start.next;
            start.next = null;
            end.next = head;
            return ret;
        }
    }
}
