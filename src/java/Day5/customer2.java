package java.Day5;

import java.simple.Password;

public class customer2 extends Password {
    private String customerId;

    public customer2(String customerId, String pw) {
        super(pw);
        this.customerId = customerId;
    }

    //    재정의가 필수다
    public boolean login(String Id, String pw) {

        return false;
    }

}