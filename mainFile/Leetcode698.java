package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;

/**
 * 题名 : 划分k个相等的子集
 * 题目 : 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
 *
 * 思路 : 计算数组所有元素的和除以k得到每一部分的和为N,从大到小排序,然后回溯查找k个N
 * 执行时间 : 10ms
 * @author clay
 * @date 18-11-12 16:04
 */
public class Leetcode698 {

    private boolean visit[];
    private int partN;
    private int []nums;

    private boolean dfs(int target, int n){
        if(target == 0){
            if(n == 0){
                return true;
            }else {
                n--;
                target = partN;
            }
        }

        for(int i = nums.length-1; i >= 0; i--){
            if(visit[i] || nums[i] > target){
               continue;
            }
            visit[i] = true;
            if(dfs(target-nums[i],n)){
                return true;
            }else {
                visit[i] = false;
            }

        }
        return false;
    }

    public boolean canPartitionKSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        this.nums = nums;
        visit = new boolean[nums.length];
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for(int n : nums){
            if(n > max){
                max = n;
            }
            sum += n;
        }
        partN = sum / k;
        if(sum % k != 0 || max > partN){
            return false;
        }
        return dfs(partN,k-1);
    }

    public static void main(String ...args){
        Leetcode698 p = new Leetcode698();
        System.out.println(p.canPartitionKSubsets(new int[]{4, 3, 2, 3, 5, 2, 1},4));
    }
}
