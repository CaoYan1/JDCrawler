package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * 题名 : 组合总和
 * 题目 : 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 * candidates 中的数字可以无限制重复被选取。　
 *
 * 思路 : dfs
 * @author clay
 * @date 19-3-6 08:52
 */
public class Leetcode39 {

    public static void main(String[] args) {
        Solution s = new Leetcode39().new Solution();
        System.out.println(s.combinationSum(new int[]{2,3,5}, 8));
    }

    class Solution {

        private List<List<Integer>> result = new LinkedList<>();

        private void dfs(int[] candidates, int target, int cur, LinkedList<Integer> list, int n){
            if (target < cur){
                return;
            }
            if (target == cur){
                result.add((List<Integer>) list.clone());
            }
            for (int i = n; i < candidates.length; i++){
                list.push(candidates[i]);
                dfs(candidates, target, cur + candidates[i], list, i);
                list.pop();
            }
        }

        public List<List<Integer>> combinationSum(int[] candidates, int target) {
            dfs(candidates, target, 0, new LinkedList<>(), 0);
            return result;
        }
    }
}
