package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * 题名 : 单词拆分
 * 题目 : 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
 * 说明：
 *   1.拆分时可以重复使用字典中的单词。
 *   2.你可以假设字典中没有重复的单词。
 *
 * 思路 : 动态规划,dp[i]代表s[0~i]能否被拆分,则dp[i]=dp[n]&&字典里有s[i+1~n],因为单词比较短,倒着遍历效率高
 * 执行时间 : 6ms
 * @author clay
 * @date 18-11-21 20:26
 */
public class Leetcode139 {

    public boolean wordBreak(String s, List<String> wordDict) {
        boolean []dp = new boolean[s.length()];
        Set<String> set = new HashSet<>(wordDict);
        for(int i = 0; i < s.length(); i++){
            for(int j = i; j >= 0; j--){
                if(((j-1) < 0 || dp[j-1]) && set.contains(s.substring(j,i+1))){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()-1];
    }

    public static void main(String ...args){
        System.out.println(new Leetcode139().wordBreak("applepenapple",
                Arrays.asList("apple","pen")));
    }
}
