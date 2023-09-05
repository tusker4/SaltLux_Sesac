package java.Day3;

public class MinMaxTest {
    //    메서드
    public static void main(String[] args) {
//        1. 입력
        MinMaxTest mmt = new MinMaxTest();
//  2. 처리 (result 함수에서해주고) 3. 출력
        System.out.println("최대값은 " + mmt.Max(3, 2, 3));
        System.out.println("최소값은 " + mmt.Min(3, 2, 3));
    }

    //    메서드
    public int Max(int num1, int num2, int num3) {
//        1. 기본값 정의 (입력)

        int numMax = num1;
//  2. 처리
        if (num2 > num1) {
            numMax = num2;
        }
        ;

        if (num3 > num2) {
            numMax = num3;
        }
        ;

        if (num1 > num3) {
            numMax = num1;
        }
        ;

//  3. 출력
        return numMax;
    }

    public int Min(int num1, int num2, int num3) {
//        1. 기본값 정의 (입력)

        int numMin = num1;
//  2. 처리
        if (num2 < num1) {
            numMin = num2;
        }
        ;

        if (num3 < num2) {
            numMin = num3;
        }
        ;
        if (num1 < num3) {
            numMin = num1;
        }
        ;

//  3. 출력
        return numMin;
    }

}