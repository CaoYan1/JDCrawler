package com.cy.algorithm.leetcode.medium;

/**
 * 题名 :　有序链表转换为二叉搜索树
 * 题目 : 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
 * 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
 *
 * 思路 : 找到链表中点,递归左右子树
 *
 * @author clay
 * @date 19-2-14 16:19
 */
public class Leetcode109 {

    public static void main(String[] args) {
        Solution s = new Leetcode109().new Solution();
        ListNode l1 = new Leetcode109().new ListNode(-10);
        ListNode l2 = new Leetcode109().new ListNode(-3);
        ListNode l3 = new Leetcode109().new ListNode(0);
        ListNode l4 = new Leetcode109().new ListNode(5);
        ListNode l5 = new Leetcode109().new ListNode(9);
        l1.next = l2;l2.next=l3;l3.next=l4;l4.next=l5;
        System.out.println(s.sortedListToBST(l1));
    }

     public class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
     }

     public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

    class Solution {

         public TreeNode doSortedListToBST(ListNode head, int length){
             if (length <= 0){
                 return null;
             }
             if (length == 1){
                 return new TreeNode(head.val);
             }
             ListNode left = head, right;
             for (int i = 1; i < length/2; i++){
                 head = head.next;
             }
             ListNode rootVal = head.next;
             head.next = null;
             right = rootVal.next;
             TreeNode root = new TreeNode(rootVal.val);
             root.left = doSortedListToBST(left, length / 2);
             root.right = doSortedListToBST(right, length - length / 2 - 1);
             return root;
         }

         public TreeNode sortedListToBST(ListNode head) {
             int length = 1;
             ListNode temp = head;
             while ((temp = temp.next) != null){
                 length++;
             }
             return doSortedListToBST(head, length);
         }
    }
}
