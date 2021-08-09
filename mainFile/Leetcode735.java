package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;

/**
 * 题名 : 行星碰撞
 * 题目 : 给定一个整数数组 asteroids，表示在同一行的行星。
 * 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
 * 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
 *
 * 思路 : 放入栈中,比较栈顶,会碰撞出栈.
 *
 * @author clay
 * @date 19-2-14 15:45
 */
public class Leetcode735 {

    public static void main(String[] args) {
        Solution s = new Leetcode735().new Solution();
        System.out.println(s.asteroidCollision(new int[]{1,-2,-2,-2}));
    }

    class Solution {
        public int[] asteroidCollision(int[] asteroids) {
            LinkedList<Integer> stack = new LinkedList<>();
            for (int i = 0; i < asteroids.length; i++){
                if (asteroids[i] > 0 || stack.isEmpty()){
                    stack.push(asteroids[i]);
                    continue;
                }
                while (!stack.isEmpty()){
                    int top = stack.peek();
                    if (top > 0){
                        if (top > -asteroids[i]){
                            break;
                        }else if (top == -asteroids[i]){
                            stack.pop();
                            break;
                        }else {
                            stack.pop();
                            if (stack.isEmpty()){
                                stack.push(asteroids[i]);
                                break;
                            }
                            continue;
                        }

                    }else {
                        stack.push(asteroids[i]);
                        break;
                    }
                }
            }
            int[] ret = new int[stack.size()];
            int i = 0;
            Iterator<Integer> it = stack.descendingIterator();
            while (it.hasNext()){
                ret[i++] = it.next();
            }
            return ret;
        }
    }
}
