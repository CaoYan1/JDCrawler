package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 二叉树剪枝
 * 题目 : 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。
 * 返回移除了所有不包含 1 的子树的原二叉树。
 * ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)
 *
 * 思路 : 递归剪枝
 *
 * @author clay
 * @date 18-12-31 13:30
 */
public class Leetcode814 {


     public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

    class Solution {

         public boolean trim(TreeNode root){
             if(root == null){
                 return true;
             }
             boolean left = trim(root.left);
             boolean right = trim(root.right);
             if(left){
                 root.left = null;
             }
             if(right){
                 root.right = null;
             }
             return root.val == 0 && left && right;

         }

         public TreeNode pruneTree(TreeNode root) {
               if(trim(root)){
                   return null;
               }else {
                   return root;
               }
         }
    }
}
