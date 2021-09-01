package com.cy.algorithm.leetcode.medium;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

/**
 * 题名 : 情感丰富的文字
 * 题目 : 有时候人们会用额外的字母来表示额外的情感，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将连续的相同的字母分组，并且相邻组的字母都不相同。我们将一个拥有三个或以上字母的组定义为扩张状态（extended），如第一个例子中的 "e" 和" o" 以及第二个例子中的 "i"。 此外，"abbcccaaaa" 将有分组 "a" , "bb" , "ccc" , "dddd"；其中 "ccc" 和 "aaaa" 处于扩张状态。
 * 对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。我们允许选择一个字母组（如包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。注意，我们不能将一个只包含一个字母的字母组，如 "h"，扩张到一个包含两个字母的组，如 "hh"；所有的扩张必须使该字母组变成扩张状态（至少包含三个字母）。
 * 输入一组单词，输出其中可扩张的单词数量。
 *
 * 思路 : 记录每个字符串中连续相同的字母以及出现的次数,然后比较
 * @author clay
 * @date 19-1-18 17:55
 */
public class Leetcode809 {

    public static void main(String[] args){
        Solution s = new Leetcode809().new Solution();
        System.out.println(s.expressiveWords("aaa",new String[]{"aaaa"}));
    }

    class Solution {
        public void getPattern(String S, List<Integer> pattern){
            char last = S.charAt(0);
            int count = 1;
            for(int i = 1; i < S.length(); i++){
                if(S.charAt(i) == last){
                    count++;
                    continue;
                }else {
                    pattern.add((int)last);
                    pattern.add(count);
                    count = 1;
                    last = S.charAt(i);
                }
            }
            pattern.add((int)last);
            pattern.add(count);
        }
        public int expressiveWords(String S, String[] words) {
            List<Integer> pattern = new LinkedList<>();
            getPattern(S,pattern);
            Iterator<Integer> i1 = pattern.iterator();
            int count = 0;
            for(String word : words){
                List<Integer> wordPattern = new LinkedList<>();
                getPattern(word,wordPattern);
                if(pattern.size() != wordPattern.size()) continue;
                Iterator<Integer> i2 = wordPattern.iterator();
                boolean result = true;
                while(i1.hasNext()){
                    if(!i1.next().equals(i2.next())){
                        result = false;
                        break;
                    }
                    int count1 = i1.next();
                    int count2 = i2.next();
                    if(count1 != count2 && (count1 < 3 || count2 > count1)){
                        result = false;
                        break;
                    }
                }
                if(result){
                    count++;
                }
                i1 = pattern.iterator();
            }
            return count;
        }
    }
}
