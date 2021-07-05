package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 消除游戏
 * 题目 : 给定一个从1 到 n 排序的整数列表。
 * 首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
 * 第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
 * 我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
 * 返回长度为 n 的列表中，最后剩下的数字。
 *
 * 思路 : 不断构造下一次的递归序列，将递归分为两部分，ｆ和ｂ，ｆ是从左向右，ｂ为从右向左．
 * ｆ(n)= 2 * b(n/2),筛选掉奇数之后把剩余的数字除以２就是一个ｎ／２的列表了，最后结果在乘２就行
 * ｂ(n) = 2 * f(n/2) ｎ为奇数的时候筛选掉的全是奇数，跟上面情况差不多，除以２构造下一层递归
 * ｂ(n) = f(n/2) * 2 - 1 ｎ为偶数的时候筛选掉的全是偶数，把剩下的奇数加１除以２之后就构造了一个ｎ／２的列表
 * @author clay
 * @date 19-1-21 17:42
 */
public class Leetcode390 {
    class Solution {

        public int lastRemaining(int n) {
            return n == 1 ? 1 : 2 * (n / 2 + 1 - lastRemaining(n / 2));
        }

        public int f(int n){
            return n == 1 ? 1 : 2 * b(n/2);
        }

        public int b(int n){
            if(n == 1){
                return 1;
            }
            if(n % 2 == 0){
                return f(n/2) + 1;
            }else {
                return 2 * f(n/2);
            }
        }
        public int lastRemaining1(int n) {
            return f(n);
        }
    }
}
