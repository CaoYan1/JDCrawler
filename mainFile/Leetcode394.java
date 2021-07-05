package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * 题名 ： 字符串解码
 * 题目 : 给定一个经过编码的字符串，返回它解码后的字符串。
 * 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
 * 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
 * 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
 *
 * 思路 : 用栈存储,遇到']'就出栈里面的字符串直到'[',然后出栈数字,计算重复的次数,再将里面的字符串入栈
 * @author clay
 * @date 19-1-15 13:45
 */
public class Leetcode394 {

    public static void main(String[] args){
        Solution s = new Leetcode394().new Solution();
        System.out.println(s.decodeString("2[abc]3[cd]ef"));
    }
    class Solution {
        public String decodeString(String s) {
            char[] cs = s.toCharArray();
            LinkedList<String> stack = new LinkedList<>();
            StringBuilder result = new StringBuilder();
            int count3 = 0;
            for(char c : cs){
                if(c == ']'){
                    count3--;
                    String temp = "";
                    while (!stack.peek().equals("[")){
                        temp = stack.pop() + temp;
                    }
                    stack.pop();
                    int count = 0;
                    int count1 = 1;
                    while (!stack.isEmpty() && stack.peek().length() == 1 && stack.peek().charAt(0) >= '0'
                            && stack.peek().charAt(0) <= '9'){
                        count += (stack.pop().charAt(0) - 48)*count1;
                        count1 *= 10;
                    }
                    if(stack.isEmpty()){
                        for(int i = 0; i < count; i++){
                            result.append(temp);
                        }
                    }else {
                        StringBuilder sb = new StringBuilder();
                        for(int i = 0; i < count; i++){
                            sb.append(temp);
                        }
                        stack.push(sb.toString());
                    }
                }else {
                    if(c == '['){
                        count3++;
                    }else if(count3 == 0 && (c < '0' || c > '9')){
                        result.append(c);
                        continue;
                    }
                    stack.push("" + c);
                }
            }
            return result.toString();
        }
    }

}
