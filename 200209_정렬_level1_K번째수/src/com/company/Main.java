package com.company;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        // write your code here
        System.out.println(Solution.solution(new int[]{10, 11, 20, 2, 3, 1}, new int[][]{{2, 5, 3}, {4, 4, 1}}));
    }


    static class Solution {
        public static int[] solution(int[] array, int[][] commands) {


            int[] answer = new int[commands.length];

            int i = 0; // 시작
            int j = 0; // 끝
            int k = 0; // 몇번째 숫자
            int a = 0;

            for (int[] cmd : commands) {

                ArrayList<Integer> arraylist = new ArrayList(); // 값을 저장할 arraylist

                i = cmd[0];
                j = cmd[1];
                k = cmd[2];

                for (int count = i - 1; count < j; count++) {
                    arraylist.add(array[count]);
                }

                Collections.sort(arraylist);
                answer[a] = arraylist.get(k - 1);

                //System.out.println(a);
                //System.out.println(answer[a]);

                a++;
            }

            return answer;
        }
    }

}