package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 加油站
 * 题目 : 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
 * 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
 * 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
 *
 * 思路 : 贪心算法,从0开始扫描一遍数组,起点为0,如果油在i处不够了,起点设置为i+1.总油量大于总耗油答案就是起点,否则-1
 * @author clay
 * @date 19-3-4 09:59
 */
public class Leetcode134 {
    class Solution {
        public int canCompleteCircuit(int[] gas, int[] cost) {
            if (gas.length <= 0){
                return -1;
            }
            int start = -1;
            int rest = 0;
            int cur = 0;
            while (cur != start){
                if (cur == 0 && start== -1){
                    return 0;
                }
                rest += gas[cur] - cost[cur];
                if (rest < 0){
                    if (cur < start){
                        return -1;
                    }
                    start = cur;
                    rest = 0;
                }
                cur++;
                cur %= gas.length;
            }
            return start;
        }
    }
}
