package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * 题名 : 单词的压缩编码
 * 题目 : 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
 * 例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
 * 对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
 * 那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
 *
 * 思路 : 对每个单词倒着往前建一棵树,因为一个单词的末尾包含另一个单词则那个单词不需要额外空间
 * 最后深度优先遍历这棵树,结果为所有叶子的高度+1(因为'#'也占一个位置)的和
 * @author clay
 * @date 18-12-30 16:40
 */
public class Leetcode820 {

    public static void main(String[] args){
        Solution s = new Leetcode820().new Solution();
        System.out.println(s.minimumLengthEncoding(new String[]{"time", "me", "bell"}));
    }


    class Solution {

        public void insert(HashMap<Character, HashMap> root, String word){
            char []chars = word.toCharArray();
            HashMap<Character, HashMap> map = new HashMap<>();
            for(int i = chars.length - 1; i >= 0; i--){
                HashMap<Character, HashMap> next = root.putIfAbsent(chars[i],map);
                if(next == null){
                    next = map;
                    map = new HashMap<>();
                }
                root = next;
            }
        }

        public int count(HashMap<Character, HashMap> root, int h){
            int sum = 0;
            if(root.isEmpty()){
                return h + 1;
            }
            for(Map.Entry<Character, HashMap> entry : root.entrySet()){
                sum = sum + count(entry.getValue(), h + 1);
            }
            return sum;
        }

        public int minimumLengthEncoding(String[] words) {
            HashMap<Character, HashMap> root = new HashMap<>();
            for(String word : words){
                insert(root, word);
            }
            return count(root, 0);
        }
    }
}
