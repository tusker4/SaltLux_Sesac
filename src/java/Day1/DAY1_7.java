import java.util.Random;

import java.util.Scanner;

public class DAY1_7 {
    public static void main(String[] args) {

        for (int dan = 2; dan <= 9; dan++) {
            for (int num = 2; num <= 9; num++) {
                int result = dan * num;
                System.out.println(dan + "x" + num + "=" + result);
            }
            System.out.println("---------------------------------");
        }
        System.out.println();
    }

    public static void two() {

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < i; j++) {
                System.out.println("*");
            }
            System.out.println();
        }

    }

}
