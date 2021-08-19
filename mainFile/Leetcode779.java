package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 第k个语法符号
 * 题目 : 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
 * 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
 *
 * 思路 : 递归找上一层的
 * 执行时间 : 3ms
 * @author clay
 * @date 18-11-14 17:00
 */
public class Leetcode779 {

    private static final int [][]arr = new int[][]{{1,0},{0,1}};

    public int kthGrammar(int N, int K) {
        if(N == 1){
            return 0;
        }
        int lastK = (K-1)/2+1;
        int mod = K%2;
        int lastNum = kthGrammar(N-1,lastK);
        return arr[lastNum][mod];
    }

    public static void main(String ...args){
        System.out.println(new Leetcode779().kthGrammar(4,4));

    }
}
