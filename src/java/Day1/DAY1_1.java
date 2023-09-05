import java.util.Scanner;

public class DAY1_1 {
    public static void main(String[] args) {
//        1. scanner
        Scanner s = new Scanner(System.in);
//        2. 형식
        String name = s.next();
        String add = s.next();
        String weight = s.next();
        int fee = Integer.parseInt(weight) * 5;
//        3. 함수
        display(name);
        display(add);
        display(fee + "");
//        1-2. 닫음
        s.close();

    }
    //    3 . 함수
    public static void display(String msg){
//        4. 결과
        System.out.println(msg);
    }

}
