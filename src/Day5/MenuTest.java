package Day5;

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

// 1. 프로그램은 계속 실행
//2. 키보드로 문자열을 입력하고 입력된 문자열은 모니터로 전송
//3. 프로그램 종료 exit 문자열을 입력하면 종료
// 451p 참고
public class MenuTest {

    public MenuTest() throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        FileWriter out = new FileWriter("menu_out.txt");
        while (true) {
            String word = br.readLine();
            out.write(word + "\n");
            out.flush(); // 여기여기로 전달해라
            if (word.equals("exit")) {
                break;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new MenuTest();

    }
}