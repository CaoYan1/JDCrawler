package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 区间子数组个数
 * 题目 : 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。
 * 求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。
 *
 * 思路 : 动态规划,dp[i][0]为以i为末尾的符合条件子数组个数,dp[i][1]为以i为
 * 末尾连续小于L的个数,如果A[i] ∈ [L,R],则dp[i][0] = dp[i-1][0] + 1 + dp[i-1][1],dp[i][1]=0
 * 如果 A[i] < L 则dp[i]=dp[i-1][0],dp[i][1]=do[i-1][1]+1
 * 否则 dp[i][0]=dp[i][1]=0
 * @author clay
 * @date 19-1-6 19:24
 */
public class Leetcode795 {

    public static void main(String[] args){
        Solution s = new Leetcode795().new Solution();
        System.out.println(s.numSubarrayBoundedMax(new int[]{73,55,36,5,55,14,9,7,72,52},32,69));
    }

    class Solution {
        public int numSubarrayBoundedMax(int[] A, int L, int R) {
            int[][] dp = new int[A.length][2];
            int count = 0;
            dp[0][0] = (A[0] >= L && A[0] <= R) ? 1 : 0;
            count += dp[0][0];
            dp[0][1] = A[0] < L ? 1 : 0;
            for(int i = 1; i < A.length; i++){
                if (A[i] >= L && A[i] <= R){
                    dp[i][0] = dp[i - 1][0] + 1 + dp[i - 1][1];
                    dp[i][1] = 0;
                }else if (A[i] < L){
                    dp[i][0] = dp[i - 1][0];
                    dp[i][1] = dp[i - 1][1] + 1;
                }
                count += dp[i][0];
            }
            return count;
        }
    }
}
