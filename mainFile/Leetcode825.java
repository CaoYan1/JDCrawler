package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 适龄的朋友
 * 题目 : 人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，ages[i] 表示第 i 个人的年龄。
 * 当满足以下条件时，A 不能给 B（A、B不为同一人）发送好友请求：
 *     age[B] <= 0.5 * age[A] + 7
 *     age[B] > age[A]
 *     age[B] > 100 && age[A] < 100
 * 否则，A 可以给 B 发送好友请求。
 * 注意如果 A 向 B 发出了请求，不等于 B 接受了 A 的请求。而且，人们不会给自己发送好友请求。
 * 求总共会发出多少份好友请求?
 *
 * 思路 : 对于每个age,统计小于这个age的人数,然后遍历每个age,计算age符合题意的区间,然后乘以人数
 * 要减去自己.根据条件可以计算15岁以下无法同时满足条件1,2
 *
 * @author clay
 * @date 19-1-1 13:12
 */
public class Leetcode825 {

    class Solution {
        public int numFriendRequests(int[] ages) {
            int result = 0;
            int[] nums = new int[121];
            int[] sums = new int[121];
            for(int age : ages){
                nums[age]++;
            }
            for(int i = 1; i < sums.length; i++){
                sums[i] = nums[i] + sums[i-1];
            }
            for(int i = 15; i < 121; i++){
                result += nums[i] * (sums[i] - sums[i/2+7] - 1);
            }
            return result;
        }
    }
}
