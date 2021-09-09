package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 题名 : 钥匙和房间
 * 题目 : 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
 * 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
 * 最初，除 0 号房间外的其余所有房间都被锁住。
 * 你可以自由地在房间之间来回走动。
 * 如果能进入每个房间返回 true，否则返回 false。
 *
 * 思路 : 广度优先搜索,记录已经搜索过的不再搜索,记录打开的房间数,最终判断房间数等不等于总房间数
 * @author clay
 * @date 19-1-8 17:47
 */
public class Leetcode841 {

    class Solution {
        public boolean canVisitAllRooms(List<List<Integer>> rooms) {
            boolean[] visited = new boolean[rooms.size()];
            visited[0] = true;
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(0);
            visited[0] = true;
            int count = 1;
            while (!queue.isEmpty()){
                int cur = queue.poll();
                for(int i : rooms.get(cur)){
                    if(!visited[i]){
                        queue.offer(i);
                        visited[i] = true;
                        count++;
                    }
                }
            }
            return count == rooms.size();
        }
    }
}
