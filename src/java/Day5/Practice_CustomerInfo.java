package java.Day5;

// 고객의 고객아이디, 비밀번호, 비밀버호 수정가능
// 관리자는 관리자의 아이디, 비밃번호, 담당부서 있다
// 비밀번호 담당부서를 수정가능하다

public class Practice_CustomerInfo extends Practice_customer {
    public static void main(String[] args) {
        Practice_customer Pc = new Practice_customer("남성희", "eee");

        System.out.println(Pc.getCustomerId());

    }

}