package com.cy.algorithm.leetcode.medium;

import java.util.HashMap;
import java.util.Map;

/**
 * 题名 : 我能赢吗
 * 题目 : 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。
 * 如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
 * 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
 * 给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
 * 你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
 *
 * 思路 : 递归搜索,当第一个人选的时候,如果有一种选择方法能赢就能赢,如果第二个人选,只有他怎么选都会输的情况下第一个人才能赢,
 * 用一个整形存储
 *
 * @author clay
 * @date 19-2-9 19:44
 */
public class Leetcode464 {

    public static void main(String[] args) {
        Solution s = new Leetcode464().new Solution();
        System.out.println(s.canIWin(4,6));
    }

    class Solution {

        public Map<Integer, Boolean> map = new HashMap<>();
        public int maxChoosableInteger;
        public boolean dfs(int desiredTotal, int visited){
            if (desiredTotal <= 0){
                return false;
            }
            Boolean result;
            if((result = map.get(visited)) != null) {
                return result;
            }
            for(int i = 1; i <= maxChoosableInteger; i++){
                int mask = 1 << i;
                if((visited & mask) == 0){
                    visited |= mask;
                    boolean win = dfs(desiredTotal - i, visited);
                    if(desiredTotal - i >= 0){
                        map.put(visited, win);
                    }
                    visited ^= mask;
                    if(!win){
                        return true;
                    }
                }
            }
            return false;
        }

        public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
            if(desiredTotal <= maxChoosableInteger){
                return true;
            }
            if(desiredTotal > (maxChoosableInteger + 1) * maxChoosableInteger / 2){
                return false;
            }
            this.maxChoosableInteger = maxChoosableInteger;
            return dfs(desiredTotal, 0);
        }
    }
}
