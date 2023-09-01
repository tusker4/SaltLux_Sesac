package 실습2;

//고객의 정보는 이름, 포인트로 관리
// 고객정보를 입력할 때 이름 2자 이상, 포인트는 1점이상
// 혹시 하나라도 만족하지 않으면 고객의 정보를 입력못하게한다.
public class customerInfo {
    public static void main(String[] args) {
        customer c = new customer("김", 3);

        System.out.println(c.getCustomerName() + "  " + c.getPoint());
        System.out.println("고객의 정보가 입력되었습니다.");
    }
}