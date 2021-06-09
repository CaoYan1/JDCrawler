package com.cy.algorithm.leetcode.medium;

import java.util.HashSet;
import java.util.Set;

/**
 * 题名 : 从中序与后序遍历序列构造二叉树
 * 题目 : 根据一棵树的中序遍历与后序遍历构造二叉树。
 *
 * 思路 : 后序遍历的最后一个数字一定是当前结点的右子结点,根据这个规律递归
 *
 * @author clay
 * @date 19-3-15 20:15
 */
public class Leetcode106 {

    public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

    class Solution {

        private int index;

        public TreeNode buildTree(int[] inorder, int[] postorder) {
            index = postorder.length - 1;
            return doBuildTree(inorder,0,index,postorder);
        }

        private TreeNode doBuildTree(int[] inorder, int l, int r, int[] postorder){
            if (l > r){
                return null;
            }
            int n = postorder[index];
            TreeNode result = null;
            for (int i = l; i <= r; i++){
                if (inorder[i] == n){
                    index--;
                    result = new TreeNode(n);
                    result.right = doBuildTree(inorder, i+1, r, postorder);
                    result.left = doBuildTree(inorder, l, i - 1, postorder);
                    break;
                }
            }
            return result;
        }
    }

}
