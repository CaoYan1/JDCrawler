package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 最多能完成排序的块
 * 题目 : 数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
 * 我们最多能将数组分成多少块？
 *
 * 思路 : 搜索一遍,找到当前最大值,如果到达最大值索引就可以分成一块
 * @author clay
 * @date 19-3-2 09:04
 */
public class Leetcode769 {

    class Solution {
        public int maxChunksToSorted(int[] arr) {
            int count = 0;
            int pos = 0;
            for (int i = 0; i < arr.length; i++){
                pos = Math.max(pos, arr[i]);
                if (i == pos){
                    count++;
                }
            }
            return count;
        }
    }
}
