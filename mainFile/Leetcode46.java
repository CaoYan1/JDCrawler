package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * 题名 : 全排列
 * 题目 : 给定一个没有重复数字的序列，返回其所有可能的全排列。
 *
 * 思路 : 交换位置递归
 * @author clay
 * @date 19-3-2 08:44
 */
public class Leetcode46 {

    class Solution {

        private List<List<Integer>> result = new LinkedList<>();

        public void doPermute(ArrayList<Integer> nums, int i){

            if (i >= nums.size()){
                result.add((ArrayList)nums.clone());
            }
            for (int j = i; j < nums.size(); j++){
                Collections.swap(nums, i, j);
                doPermute(nums, i + 1);
                Collections.swap(nums, i, j);
            }
        }

        public List<List<Integer>> permute(int[] nums) {
            ArrayList<Integer> list = new ArrayList<>(nums.length);
            for (int num : nums){
                list.add(num);
            }
            doPermute(list, 0);
            return result;
        }
    }

}
