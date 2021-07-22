package com.cy.algorithm.leetcode.medium;

import java.util.Random;
import java.util.TreeMap;

/**
 * 题名 : 按权重随机选择
 * 题目 : 给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与 w[i] 成正比。
 *
 * 思路 : 根据权重分布不同的区间,用TreeMap记录区间开始位置和索引,生成随机数根据TreeSet查找索引
 * @author clay
 * @date 19-2-21 16:49
 */
public class Leetcode528 {

    public static void main(String[] args) {
        System.out.println((int)Math.random());
    }

    class Solution {

        //probability and index
        private TreeMap<Integer, Integer> treeMap = new TreeMap<>();

        private int sum = 1;

        public Solution(int[] w) {
            for (int i = 0; i < w.length; i++){
                treeMap.put(sum, i);
                sum += w[i];
            }
        }

        public int pickIndex() {
            int rand = (int)(Math.random() * sum) + 1;
            return treeMap.floorEntry(rand).getValue();
        }
    }
}
