package com.cy.algorithm.leetcode.medium;

import java.util.HashMap;

/**
 * 题名 : 一和零
 * 题目 : 在计算机界中，我们总是追求用有限的资源获取最大的收益。
 * 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
 * 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。　
 *
 * 思路 : 背包问题思路
 * @author clay
 * @date 19-3-1 09:46
 */
public class Leetcode474 {

    public static void main(String[] args) {
        Solution s = new Leetcode474().new Solution();
        System.out.println(s.findMaxForm(new String[]{"10","0001","111001","1","0"},5,3));
    }

    class Solution{

        public int findMaxForm(String[] strs, int m, int n) {
            if (strs.length <= 0 || m <= 0 || n <= 0){
                return 0;
            }
            int[] count0 = new int[strs.length];
            for (int i = 0; i < strs.length; i++){
                for (int j = 0; j < strs[i].length(); j++){
                    if (strs[i].charAt(j) == '0'){
                        count0[i]++;
                    }
                }
            }
            int[][] dp = new int[m+1][n+1];
            for (int i = 0; i < count0.length; i++){
                int c0 = count0[i], c1 = strs[i].length() - c0;
                for (int j = m; j >= c0; j--){
                    for (int k = n; k >= c1; k--){
                        dp[j][k] = Math.max(dp[j][k], dp[j-c0][k-c1] + 1);
                    }
                }
            }
            return dp[m][n];
        }
    }
}
