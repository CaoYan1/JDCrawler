package com.cy.algorithm.leetcode.medium;

/**
 * 题目 :
 *
 * @author clay
 * @date 19-3-1 09:38
 */
public class Leetcode75 {
    class Solution {
        public void sortColors(int[] nums) {
            int i = 0, j = nums.length - 1;
            for (int k = 0; k <= j; k++){
                if (nums[k] == 0){
                    nums[k] = nums[i];
                    nums[i++] = 0;
                }else if (nums[k] == 2){
                    nums[k] = nums[j];
                    nums[j--] = 2;
                    k--;
                }
            }
        }
    }
}
