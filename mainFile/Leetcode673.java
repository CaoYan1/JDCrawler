package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 最长递增子序列的个数
 * 题目 : 给定一个未排序的整数数组，找到最长递增子序列的个数。
 *
 * 思路 : 类似于最长递增子序列的动态规划解法,在dp中多加一条信息为出现的次数,最后统计最长的出现的次数.
 *
 * @author clay
 * @date 19-2-12 19:16
 */
public class Leetcode673 {

    public static void main(String[] args) {
        Solution s = new Leetcode673().new Solution();
        System.out.println(s.findNumberOfLIS(new int[]{2,2,2,2,2}));
    }

    class Solution {
        public int findNumberOfLIS(int[] nums) {
            int[][] dp = new int[nums.length][2];
            dp[0][0] = dp[0][1] = 1;
            int m = 1, t = 1;
            for (int i = 1; i < nums.length; i++){
                int max = 1;
                int times = 1;
                for (int j = 0; j < i; j++){
                    if (nums[j] < nums[i]){
                        int curLen = dp[j][0] + 1;
                        if (curLen > max){
                            max = curLen;
                            times = dp[j][1];
                        }else if (curLen == max){
                            times += dp[j][1];
                        }
                    }
                }
                dp[i][0] = max;
                dp[i][1] = times;
                if (max == m){
                    t += times;
                }
                if(max > m){
                    m = max;
                    t = times;
                }
            }
            return t;
        }
    }
}
