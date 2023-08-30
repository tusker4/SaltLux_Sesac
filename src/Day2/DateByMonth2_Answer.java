package Day2;

import java.util.Scanner;

public class DateByMonth2_Answer {
    public static void main(String[] args) {
//        1. 입력
        Scanner scanner = new Scanner(System.in);
        int month;

//        2. 처리
        //            비기능 처리
        while (true) {
            System.out.print("월을 입력하세요.");
            month = scanner.nextInt();
            if (month >= 1 && month <= 12)
                break;
        }

        int date = 31;
        switch (month) {
            case 2:
                date = 28;
                break;
            case 4, 6, 9, 11:
                date = 30;
                break;
        }
//        3. 출력
        System.out.println(month + "월은 " + date + "입니다. ");
        scanner.close();
    }
}
