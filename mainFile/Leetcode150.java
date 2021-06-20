package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * 题名 : 逆波兰表达式求值
 * 题目 : 根据逆波兰表示法，求表达式的值。
 * 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
 * 说明：
 *     整数除法只保留整数部分。
 *     给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
 *
 * 思路 : 数字入栈,操作符出栈
 * @author clay
 * @date 19-2-1 19:12
 */
public class Leetcode150 {

    public static void main(String[] args) {
        System.out.println(0/1);
    }

    class Solution {
        public int evalRPN(String[] tokens) {
            LinkedList<String> stack = new LinkedList<>();
            for (int i = 0; i < tokens.length; i++){
                if(tokens[i].equals("+")){
                    stack.push("" + (Integer.parseInt(stack.pop()) + Integer.parseInt(stack.pop())));
                }else if(tokens[i].equals("-")){
                    int a = Integer.parseInt(stack.pop());
                    int b = Integer.parseInt(stack.pop());
                    stack.push("" + (b - a));
                }else if(tokens[i].equals("*")){
                    stack.push("" + (Integer.parseInt(stack.pop()) * Integer.parseInt(stack.pop())));
                }else if(tokens[i].equals("/")){
                    int a = Integer.parseInt(stack.pop());
                    int b = Integer.parseInt(stack.pop());
                    stack.push("" + (b / a));
                }else {
                    stack.push(tokens[i]);
                }
            }
            return Integer.parseInt(stack.pop());
        }
    }
}
