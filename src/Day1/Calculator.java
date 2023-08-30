import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

//    1. 형식
        String name = s.next();
        String add = s.next();
        String weight = s.next();
        int fee = Integer.parseInt(weight);
//        2. 함수
        display(name);
        display(add);
        display(fee+"");

        s.close();
    }

    public static void display(String msg) {
        System.out.println(msg);
    }


};
