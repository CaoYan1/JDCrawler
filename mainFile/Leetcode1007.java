package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;

/**
 * 题名 : 行相等的最少多米诺旋转
 * 题目 : 在一排多米诺骨牌中，A[i] 和 B[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）
 * 我们可以旋转第 i 张多米诺，使得 A[i] 和 B[i] 的值交换。
 * 返回能使 A 中所有值或者 B 中所有值都相同的最小旋转次数。
 * 如果无法做到，返回 -1.
 *
 * 思路 : 找到众数,查找交换次数
 *
 * @author clay
 * @date 19-3-10 11:06
 */
public class Leetcode1007 {
    class Solution {
        public int minDominoRotations(int[] A, int[] B) {
            int[] arr = Arrays.copyOf(A,A.length + B.length);
            int n = 0;
            for (int i = 0; i < B.length; i++){
                arr[A.length + i] = B[i];
            }
            Arrays.sort(arr);
            int times = 1;
            int num = arr[0];
            for (int i = 0; i < arr.length; i++){
                if (arr[i] == num){
                    times++;
                }else {
                    times = 1;
                    num = arr[i];
                }
                if (times >= arr.length / 2){
                    n = num;
                    break;
                }
            }
            int countA = 0;
            for (int i = 0; i < A.length; i++){
                if (B[i] == n){
                    continue;
                }else if (A[i] == n){
                    countA++;
                }else {
                    return -1;
                }
            }
            int countB = 0;
            for (int i = 0; i < A.length; i++){
                if (A[i] == n){
                    continue;
                }else if (B[i] == n){
                    countB++;
                }else {
                    return -1;
                }
            }
            return Math.min(countA,countB);
        }
    }
}
