package com.cy.algorithm.leetcode.medium;

import java.lang.reflect.Method;
import java.util.LinkedList;
import java.util.List;

/**
 * 题名 :　合并区间
 * 题目 : 给出一个区间的集合，请合并所有重叠的区间。
 *
 * 思路 : 根据区间起始位置排序,判断末尾位置与起始位置大小
 * @author clay
 * @date 19-2-28 08:39
 */
public class Leetcode56 {

     public class Interval {
         int start;
         int end;
         Interval() { start = 0; end = 0; }
         Interval(int s, int e) { start = s; end = e; }
     }

    class Solution {
        public List<Interval> merge(List<Interval> intervals) throws NoSuchMethodException {
            if (intervals.size() <= 0){
                return new LinkedList<>();
            }
            intervals.sort((i1, i2)->i1.start > i2.start ? 1 : i1.start == i2.start ? 0 : -1);
            List<Interval> result = new LinkedList<>();
            Interval interval = intervals.get(0);
            int start = interval.start, end = interval.end;
            for (Interval i : intervals){
                if (i.start <= end){
                    end = Math.max(end, i.end);
                }else {
                    Interval cur = new Interval(start, end);
                    result.add(cur);
                    start = i.start;
                    end = i.end;
                }
            }
            result.add(new Interval(start, end));
            return result;
        }
    }
}
