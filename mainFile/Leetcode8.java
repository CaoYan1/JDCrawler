package com.cy.algorithm.leetcode.medium;

import java.math.BigInteger;

/**
 * 题名 : 字符串转换整数(atoi)
 * 题目 : 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
 * 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
 * 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
 * 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
 * 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
 *
 * 在任何情况下，若函数不能进行有效的转换时，请返回 0。
 * 思路 : 按照题意慢慢往后遍历,用biginteger保存有效的位
 *
 * @author clay
 * @date 19-1-12 15:33
 */
public class Leetcode8 {

    class Solution {
        public int myAtoi(String str) {
            if(str == null || str.length() <= 0){
                return 0;
            }
            char[] chars = str.toCharArray();
            int i = 0;
            while(i < chars.length && chars[i] == ' '){
                ++i;
            }
            int j = i;
            if(j >= chars.length){
                return 0;
            }
            if(j < chars.length && chars[j] == '-' || chars[j] == '+'){
                j++;
            }else if(chars[j] < '0' || chars[j] > '9'){
                return 0;
            }
            for(; j < chars.length && chars[j] >= '0' && chars[j] <= '9'; j++){
                   if(j - i > 11){
                       if(chars[i] == '-'){
                           return Integer.MIN_VALUE;
                       }else {
                           return Integer.MAX_VALUE;
                       }
                   }
            }
            if(i == j || (i == j - 1 && (chars[i] == '-' || chars[i] == '+'))){
                return 0;
            }
            BigInteger result =  new BigInteger(new String(chars,i,j - i));
            if(result.compareTo(new BigInteger(""+Integer.MAX_VALUE)) > 0){
                return Integer.MAX_VALUE;
            }
            if(result.compareTo(new BigInteger(""+Integer.MIN_VALUE)) < 0){
                return Integer.MIN_VALUE;
            }
            return result.intValue();
        }
    }
}
