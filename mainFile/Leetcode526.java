package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 优美的排列
 * 题目 : 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
 *     第 i 位的数字能被 i 整除
 *     i 能被第 i 位上的数字整除
 * 现在给定一个整数 N，请问可以构造多少个优美的排列？
 *
 * 思路 : dfs
 * @author clay
 * @date 19-3-6 09:26
 */
public class Leetcode526 {

    class Solution {

        private int result = 0;

        private void dfs(int N, int visited, int n){
            if (n == N){
                result++;
                return;
            }
            for (int i = 1; i <= N; i++){
                int mask = 1 << i;
                if (((i == n) || (i > n && i % n == 0) || (i < n && n % i == 0)) && (visited & mask) == 0){
                    visited |= mask;
                    dfs(N, visited, n + 1);
                    visited ^= mask;
                }
            }
        }

        public int countArrangement(int N) {
            dfs(N, 0, 0);
            return result;
        }
    }
}
