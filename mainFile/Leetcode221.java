package com.cy.algorithm.leetcode.medium;

/**
 * 题名 :最大正方形
 * 题目 :在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
 *
 * 思路 :动态规划 dp[i][j] = Math.min(dp[i-1][j-1],
 *                                 Math.min(dp[i-1][j],dp[i][j-1])) + 1;
 * 执行时间 : 9ms
 *
 * @author clay
 * @date 18-11-17 16:34
 */
public class Leetcode221 {


    public int maximalSquare(char[][] matrix) {
        if(matrix.length == 0){
            return 0;
        }
        int [][]dp = new int[matrix.length][matrix[0].length];
        int max = 0;
        for(int i = 0; i < dp.length; i++){
            for(int j = 0; j < dp[0].length; j++){
                if(i == 0 || j == 0){
                    dp[i][j] = matrix[i][j] == '1' ? 1 : 0;
                }else {
                    if(matrix[i][j] == '1'){
                        dp[i][j] = Math.min(dp[i-1][j-1],
                                Math.min(dp[i-1][j],dp[i][j-1])) + 1;
                    }
                }
                if(dp[i][j] > max){
                    max = dp[i][j];
                }
            }
        }
        return max * max;
    }
}
