package test.com.oopsw.simple;

import Day4.실습3.해답.Employee;
import Day4.실습3.해답.Manager;

public class EmployeeTest {

    public static void main(String[] args) {
        Employee[] list = new Employee[4];

        list[0] = new Employee("2942949", "Scott");
        list[1] = new Employee("5324563", "Tiger");
        list[2] = new Manager("141242141", "King", "Manager");
        list[3] = new Manager("141242142", "Allen", "Clerk");

        for (Employee emp : list) {
            System.out.println(emp);
        }//for

    }

}