package com.cy.algorithm.leetcode.medium;

import java.util.TreeMap;

/**
 * 题名 : 删除与获得点数
 * 题目 : 给定一个整数数组 nums ，你可以对它进行一些操作。
 * 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
 * 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
 *
 * 思路 : 先用数组保存每个数字出现的次数,然后从小到大记录每个数字操作或不操作分别的最大值,
 * 最终的最大值就是答案
 * @author clay
 * @date 19-2-5 18:13
 */
public class Leetcode740 {

    public static void main(String[] args) {
        Solution s = new Leetcode740().new Solution();
        System.out.println(s.deleteAndEarn(new int[]{8,10,4,9,1,3,5,9,4,10}));
    }

    class Solution {
        public int deleteAndEarn(int[] nums) {
            if (nums == null || nums.length <= 0){
                return 0;
            }
            int[] dp = new int[10001];
            int a = 0, b = 0;
            int max = 0, min = 10001;
            for (int num : nums){
                dp[num]++;
                if(num > max){
                    max = num;
                }
                if(num < min){
                    min = num;
                }
            }
            for(int i = min; i <= max; i++){
                int temp = b + i * dp[i];
                b = Math.max(a, b);
                a = temp;
            }
            return Math.max(a,b);

        }
    }
}
