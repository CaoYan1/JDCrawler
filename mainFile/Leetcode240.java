package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;

/**
 * 题名 : 搜索二维矩阵
 * 题目 :编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
 *     每行的元素从左到右升序排列。
 *     每列的元素从上到下升序排列。
 *
 * 思路 : 二分法,对于一个二维矩阵,左上是最大值,右下是最小值,如果target不在这个范围内就return false
 * 否则就将矩阵均分为四块,分别递归
 *
 * @author clay
 * @date 19-1-1 13:29
 */
public class Leetcode240 {

    public static void main(String[] args){
        Solution s = new Leetcode240().new Solution();
        System.out.println(s.searchMatrix(new int[][]{{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}},20));
    }

    class Solution {

        public boolean binarySearch(int[][] matrix, int x1, int x2,
                                    int y1, int y2, int target){
            if(x1 > x2 || y1 > y2 || target < matrix[x1][y1] || target > matrix[x2][y2]){
                return false;
            }
            if(x1 == x2 && y1 == y2){
                return matrix[x1][y1] == target;
            }else {
                int x3 = (x1+x2)/2, y3 = (y1+y2)/2;
                return binarySearch(matrix,x1,x3,y1,y3,target)||
                        binarySearch(matrix,x3+1,x2,y1,y3,target)||
                        binarySearch(matrix,x1,x3,y3+1,y2,target)||
                        binarySearch(matrix,x3+1,x2,y3+1,y2,target);
            }


        }

        public boolean searchMatrix(int[][] matrix, int target) {
            if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
                return false;
            }
            return binarySearch(matrix,0,matrix.length-1,0,matrix[0].length-1,target);
        }
    }
}
