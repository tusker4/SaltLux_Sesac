package Day2;

import java.util.ArrayList;
import java.util.Scanner;

public class Practice {
    //    입력 - 처리 - 출력
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int korean;
        while (true) {
            System.out.println("국어점수를 입력하세요");
            korean = scanner.nextInt();
            if (korean <= 100 && korean >= 0) {
                break;
            }
        }

        System.out.println("영어점수를 입력하세요");
        int english = scanner.nextInt();

        System.out.println("수학점수를 입력하세요");
        int math = scanner.nextInt();

        int scoreSum = korean + english + math;
        int scoreAvg = scoreSum / 3;

        System.out.println(scoreSum + "총점과" + scoreAvg + "평균");
        scanner.close();
    }

}