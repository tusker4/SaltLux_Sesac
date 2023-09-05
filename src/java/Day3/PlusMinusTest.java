package java.Day3;

public class PlusMinusTest {
    //    메서드
    public static void main(String[] args) {
//        1. 입력
        PlusMinusTest pmt = new PlusMinusTest();
//  2. 처리 (result 함수에서해주고)  3. 출력
        System.out.println(pmt.result(1));
        System.out.println(pmt.result(0));
        System.out.println(pmt.result(-1));
    }

    //    메서드
    public String result(int num) {
//        1. 기본값 정의 (입력)
        String result = "양수";
//  2. 처리
        if (num == 0) {
            result = "숫자 0";
        } else if (num < 0) {
            result = "음수";
        }
//  3. 출력
        return result;
    }

}