package com.cy.algorithm.leetcode.medium;

import java.util.HashMap;

/**
 * 题名 : 和为k的子数组
 * 题目 : 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
 *
 * 思路 : 记录数组的前缀和p,即对于p[i]为nums[0] + nums[1] + .... + nums[i]
 * 对于从i到j连续的子数组和为p[j]-p[i],所以将前缀和放入哈希表并记录出现的次数,对于以j为子数组的
 * 末尾的子数组,和为k的子数组的数量为满足p[i]=p[j]-k等式i的数量.
 *
 * @author clay
 * @date 19-4-8 17:09
 */
public class Leetcode560 {

    class Solution {
        public int subarraySum(int[] nums, int k) {
            HashMap<Integer, Integer> sumTimes = new HashMap<>();
            sumTimes.put(0, 1);
            int result = 0;
            int sum = 0;
            for (int num : nums){
                sum += num;
                result += sumTimes.getOrDefault(sum - k, 0);
                sumTimes.put(sum, sumTimes.getOrDefault(sum, 0) + 1);
            }
            return result;
        }
    }
}
