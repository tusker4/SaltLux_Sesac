package java.Day2;

import java.util.Scanner;

public class ScoreTest {
    //    메인 메서드
//    void : 패턴, 타입
//    String[] args : 입력
//    {  } 처리
    public static void main(String[] args) {
//        지역변수는 초기화가 필수다 -> stack
        int score1 = 100, score2 = 90, score3 = 70;
//        같은 자료형이고, 의미가 같으면 --->  배열
        int[] scores = new int[3];
//        scoreTest를 실행하면,  무조건 잡히는 메모리공간이 있다.
//        이것이 static : 너무 많으면 로딩시간이길다. 그러니 1번, 공유하는 데이터만 올라온다
//        해석은 main 위주로 한다.

        Scanner sc = new Scanner(System.in);
        int totalScore = 0;
        float avgScore = 0;
        for (int i = 0; i < scores.length; i++) {
            scores[i] = sc.nextInt();
            totalScore += scores[i];
        }

        avgScore = (float) totalScore / scores.length;
        System.out.println("총점 :" + totalScore + ", 평균 : " + avgScore);
    }

}