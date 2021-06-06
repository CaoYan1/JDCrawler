package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * 题名 : 二叉树的层次遍历
 * 题目 : 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
 *
 * 思路 : 队列,广度优先搜索
 *
 * @author clay
 * @date 19-2-27 08:34
 */
public class Leetcode102 {

     public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

    class Solution {
        public List<List<Integer>> levelOrder(TreeNode root) {
            if (root == null){
                return new LinkedList<>();
            }
            List<List<Integer>> result = new LinkedList<>();
            Queue<TreeNode> queue = new LinkedList<>();
            TreeNode place = new TreeNode(-1);
            queue.offer(root);
            queue.offer(place);
            List<Integer> layer = new ArrayList<>();
            while (!queue.isEmpty()){
                TreeNode cur = queue.poll();
                if (cur == null){
                    continue;
                }
                if (cur == place){
                    if (queue.isEmpty()){
                        break;
                    }
                    queue.offer(place);
                    result.add(layer);
                    layer = new LinkedList<>();
                } else {
                    layer.add(cur.val);
                    queue.offer(cur.left);
                    queue.offer(cur.right);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {

    }

}
