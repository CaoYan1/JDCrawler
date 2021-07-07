package com.cy.algorithm.leetcode.medium;

import java.util.Arrays;
import java.util.Comparator;

/**
 * 题名 : 用最少数量的箭引爆气球
 * 题目 : 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。
 * 一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
 *
 * 思路 : 按照气球的右边位置排序,从左往右遍历直到气球的左边位置大于第一个的右边为止,则之前的气球都可以一起引爆
 * 执行时间 : 122ms
 *
 * @author clay
 * @date 18-12-1 20:26
 */
public class Leetcode452 {

    class Solution {
        public int findMinArrowShots(int[][] points) {
            if(points == null || points.length == 0){
                return 0;
            }
            Arrays.sort(points, (o1, o2) ->
                o1[0] > o2[0] ? 1 : o1[0] == o2[0] ? 0 : -1
            );
            for(int i = 0; i < points.length; i++){
                for(int j = i + 1; j < points.length; j++){
                    if(points[j][0] > points[i][1]){
                        break;
                    }
                    if(points[j][1] <= points[i][1]){
                        points[i][0] = Integer.MIN_VALUE;
                        points[i][1] = Integer.MAX_VALUE;
                        break;
                    }
                }
            }
            int result = 0;
            int cur = 0;
            while(cur < points.length){
                if(points[cur][0] == Integer.MIN_VALUE && points[cur][1] == Integer.MAX_VALUE){
                    cur++;
                    continue;
                }
                int i = cur + 1;
                while(i < points.length && (points[i][0] <= points[cur][1] || (points[i][0] == Integer.MIN_VALUE && points[cur][1] == Integer.MAX_VALUE))){
                    i++;
                }
                cur = i;
                result++;
            }
            return result == 0 ? 1 : result;
        }
    }

    public static void main(String ...args){
        int[][] arg = new int[][]{{3,9},{7,12},{3,8},{6,8},{9,10},{2,9},{0,9},{3,9},{0,6},{2,8}
};
        Solution s = new Leetcode452().new Solution();
        System.out.println(s.findMinArrowShots(arg));
    }
}
