package java.Day6;

import java.util.Scanner;

public class Test06_UI_Teacher {
    private Scanner sc;

    public Test06_UI_Teacher() {
        sc = new Scanner(System.in);
        checkMenu();
    }

    private void checkMenu() {
        while (true) {
            switch (Integer.parseInt(inputMessage("메뉴1~5 : "))) {
                case 1:
                    break;
                case 2:
                    break;
                case 3:
                    break;
                case 4:
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("메뉴는 1~5까지만");

            }

        }
    }

    private String inputMessage(String title) {
        System.out.print(title);
        return sc.nextLine();
    }
}