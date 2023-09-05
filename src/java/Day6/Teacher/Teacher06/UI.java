package java.Day6.Teacher.Teacher06;

import java.util.Scanner;

public class UI {
    private Scanner sc;
    private CustomerService service;

    public UI() {
        sc = new Scanner(System.in);
        service = new CustomerServiceImpl();
        checkMenu();
    }

    private void checkMenu() {
        while (true) {
            switch (Integer.parseInt(inputMessage("메뉴1~5 : "))) {
                case 1:
                    service.addCustomer(
                            new CustomerVO(inputMessage("id"),
                                    Integer.parseInt(inputMessage("point"))));

                    break;
                case 2:
                    System.out.println(service.getCustomerPoint(inputMessage("id")));
                    break;
                case 3:
                    System.out.println(service.getCustomers());
                    break;
                case 4:
                    service.setCustomerPoint(inputMessage("id"),
                            Integer.parseInt(inputMessage("수정할 포인트")));
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