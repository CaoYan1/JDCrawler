package com.cy.algorithm.leetcode.medium;

import java.util.LinkedList;
import java.util.List;

/**
 * 题名 : 找到最终的安全状态
 * 题目 : 在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。
 * 现在, 如果我们最后能走到终点，那么我们的起始节点是最终安全的。 更具体地说, 存在一个自然数 K,  无论选择从哪里开始行走, 我们走了不到 K 步后必能停止在一个终点。
 * 哪些节点最终是安全的？ 结果返回一个有序的数组。
 * 该有向图有 N 个节点，标签为 0, 1, ..., N-1, 其中 N 是 graph 的节点数.  图以以下的形式给出: graph[i] 是节点 j 的一个列表，满足 (i, j) 是图的一条有向边。
 *
 * 思路 : 备忘录 + 深搜
 * @author clay
 * @date 19-1-8 16:50
 */
public class Leetcode802 {

    class Solution {

        public int[] dp;
        public boolean[] visited;

        public boolean dfs(int[][] graph, int a){
            if(dp[a] != 0){
                return dp[a] == 1;
            }
            if(graph[a] == null || graph[a].length == 0){
                dp[a] = 1;
                return true;
            }
            visited[a] = true;
            for(int i = 0; i < graph[a].length; i++){
                if(visited[graph[a][i]] || !dfs(graph,graph[a][i])){
                    dp[graph[a][i]] = 2;
                    return false;
                }
            }
            visited[a] = false;
            dp[a] = 1;
            return true;
        }

        public List<Integer> eventualSafeNodes(int[][] graph) {
            dp = new int[graph.length];
            List<Integer> result = new LinkedList<>();
            for(int i = 0; i < graph.length; i++){
                visited = new boolean[graph.length];
                visited[i] = true;
                if(dfs(graph,i)){
                    result.add(i);
                }
                visited[i] = false;
            }
            return result;
        }
    }
}
