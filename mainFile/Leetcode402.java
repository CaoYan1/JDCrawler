package com.cy.algorithm.leetcode.medium;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Stack;

/**
 * 题名 : 移掉k位数字
 * 题目 : 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
 *
 * 思路 : 用栈,每次入栈将栈顶所有比当前数字的出栈,直到出栈了k个
 *
 * @author clay
 * @date 19-3-9 14:20
 */
public class Leetcode402 {

    class Solution {

        public String removeKdigits(String num, int k) {
            LinkedList<Character> stack = new LinkedList<>();
            char[] numArr = num.toCharArray();
            for (int i = 0; i < numArr.length; i++){
               if (k == 0){
                   stack.push(numArr[i]);
                   continue;
               }

               while (!stack.isEmpty() && numArr[i] < stack.peek() && k > 0){
                   stack.pop();
                   k--;
               }
               if (stack.isEmpty() && numArr[i] == '0'){
                    continue;
               }else {
                   stack.push(numArr[i]);
               }
            }
            while (!stack.isEmpty() && k > 0){
                stack.pop();
                k--;
            }
            if (stack.isEmpty()){
                return "0";
            }
            StringBuilder result = new StringBuilder();
            Iterator<Character> it = stack.descendingIterator();
            while (it.hasNext()){
                result.append(it.next());
            }
            return result.toString();
        }
    }
}
