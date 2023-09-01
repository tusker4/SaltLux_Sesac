package Exception;

public class Member2Test {

    public static void main(String[] args) {
        try {
            //case1 둘다 틀림
            System.out.println(new Member2("영", 0));
        } catch (Exception e) {
            e.printStackTrace();
        }
        //case2 이름
        try {
            System.out.println(new Member2("영", 1));
        } catch (Exception e) {
            e.printStackTrace();
        }

        //case3 포인트
        try {
            System.out.println(new Member2("하나", 0));
        } catch (Exception e) {
            e.printStackTrace();
        }

        //case4 맞음
        try {
            System.out.println(new Member2("하나", 1));
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("end");
    }

}