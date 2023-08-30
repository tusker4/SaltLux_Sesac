package Day2;

import java.util.Scanner;

public class ScoreSumAvg {
    public static void main(String[] args) {
//        1. 입력
        Scanner scanner = new Scanner(System.in);

        System.out.print("국어 성적을 입력하세요.");
        int korean = scanner.nextInt();
        if (korean > 100 || korean < 0) {
            System.out.println("잘못입력하였습니다. 다시입력하세요");
        }

        System.out.print("영어 성적을 입력하세요.");
        int english = scanner.nextInt();

        System.out.print("수학 성적을 입력하세요.");
        int math = scanner.nextInt();


        int sumScore = korean + english + math;
        double avgScore = sumScore / 3;

//        3. 출력
        System.out.println("총점은" + sumScore + ", 평균은 " + avgScore + "입니다. ");
        scanner.close();
    }

}
