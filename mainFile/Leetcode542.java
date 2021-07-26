package com.cy.algorithm.leetcode.medium;

/**
 * description
 *
 * @author clay
 * @date 19-2-26 12:20
 */
public class Leetcode542 {

    public static void main(String[] args) {
        Solution s = new Leetcode542().new Solution();
        System.out.println(s.updateMatrix(new int[][]{{0,0,0},{0,1,0},{1,1,1}}));
    }

    class Solution {

        private boolean[][] visited;

        private int[][] direction = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};

        public void update(int[][] matrix, int x, int y){
            for (int[] dir : direction){
                int x1 = x + dir[0], y1 = y + dir[1];
                if (x1 < 0 || y1 < 0 || x1 >= matrix.length || y1 >= matrix[0].length){
                    continue;
                }
                if (matrix[x1][y1] == 0){
                    continue;
                }
                if (!visited[x1][y1]){
                    visited[x1][y1] = true;
                    matrix[x1][y1] = Integer.MAX_VALUE;
                }
                if ((matrix[x][y] + 1) > matrix[x1][y1]){
                    continue;
                }else {
                    matrix[x1][y1] = matrix[x][y] + 1;
                    update(matrix, x1, y1);
                }
            }
        }

        public int[][] updateMatrix(int[][] matrix) {
            visited = new boolean[matrix.length][matrix[0].length];
            for (int i = 0; i < matrix.length; i++){
                for (int j = 0; j < matrix[0].length; j++){
                    if (matrix[i][j] == 0){
                        update(matrix, i, j);
                    }
                }
            }
            return matrix;
        }
    }
}
