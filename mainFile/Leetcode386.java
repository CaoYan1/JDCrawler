package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * 题名 : 字典序排数
 * 题目 : 给定一个整数 n, 返回从 1 到 n 的字典顺序。
 * 例如，
 * 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
 * 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
 *
 * 思路 : 直接转换成字符串排序, 也可以深度优先搜寻插入,后者效率高点.
 *
 * @author clay
 * @date 19-1-6 20:08
 */
public class Leetcode386 {
    class Solution {
        //直接排序方法
        public List<Integer> lexicalOrder(int n) {
            LinkedList<Integer> list = new LinkedList<>();
            for(int i = 1; i <= n; i++){
                list.add(i);
            }
            list.sort((i1,i2)->{
                String s1 = i1.toString(), s2 = i2.toString();
                return s1.compareTo(s2);
            });
            return list;
        }

        public void dfs(int n, int cur, List<Integer> list){
            if (cur > n){
                return;
            }
            list.add(cur);
            for(int i = 0; i < 9; i++){
                int num = cur * 10 + i;
                if(num > n){
                    break;
                }
                dfs(n, num, list);
            }
        }
        //dfs方法
        public List<Integer> lexicalOrder2(int n) {
            List<Integer> result = new LinkedList<>();
            for(int i = 1; i < 9; i++){
                dfs(n,i,result);
            }

            return result;
        }
    }
}
