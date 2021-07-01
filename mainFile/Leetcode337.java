package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 打家劫舍III
 * 题目 :在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
 * 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
 *
 * 思路 : 递归算法,每一个节点有偷或者不偷两种选择,然而递归到下一层
 * 执行时间 : 635ms
 * @author clay
 * @date 18-12-2 19:35
 */
public class Leetcode337 {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
    class Solution {

        public int rob(TreeNode root) {
            if(root == null){
                return 0;
            }
            int value0 = 0, value1 = 0;
            if(root.left != null){
                value0 += rob(root.left.left) + rob(root.left.right);
                value1 += rob(root.left);
            }
            if(root.right != null){
                value0 += rob(root.right.left) + rob(root.right.right);
                value1 += rob(root.right);
            }
            return Math.max(value0 + root.val, value1);
        }
    }
}
