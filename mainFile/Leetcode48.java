package com.cy.algorithm.leetcode.medium;

/**
 * 题名 : 旋转图像
 * 题目 : 给定一个 n × n 的二维矩阵表示一个图像。
 * 将图像顺时针旋转 90 度。
 * 说明：
 * 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
 *
 * 思路 : 简单的方法是新建一个数组然后翻转最后用system.arrayCopy拷贝到原数组,或者由外向内翻转
 * 一圈一圈旋转,找到被替换元素之间的关系
 * 执行时间 : 2ms
 * @author clay
 * @date 18-11-17 15:46
 */
public class Leetcode48 {

    public void rotate(int[][] matrix) {
        int len = matrix.length;
        //一层一层旋转的次数
        int t = len/2;
        for(int i = 0; i < t; i++){
            int inneLen = len - i * 2;
            for(int j = 0; j < inneLen-1; j++){
                int backup = matrix[i][i+j];
                matrix[i][i+j] = matrix[i+inneLen-j-1][i];
                matrix[i+inneLen-j-1][i] = matrix[i+inneLen-1][i+inneLen-j-1];
                matrix[i+inneLen-1][i+inneLen-j-1] = matrix[i+j][i+inneLen-1];
                matrix[i+j][i+inneLen-1] = backup;
            }

        }
    }

    public static void main(String []args){
        Leetcode48 l = new Leetcode48();
        int [][]arr = new int[][]{{1,2,2,1},{3,4,4,3},{5,6,6,5},{7,8,8,7}};
        l.rotate(arr);
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[0].length; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
