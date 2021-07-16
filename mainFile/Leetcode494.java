package com.cy.algorithm.leetcode.medium;

import java.util.HashMap;
import java.util.Map;

/**
 * 题名 : 目标和
 * 题目 : 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
 * 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
 *
 * 思路 : dfs + 记忆化搜索
 * @author clay
 * @date 19-2-25 22:07
 */
public class Leetcode494 {

    public static void main(String[] args) {
        Solution s = new Leetcode494().new Solution();
        System.out.println(s.findTargetSumWays(new int[]{1,1,1,1,1}, 3));
    }

    class Solution {

        private Map<Integer, Integer> map = new HashMap<>();

        public int dfs(int[] nums, int i, int S){
            if (S > 1001){
                return 0;
            }
            if (i == nums.length && S == 0){
                return 1;
            }else if (i >= nums.length){
                return 0;
            }
            Integer cache = map.getOrDefault(i * 2000 + S, null);
            if (cache != null){
                return cache;
            }
            Integer result = dfs(nums, i + 1, S + nums[i])
                    + dfs(nums, i + 1, S - nums[i]);
            map.put(i * 2000 + S, result);
            return result;
        }

        public int findTargetSumWays(int[] nums, int S) {
            if (nums.length == 0 && S == 0){
                return 1;
            }
            if (nums.length == 0){
                return 0;
            }
            return dfs(nums, 0, S);
        }
    }
}
