package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;

/**
 * 题名 : 使序列递增的最少交换次数
 * 题目 :我们有两个长度相等且不为空的整型数组 A 和 B 。
 * 我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。
 * 在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。
 * 给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。
 *
 * 思路 : 用dp二维数组存储交换和不交换两种情况的最小交换次数.
 * 要先比较A[i],B[i]与A[i-1],B[i-1]的大小,再记录A[i],B[i]交换与不交换两种情况最小值
 *
 * @author clay
 * @date 18-12-31 14:06
 */
public class Leetcode801 {

    public static void main(String[] args){
        Solution s = new Leetcode801().new Solution();
        System.out.println(s.minSwap(new int[]{0,3,5,8,9},
                new int[]{2,1,4,6,9}));
    }

    class Solution {
        public int minSwap(int[] A, int[] B) {
            int n = A.length;
            int[][] dp = new int[n][2];
            dp[0][1] = 1;
            for(int i = 1; i < n; i++){
                if(Math.min(A[i],B[i]) > Math.max(A[i-1],B[i-1])){
                    dp[i][0] = Math.min(dp[i-1][0],dp[i-1][1]);
                    dp[i][1] = Math.min(dp[i-1][0] + 1,dp[i-1][1] + 1);
                }else if(A[i] > A[i-1] && B[i] > B[i-1]){
                    dp[i][0] = dp[i-1][0];
                    dp[i][1] = dp[i-1][1] + 1;
                }else if(A[i] > B[i-1] && B[i] > A[i-1]){
                    dp[i][0] = dp[i-1][1];
                    dp[i][1] = dp[i-1][0] + 1;
                }else {
                    return Integer.MAX_VALUE;
                }

            }
            return Math.min(dp[n-1][0],dp[n-1][1]);
        }
    }
}
