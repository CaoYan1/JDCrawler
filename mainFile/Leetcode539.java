package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;
import java.util.List;

/**
 * 题名 : 最小时间差
 * 题目 : 给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。
 *
 * 思路 : 全部以分钟数表示排个序比较相邻的和第一个与最后一个的时间差
 *
 * @author clay
 * @date 19-3-16 09:11
 */
public class Leetcode539 {

    class Solution {
        public final int FULL_MIN = 24 * 60;

        class Time implements Comparable<Time>{

            private int min;
            public Time(String time) {
                String[] minAndHour = time.split(":");
                min = Integer.parseInt(minAndHour[0]) * 60 + Integer.parseInt(minAndHour[1]);
            }

            @Override
            public int compareTo(Time o) {
                return Integer.compare(min, o.min);
            }
        }

        public int findMinDifference(List<String> timePoints) {
            Time[] times = new Time[timePoints.size()];
            for (int i = 0; i < times.length; i++){
                times[i] = new Time(timePoints.get(i));
            }
            Arrays.sort(times);
            int min = Integer.MAX_VALUE;
            for (int i = 1; i < times.length; i++){
                int interval = times[i].min - times[i - 1].min;
                if (interval < min){
                    min = interval;
                }
            }
            int interval = FULL_MIN - times[times.length - 1].min + times[0].min;
            if (interval < min){
                min = interval;
            }
            return min;
        }
    }
}
