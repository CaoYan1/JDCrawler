package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 回文子串
 * 题目 : 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
 * 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
 *
 * 思路 : 马拉车算法,求出每个字符为中心的半径,半径长度以该字符为中心的回文串个数
 * 马拉车算法详见: https://blog.csdn.net/Form_/article/details/79766986
 * @author clay
 * @date 19-2-15 15:47
 */
public class Leetcode647 {

    public static void main(String[] args) {
        Solution s = new Leetcode647().new Solution();
        System.out.println(s.countSubstrings("xvxvg"));
    }

    class Solution {
        public int countSubstrings(String s) {
            char[] cs = new char[s.length()*2+1];
            for (int i = 0; i < s.length(); i++){
                cs[2 * i] = '#';
                cs[2 * i + 1] = s.charAt(i);
            }
            cs[cs.length - 1] = '#';
            int count = 0;
            int[] dp = new int[cs.length];
            int max = -1, c = -1;
            for (int i = 0; i < cs.length; i++){
                int len = 1;
                if (max > i){
                    len = Math.min(dp[c*2 - i], max - i + 1);
                    if (max - i + 1 <= len){
                        for (int j = max - i + 1; i + j < cs.length && i - j >= 0 && cs[i+j] == cs[i-j]; j++){
                            len++;
                        }
                    }
                }else {
                    for (int j = 1; i + j < cs.length && i - j >= 0 && cs[i+j] == cs[i-j]; j++){
                        len++;
                    }
                }
                dp[i] = len;
                if (i + len - 1 > max){
                    c = i;
                    max = i + len - 1;
                }
                if (cs[i] == '#'){
                    count += len / 2;
                }else {
                    count += (len + 1) / 2;
                }
            }
            return count;
        }
    }
}
