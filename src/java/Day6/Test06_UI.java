package java.Day6;

import java.util.ArrayList;
import java.util.Scanner;

public class Test06_UI {
    private Scanner sc;
    private Te06_CustomerService service;

    public Test06_UI() {
        sc = new Scanner(System.in);
        service = new Te06_CustomerService() {
            @Override
            public void addCustomer(Test06_CustomerVO vo) {

            }

            @Override
            public int getCustomerPoint(String CustomerID) {
                return 0;
            }

            @Override
            public ArrayList<Test06_CustomerVO> getCustomers() {
                return null;
            }

            @Override
            public boolean setCustomerPoint(String customerId, int updatePoint) {
                return false;
            }
        };
        checkMenu();
    }

    private void checkMenu() {
        while (true) {
            switch (Integer.parseInt(inputMessage("메뉴 1~5: "))) {

                case 1:
                    service.addCustomer(new Test06_CustomerVO(inputMessage("id"), Integer.parseInt(inputMessage("point"))));
                    break;
                case 2:
                    System.out.println(service.getCustomerPoint(inputMessage("id")));
                    break;
                case 3:
                    System.out.println(service.getCustomers());
                    break;
                case 4:
                    service.setCustomerPoint(inputMessage("id"),
                            Integer.parseInt(inputMessage("point")));
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("메뉴는 1~5까지만");
//                    커맨드패턴
            }
        }

    }

    private String inputMessage(String title) {
        System.out.print(title);
        return sc.nextLine();
    }
}