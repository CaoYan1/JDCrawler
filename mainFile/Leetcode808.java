package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 分汤
 * 题目 : 有 A 和 B 两种类型的汤。一开始每种类型的汤有 N 毫升。有四种分配操作：
 *     提供 100ml 的汤A 和 0ml 的汤B。
 *     提供 75ml 的汤A 和 25ml 的汤B。
 *     提供 50ml 的汤A 和 50ml 的汤B。
 *     提供 25ml 的汤A 和 75ml 的汤B。
 * 当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为0.25的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。
 * 注意不存在先分配100 ml汤B的操作。
 * 需要返回的值： 汤A先分配完的概率 + 汤A和汤B同时分配完的概率 / 2。
 *
 * 思路 : 递归思想,对于f(a,b)为a ml A 和 b ml B的答案,则有f(a,b) =
 * (f(a-100,b) + f(a-75,b-25) + f(a-50,b-50) + f(a-25,b-75))/4;
 * 因为四种操作的概率是相等的.因为操作都是25的倍数,所以可以把N除以25,然后所有操作都除以25,
 * 然后向上取整.因为汤剩余不够的时候也可以当做一次操作,这样可以减少备忘录的容量
 * 递归的时候使用数组记录结果,避免重复搜索.
 * 也可以动态规划自底向上.
 *
 *
 *
 * @author clay
 * @date 18-12-22 20:23
 */
public class Leetcode808 {

    class Solution {

        double[][] dp = new double[225][225];

        public double soupServings(int N) {
            int n = (int)Math.ceil(N/25.0);
            return N >= 5600 ? 1 : r(n,n);
        }

        public double r(int a, int b){
            if(a <= 0 && b <= 0){
                return 0.5;
            }else if(b <= 0){
                return 0;
            }else if(a <= 0){
                return 1;
            }else if(dp[a][b] == 0){
                dp[a][b] = 0.25*(r(a-4,b) + r(a-3,b-1)+ r(a-2,b-2) + r(a-1,b-3));
            }
            return dp[a][b];
        }
    }

}
