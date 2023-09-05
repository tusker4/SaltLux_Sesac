package java.Day2;

import java.util.Scanner;

public class DAY2_1 {
    public static void main(String[] args) {
//        1. scanner
        Scanner s = new Scanner(System.in);
//        2. 형식
//        next 를 쓰는 이유?  next -> nextInt
        int hour = s.nextInt();
        int minute = s.nextInt();

//        3. 함수
        int answer = minute + hour * 60;

//        4. 결과
        System.out.println(answer + "분");

//        1-2. 닫음
        s.close();

    }

}