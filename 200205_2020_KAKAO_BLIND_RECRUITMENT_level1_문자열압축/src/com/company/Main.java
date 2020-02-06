package com.company;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    public static void main(String[] args) {
        // write your code here
        System.out.println(Solution.solution(new String[]{"leo,", "kiki", "eden"}, new String[]{"kiki", "eden"}));
    }

    static class Solution {
        public static String solution(String[] participant, String[] completion) {
            String answer = "";

            int i = 0;

            ArrayList <String> arrayList = new ArrayList<>(Arrays.asList(participant));   // array list로 변환
            ArrayList <String> arrayList2 = new ArrayList<>(Arrays.asList(completion));   // array list로 변환
            ArrayList <String> arrayList3 = new ArrayList<>();   // 새로운 어레이리스트

            Collections.sort(arrayList);
            Collections.sort(arrayList2);

            while(true){
                if(arrayList2.get(i).equals(arrayList.get(i))){
                    // 같으면 다음으로가야되는데
                } else{
                    return arrayList.get(i);
                }
                if(i == arrayList2.size()-1){
                    return arrayList.get(i+1);
                }
                i++;
            }
        }
    }
}
