package Day5.IO;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class SysyemIOTest {
    public static void main(String[] args) throws FileNotFoundException {
        System.setOut(new PrintStream(new FileOutputStream("out.txt")));
//        setout 이라는 설정파일로 파일로 출력
        System.out.println("ABC 한글1234");
    }
}