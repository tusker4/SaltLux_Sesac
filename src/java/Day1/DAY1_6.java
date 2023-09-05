import java.util.Random;
import java.util.Scanner;

public class DAY1_6 {
    public static void main(String[] args) {

//        0. scanner
        Scanner s = new Scanner(System.in);


//        1. 선언
        int num;


//        2. 함수

//        3. 결과값.
//        1) for문
        int correct = 0;

        for (int i = 0; i < 8; i++) {
            Random rnd = new Random();
            int comNum = rnd.nextInt(2);
            System.out.println(comNum);
            System.out.println("홀 짝을 선택해주세요 (홀:0, 짝:1)");
            num = s.nextInt();


            if (num == 0 || num == 1) {
                if (comNum == num) {
                    System.out.println("맞혔습니다.");
                    correct++;
                } else {
                    System.out.println("틀렸습니다.");
                }
            } else {
                System.out.println("잘못입력하셨습니다");
            }


        }
        if (correct >= 7) {
            System.out.println("오늘 운세가 좋습니다.");
        } else if (correct >= 5) {
            System.out.println("오늘운세가 나쁘지않습니다.");
        } else if (correct > 3) {
            System.out.println("오늘운세가 나쁩니다.");
        } else {
            System.out.println("BAD");
        }

        s.close();


//        2) while문
        int count = 0;
        while (count++ < 10) {


        }


    }


}
