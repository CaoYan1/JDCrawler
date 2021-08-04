package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 只有两个键的键盘
 * 题目 : 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
 * 1.Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
 * 2.Paste (粘贴) : 你可以粘贴你上一次复制的字符。
 * 给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
 *
 * 思路 : 对于一个数n,最少的操作次数就等于他的最大公因数的操作次数 + (与最大公因数的商 - 1) + 一次copy
 * 执行时间 :　6ms
 * @author clay
 * @date 18-11-12 14:50
 */
public class Leetcode650 {

    public static int maxFactor(int n){
        for(int i = n-1; i > 0; i--){
            if(n % i == 0){
                return i;
            }
        }
        return 1;
    }

    public static int minSteps(int n) {
        if(n == 1){
            return 0;
        }
        int mf = maxFactor(n);
        return minSteps(mf) + n/mf;
    }

    public static void main(String []args){
        System.out.println(minSteps(1000));
    }
}
