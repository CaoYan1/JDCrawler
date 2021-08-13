package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 * 题名 : 重构字符串
 * 题名 : 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
 * 若可行，输出任意可行的结果。若不可行，返回空字符串。
 *
 * 思路 : 先计算出每个字母的个数,然后每两个不同的字母交替,最后多余的重复字母往中间可以插入的位置插入,
 * 如果不存在可以插入的位置,就返回""
 *
 * @author clay
 * @date 19-1-23 18:23
 */
public class Leetcode767 {
    public static void main(String[] args) {
        Solution s = new Leetcode767().new Solution();
        System.out.println(s.reorganizeString("kkkkzrkatkwpkkkktrq"));
    }
    class Solution {
        public String reorganizeString(String S) {
            int []frequency = new int[26];
            for(int i = 0; i < S.length(); i++){
                frequency[S.charAt(i) - 97]++;
            }
            Queue<Character> queue = new LinkedList<>();
            int m = 0, l = 1;
            int index = 1;
            while(true){
                while (frequency[m] != 0 && frequency[l] != 0){
                    queue.offer((char)(m + 97));
                    queue.offer((char)(l + 97));
                    frequency[m]--;
                    frequency[l]--;
                }
                if(frequency[m] == 0 && index == 25){
                    break;
                }else if(frequency[m] == 0){
                    m = ++index;
                }
                if(frequency[l] == 0 && index == 25){
                    break;
                }else if(frequency[l] == 0){
                    l = ++index;
                }
            }
            if(frequency[l] != 0){
                m = l;
            }
            StringBuilder result = new StringBuilder();
            char last = 0;
            while(!queue.isEmpty()){
                char c = queue.poll();
                if(last != m+97 && c != m+97 && frequency[m] > 0){
                    result.append((char)(m+97));
                    frequency[m]--;
                }
                last = c;
                result.append(c);
            }
            if(last != m + 97 && frequency[m] > 0){
                result.append((char)(m + 97));
                frequency[m]--;
            }
            if(frequency[m] > 0){
                return "";
            }
            return result.toString();
        }
    }
}
