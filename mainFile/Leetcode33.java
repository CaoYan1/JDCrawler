package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 搜索旋转排序数组
 * 题目 : 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 * 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 * 你可以假设数组中不存在重复的元素。
 * 你的算法时间复杂度必须是 O(log n) 级别。
 *
 * 思路 : o(log n)时间复杂度只能二分查找了,根据数组起始位置数字大小和中间位置的大小可以判断出
 * 目标在中间点左边还是右边.
 * @author clay
 * @date 19-1-21 16:52
 */
public class Leetcode33 {

    public static void main(String[] args){
        Solution s = new Leetcode33().new Solution();
        System.out.println(s.search(new int[]{1,3},3));
    }

    class Solution {

        public int doSearch(int[] nums, int a, int b, int target){
            if(a > b){
                return -1;
            }
            int pivot = (a + b) / 2;
            if(nums[pivot] == target){
                return pivot;
            }
            if((nums[a] > target && (nums[pivot] > nums[a] || nums[pivot] < target)) ||
                    (nums[a] < target && nums[pivot] > nums[a] && nums[pivot] < target)) {
                return doSearch(nums,pivot + 1, b, target);
            }else {
                return doSearch(nums, a , pivot - 1, target);
            }
        }

        public int search(int[] nums, int target) {
            if(nums == null || nums.length <= 0){
                return -1;
            }
            return doSearch(nums,0,nums.length-1,target);
        }
    }
}
