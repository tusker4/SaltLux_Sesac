package test.com.oopsw.simple;

import Day4.Person;

public abstract class Password {
    //    abstract : 생성자를 못보게 막아야
    private String pw;

    public Password(String pw) {
        setPw(pw);
    }

    public void setPw(String pw) {
//        pw 암호화정책
        this.pw = pw;
    }

    public String getPw() {
        return pw;
    }

    public abstract boolean login(String id, String pw); //1
//    업무중심 331p,

}