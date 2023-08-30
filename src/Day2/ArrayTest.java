package Day2;

import java.util.Scanner;

public class ArrayTest {
    //    메인 메서드
//    void : 패턴, 타입
//    String[] args : 입력
//    {  } 처리
    public static void main(String[] args) {
        float[] f1 = new float[2];
        char[] sizes = {'S', 'M', 'L'};
        String[] names = {"이순신", "홍길동"};
        for (int i = 0; i < f1.length; i++) {
            System.out.println(f1[i]);
        }


        System.out.println(sizes);

        for (String tmp : names) {
            System.out.println(tmp);
        }
    }

}
