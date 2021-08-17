package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 在LR字符串中交换相邻字符
 * 题目 :在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
 * 一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
 * 现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时，
 * 返回True。
 *
 * 思路 : R只能向右移动,L只能向左移动,从左到右遍历一次,向右寻找跟start匹配的R和end匹配的L
 * 执行时间 : 6ms
 * @author clay
 * @date 18-11-14 15:52
 */
public class Leetcode777 {

    public boolean canTransform(String start, String end) {
        char []startArr = start.toCharArray();
        char []endArr = end.toCharArray();
        int cur = 0, n = start.length();
        for(int i = 0; i < n; i++){
            if(startArr[i] == endArr[i]){
                continue;
            }else if(startArr[i] == 'L' || endArr[i] == 'R'){
                return false;
            }else if(startArr[i] == 'R'){
                int j = i + 1;
                for(; j < n; j++){
                    if(startArr[j] == 'L' || endArr[j] == 'L'){
                        return false;
                    }
                    if(endArr[j] == 'R'){
                        endArr[j] = 'X';
                        startArr[i] = 'X';
                        break;
                    }
                }
                if(j > n-1){
                    return false;
                }
            }else if(endArr[i] == 'L'){
                int j = i + 1;
                for(; j < n; j++){
                    if(endArr[j] == 'R' || startArr[j] == 'R'){
                        return false;
                    }
                    if(startArr[j] == 'L'){
                        endArr[i] = 'X';
                        startArr[j] = 'X';
                        break;
                    }
                }
                if(j > n-1){
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String ...args){
        Leetcode777 l = new Leetcode777();
        System.out.println(l.canTransform("XXRXXLXXXX",
                "XXXXRXXLXX"));
    }
}
