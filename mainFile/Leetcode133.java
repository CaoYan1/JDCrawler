package com.cy.algorithm.leetcode.medium;

import java.util.*;

/**
 * description
 *
 * @author clay
 * @date 18-11-17 17:09
 */
public class Leetcode133 {

    class UndirectedGraphNode {
      int label;
      List<UndirectedGraphNode> neighbors;
      UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
    }

    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node == null){
            return null;
        }
        return null;
    }
}
