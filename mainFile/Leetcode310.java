package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * 题名 : 最小高度树
 * 题目 : 对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。
 *
 * 思路 : 每次将叶子结点删掉,直到最后剩下的几个结点就是最小的根结点
 * @author clay
 * @date 19-3-8 10:14
 */
public class Leetcode310 {
    public static void main(String[] args) {
        Solution s = new Leetcode310().new Solution();
        System.out.println(s.findMinHeightTrees(6 ,new int[][]{{0,1},{0,2},{0,3},{3,4},{4,5}}));
    }
    class Solution {
        public List<Integer> findMinHeightTrees(int n, int[][] edges) {
            if (n == 1){
                List<Integer> l = new ArrayList<>();
                l.add(0);
                return l;
            }
            List<Integer>[] tree = new List[n];
            int count = 0;
            int[] edgeNum = new int[n];
            for (int i = 0; i < tree.length; i++){
                tree[i] = new LinkedList<>();
            }
            Set<Integer> leaves = new HashSet<>();
            Set<Integer> lastLeaves = new HashSet<>();
            for (int[] edge : edges){
                tree[edge[0]].add(edge[1]);
                tree[edge[1]].add(edge[0]);
                edgeNum[edge[0]]++;
                edgeNum[edge[1]]++;
                if (edgeNum[edge[0]] == 1){
                    leaves.add(edge[0]);
                }else {
                    leaves.remove(edge[0]);
                }
                if (edgeNum[edge[1]] == 1){
                    leaves.add(edge[1]);
                }else {
                    leaves.remove(edge[1]);
                }
            }
            while (!leaves.isEmpty()){
                count += leaves.size();
                if (count == n){
                    return new ArrayList<>(leaves);
                }
                for (int i : leaves){
                    for (int j : tree[i]){
                        edgeNum[i]--;
                        if (--edgeNum[j] == 1){
                            lastLeaves.add(j);
                        }
                    }
                }
                Set<Integer> temp = lastLeaves;
                lastLeaves = leaves;
                leaves = temp;
                lastLeaves.clear();
            }
            return new ArrayList<>();

        }
    }
}
