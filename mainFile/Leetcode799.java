package com.cy.algorithm.leetcode.medium;

import java.util.HashMap;

/**
 * 题名 : 香槟塔
 * 题目 : 我们把玻璃杯摆成金字塔的形状，其中第一层有1个玻璃杯，第二层有2个，依次类推到第100层，每个玻璃杯(250ml)将盛有香槟。
 * 从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）
 * 例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。
 * 现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比例（i 和 j都从0开始）。
 *
 * 思路 : 递归上一层左右两个杯子的溢出容量,用hashmap缓存已经递归过的杯子.
 * @author clay
 * @date 19-1-11 19:45
 */
public class Leetcode799 {

    class Solution {

        public HashMap<Integer,Double> cache = new HashMap<>();

        public double doChampagneTower(int poured, int query_row, int query_glass) {
            Double result;
            if((result = cache.get(query_row * 100 + query_glass)) != null){
                System.out.println(result);
                return result;

            }
            if(query_row == query_glass && query_row == 0){
                return poured;
            }else {
                double left = 0d, right = 0d;
                if(query_glass-1>=0){
                    left = doChampagneTower(poured,query_row-1,query_glass-1);
                    if(left > 1){
                        left = (left - 1) / 2;
                    }else {
                        left = 0;
                    }
                }
                if(query_glass < query_row){
                    right = doChampagneTower(poured,query_row-1,query_glass);
                    if(right > 1){
                        right = (right - 1) / 2;
                    }else {
                        right = 0;
                    }
                }
                result = left + right;
                cache.put(query_row * 100 + query_glass,result);
                return result;
            }
        }
        public double champagneTower(int poured, int query_row, int query_glass){
            double result = doChampagneTower(poured,query_row,query_glass);
            if(result > 1){
                result = 1;
            }
            return result;
        }
    }

    public static void main(String[] args){
        Solution solution = new Leetcode799().new Solution();
        System.out.println(solution.champagneTower(100,13,5));
    }
}
