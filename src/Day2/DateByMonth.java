package Day2;

import java.util.Scanner;

public class DateByMonth {
    public static void main(String[] args) {
//        1. 입력
        Scanner s = new Scanner(System.in);
//
        int month = s.nextInt();

//        2. 처리 == 함수
        if (month > 13 || month < 1) {
            System.out.println("잘못입력하였습니다.");
        } else {
            switch (month) {
                case 2:
                    System.out.printf("%d월은 28일까지 입니다.", month);
                    break;
                case 4, 6, 9, 11:
                    System.out.printf("%d월은 30일까지 입니다.", month);
                    break;
                case 1, 3, 5, 7, 8, 10, 12:
                    System.out.printf("%d월은 31일까지 입니다.", month);
                    break;
            }
        }
//        3. 리턴, 자원 반환

        s.close();
    }
}
