package com.cy.algorithm.leetcode.medium;

import java.util.HashSet;
import java.util.Set;

/**
 * 题名 : 链表组件
 * 题目 : 给定一个链表（链表结点包含一个整型值）的头结点 head。
 * 同时给定列表 G，该列表是上述链表中整型值的一个子集。
 * 返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。
 *
 * 思路 : 用set判断存不存在,然后扫描一遍链表找到连续存在的个数
 *
 * @author clay
 * @date 19-2-1 18:39
 */
public class Leetcode817 {

     public class ListNode {
          int val;
          ListNode next;
          ListNode(int x) { val = x; }
     }

    class Solution {
        public int numComponents(ListNode head, int[] G) {
            Set<Integer> set = new HashSet<>();
            for(int i : G){
                set.add(i);
            }
            int count = 0;
            boolean flag = false;
            while(head != null){
                if(set.contains(head.val)){
                    if(!flag){
                        count++;
                    }
                    flag = true;
                }else {
                    flag = false;
                }
                head = head.next;
            }
            return count;
        }
    }
}
