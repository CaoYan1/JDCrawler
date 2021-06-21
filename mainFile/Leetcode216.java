package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;
import java.util.List;

/**
 * 题名 : 组合总和III
 * 题目 : 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
 *
 * 思路 : dfs
 * @author clay
 * @date 19-2-21 16:21
 */
public class Leetcode216 {

    public static void main(String[] args) {
        Solution s = new Leetcode216().new Solution();
        System.out.println(s.combinationSum3(3,7));

    }

    class Solution {

        private List<List<Integer>> result = new LinkedList<>();

        private int k;

        private int n;

        public void dfs(int d, int sum, int last, LinkedList<Integer> cur){
            if (d > k || sum > n){
                return;
            }
            if (d == k && sum == n){
                result.add((LinkedList)cur.clone());
            }
            for (int i = last + 1; i <= 9; i++){
                cur.push(i);
                dfs(d + 1, sum + i, i, cur);
                cur.pop();
            }

        }

        public List<List<Integer>> combinationSum3(int k, int n) {
            this.k = k;
            this.n = n;
            dfs(0, 0, 0, new LinkedList<>());
            return result;
        }
    }
}
