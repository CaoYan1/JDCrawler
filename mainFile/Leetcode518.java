package com.cy.algorithm.leetcode.medium;

import com.sun.tools.javac.Main;

/**
 * 题名 : 零钱兑换
 * 题目 : 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
 *
 * 思路 : 背包问题,动态规划
 *
 * @author clay
 * @date 19-1-18 18:34
 */
public class Leetcode518 {

    public static void main(String[] args) {
        Solution s = new Leetcode518().new Solution();
        System.out.println(s.change(5,new int[]{1, 2, 5}));
    }

    class Solution {
        public int change(int amount, int[] coins) {
            int a[] = new int[amount+1];
            a[0] = 1;
            for (int i = 0; i < coins.length; i++) {
                for (int j = 1; j <=amount ; j++) {
                    if(j>=coins[i]){
                        a[j] = a[j] + a[j-coins[i]];
                    }
                }
            }
            return a[amount];
        }
    }
}
