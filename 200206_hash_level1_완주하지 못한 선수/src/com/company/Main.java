package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.solution(new String[] {"a","b","b","c","a"}, new String[] {"b","c","b","a"}));
    }
}


class Solution {
    public static String solution(String[] participant, String[] completion) {
        String answer = "";

        int i = 0;

        ArrayList<String> arrayList = new ArrayList<>(Arrays.asList(participant));   // array list로 변환
        ArrayList<String> arrayList2 = new ArrayList<>(Arrays.asList(completion));   // array list로 변환

        Collections.sort(arrayList);
        Collections.sort(arrayList2);

        while (true) {
            if (arrayList2.get(i).equals(arrayList.get(i))) {
                // 같으면 다음으로가야되는데
            } else {
                return arrayList.get(i);
            }
            if (i == arrayList2.size() - 1) {
                return arrayList.get(i + 1);
            }
            i++;
        }


    }
}