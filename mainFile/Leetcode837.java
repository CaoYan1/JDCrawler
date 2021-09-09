package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 题名 : 新21点
 * 题目 : 爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
 * 爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。
 * 当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？
 *
 * 思路 : 直接dp数组倒推或者备忘录递归都会超时,
 * 可以用一个队列存储后W个,再用一个sum记录队列的和,每次出队入队更新sum,每次将sum/W入队
 * @author clay
 * @date 19-1-3 21:07
 */
public class Leetcode837 {

    public static void main(String[] args){
        Solution s = new Leetcode837().new Solution();
        System.out.println(s.new21Game(1,0,1));
    }

    class Solution {
        public double new21Game(int N, int K, int W) {
            LinkedList<Double> queue = new LinkedList<>();
            double sum = 0;
            for(int i = K + W - 1; i >= K; i--){
                if(i <= N){
                    queue.offer(1.0);
                    sum += 1.0;
                }else {
                    queue.offer(0.0);
                }
            }
            for(int i = K - 1; i >= 0; i--){
                double cur = sum/W;
                if(i == 0){
                    return cur;
                }
                double tail = queue.poll();
                sum -= tail;
                sum += cur;
                queue.offer(cur);
            }
            return K <= N ? 1 : 0;
        }
    }
}
