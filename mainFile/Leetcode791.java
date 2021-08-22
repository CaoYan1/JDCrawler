package com.cy.algorithm.leetcode.medium;

import java.util.HashMap;
import java.util.Map;

/**
 * 题名 : 自定义字符串排序
 * 题目 : 字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。
 * S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。
 * 更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。
 * 返回任意一种符合条件的字符串T。
 *
 * 思路 : 用hashmap存储每个字符的优先级(优先级递增),然后遍历另一个字符串,
 * 如果在优先级表中存储到优先级数组中(下表为优先级)并记录出现次数,最后合并出现和没出现过的.
 * 执行时间 : 4ms
 * @author clay
 * @date 18-11-12 15:12
 */
public class Leetcode791 {

    class Element{
        int n;
        char c;
    }

    public String customSortString(String S, String T) {
        Map<Character,Integer> priorityMap = new HashMap<>(26);
        Element []array = new Element[26];
        for(int i = 0; i < array.length; i++){
            array[i] = new Element();
        }
        char []sArray = S.toCharArray();
        char []tArray = T.toCharArray();
        int currentPriority = 0;
        //s1,s2分别存储在第一个字符串中的字符和不在第一个字符串中的字符
        StringBuilder s1 = new StringBuilder();
        StringBuilder s2 = new StringBuilder();
        //存储优先级
        for(char s : sArray){
            if(!priorityMap.containsKey(s)){
                priorityMap.put(s,currentPriority++);
            }
        }
        //两种字符分离
        for(char t : tArray){
            Integer priority = priorityMap.get(t);
            if(priority == null){
                s1.append(t);
            }else {
                array[priority].c = t;
                array[priority].n++;
            }
        }
        for(Element e : array){
            for(int i = 0; i < e.n; i++){
                s1.append(e.c);
            }
        }
        s1.append(s2);
        return s1.toString();
    }

    public static void main(String ...args){
        Leetcode791 p = new Leetcode791();
        System.out.println(p.customSortString("gcmnrwpozitfqajxdshveyklu",
                "sgkkjkjtfcabzpsqpfqoomqtxiaqgumdqzhjojjwmjcogciidjklxnwzfgnwxmccwlyzduiyntenkhzabwjgbggwyezpcirjmpktndseqitpbkaczktbzqyqeozblzcuzsnvmtmtjlmffmmciuuuyqjelochmcduulcwijcramranjyzgskhajldfhltglpwshfbacuj"
        ));
    }
}
