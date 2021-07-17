package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;

/**
 * 题名 : 下一个更大的元素II
 * 题目 : 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
 *
 * 思路 : 创建一个栈,遍历两次数组,栈顶比当前小的全部出栈,然后当前元素入栈,第二次遍历不入栈
 * @author clay
 * @date 19-2-17 15:01
 */
public class Leetcode503 {

    public static void main(String[] args) {
        Solution s = new Leetcode503().new Solution();
        System.out.println(s.nextGreaterElements(new int[]{1,2,1}));
    }

    class Solution {
        public int[] nextGreaterElements(int[] nums) {
            LinkedList<int[]> stack = new LinkedList<>();
            int[] result = new int[nums.length];
            for (int i = 0; i < nums.length; i++){
                while (true){
                    if (stack.isEmpty()){
                        stack.push(new int[]{nums[i], i});
                        break;
                    }
                    int[] top = stack.peek();
                    if (top[0] < nums[i]){
                        result[top[1]] = nums[i];
                        stack.pop();
                    }else {
                        stack.push(new int[]{nums[i], i});
                        break;
                    }
                }
            }
            for (int i = 0; i < nums.length && !stack.isEmpty() && i < stack.peek()[1]; i++){
                while (!stack.isEmpty()){
                    int[] top = stack.peek();
                    if (top[0] < nums[i]){
                        result[top[1]] = nums[i];
                        stack.pop();
                    }else {
                        break;
                    }
                }
            }
            while (!stack.isEmpty()){
                result[stack.pop()[1]] = -1;
            }
            return result;
        }
    }
}
