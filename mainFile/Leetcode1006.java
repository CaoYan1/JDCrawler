package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 笨阶乘
 * 题目 : 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
 * 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
 * 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
 * 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
 * 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
 *
 * 思路 : 不断往后递推
 * @author clay
 * @date 19-3-10 10:48
 */
public class Leetcode1006 {
    class Solution {
        public int clumsy(int N) {
            int sum = 0;
            while (true){
                if (N == 0){
                    return sum;
                }
                if (N == 1){
                    if (sum == 0){
                        return 1;
                    }
                    return sum - 1;
                }
                if (N == 2){
                    if (sum == 0){
                        return 2;
                    }
                    return sum - 2;
                }
                if (N == 3){
                    if (sum == 0){
                        return 6;
                    }
                    return sum - 6;
                }
                if (sum == 0){
                    sum = N * (N - 1) / (N - 2) + (N - 3);
                }else {
                    sum = sum - N * (N - 1) / (N - 2) + (N - 3);
                }
                N -= 4;
            }
        }
    }
}
