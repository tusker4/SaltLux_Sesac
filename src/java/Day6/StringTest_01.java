package java.Day6;

public class StringTest_01 {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 10;
        String s1 = "h1";
        String s2 = "h1";
        String s3 = new String("h1");
        String s4 = new String("h1");
//        s1 ~ s4 저장되는 장소가다르다

        System.out.println(num1 == num2);
        System.out.println(s1 == s2);
        System.out.println(s3 == s4);
        String s5 = s4;
        System.out.println(s5 == s4);
    }
}