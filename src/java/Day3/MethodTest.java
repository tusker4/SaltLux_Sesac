package java.Day3;

public class MethodTest {
    //    메서드
    public int sum(int num1, int num2) {
        int sum = num1 + num2;
        return sum;
    }

    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;
        int sum = num1 + num2;
        System.out.println(sum);
        MethodTest mt = new MethodTest();
        System.out.println(mt.sum(10, 20));
        System.out.println(mt.sum(-10, 20));
    }

}