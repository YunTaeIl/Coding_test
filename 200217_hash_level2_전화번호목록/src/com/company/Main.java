package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {
	// write your code here

        String[] strings = {"119","97674223","1195524421"};
        String[] strings2 = {"123","456","789"};
        String[] strings3 = {"119","1192456"};
        String[] strings4 = {"1192456","119"};


        System.out.println(Solution.solution(strings4));
    }



    static class Solution {
        public static boolean solution(String[] phone_book) {
            boolean answer = true;

            Arrays.sort(phone_book);

            for(int i = 0; i < phone_book.length; i++){
                for(int j = i + 1; j < phone_book.length; j++){
                    try{
                        if(phone_book[i].equals(phone_book[j].substring(0,phone_book[i].length()))){
                            return false;
                        }
                    } catch (StringIndexOutOfBoundsException e){

                    }

                }
            }

            return answer;
        }
    }

}
