import java.util.Scanner;

public class DAY1_2 {
    public static void main(String[] args) {
//        1. scanner
        Scanner s = new Scanner(System.in);
//        2. 선언
        int java = 3 , mobile = 2, excel = 1;
        final double A = 4.5, A0 = 4.0, B = 3.5;
        double avg;
//        3. 함수
        avg = (java * B + mobile*A0 + excel*A) / (java + mobile + excel);

//        4. 결과
        System.out.println( "평균학점 :" + Math.round(avg*100.0)/100.0);
        System.out.printf("평균학점 : %.2f", avg);
//        1-2. 닫음
        s.close();

    }

}
