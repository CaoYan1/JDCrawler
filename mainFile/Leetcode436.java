package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * 题名 : 寻找右区间
 * 题目 : 给定一组区间，对于每一个区间 i，检查是否存在一个区间 j，它的起始点大于或等于区间 i 的终点，这可以称为 j 在 i 的“右侧”。
 * 对于任何区间，你需要存储的满足条件的区间 j 的最小索引，这意味着区间 j 有最小的起始点可以使其成为“右侧”区间。如果区间 j 不存在，则将区间 i 存储为 -1。最后，你需要输出一个值为存储的区间值的数组。
 * 注意:
 *     你可以假设区间的终点总是大于它的起始点。
 *     你可以假定这些区间都不具有相同的起始点。
 *
 * 思路 : TreeMap存储左区间和对应的索引,遍历一遍end查找大于end的最小的Entry
 * @author clay
 * @date 19-2-11 19:51
 */
public class Leetcode436 {


     public class Interval {
         int start;
         int end;
         Interval() { start = 0; end = 0; }
         Interval(int s, int e) { start = s; end = e; }
     }

    class Solution {
        public int[] findRightInterval(Interval[] intervals) {
            int[] result = new int[intervals.length];
            TreeMap<Integer, Integer> map = new TreeMap<>();
            for(int i = 0; i < intervals.length; i++){
                map.put(intervals[i].start, i);
            }
            for (int i = 0; i < intervals.length; i++){
                Map.Entry<Integer, Integer> entry = map.ceilingEntry(intervals[i].end);
                result[i] = entry == null ? -1 : entry.getValue();
            }
            return result;
        }
    }
}
