package java.Day5.IO;

import java.io.InputStream;
import java.io.InputStreamReader;

public class InputTest {
    public static void main(String[] args) throws Exception {
//        한개의 바이트를 읽는다.
        InputStream is = System.in;
        InputStreamReader isr = new InputStreamReader(is); // 구조패턴
        int input = isr.read();
        System.out.println(input + "  " + (char) input);
        isr.close();
        is.close();
    }
}