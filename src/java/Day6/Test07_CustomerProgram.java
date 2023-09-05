package java.Day6;

import java.util.Scanner;

//프로그램 실행
//
//        1. 고객정보 입력
//        2. 고객정보 확인
//        3. 모든 고객정보를 확인
//        4. 특정고객 정보를 수정
//        5. 프로그램 종료
public class Test07_CustomerProgram {
    public Test07_CustomerProgram() {

    }

    public static void main(String[] args) {
        new Test06_UI(); // UI 클래스만들면 에러안남

        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        if (num == 1) {
            System.out.println(1);
        }
        System.out.println("실행할 숫자를 입력하세요");

    }
}