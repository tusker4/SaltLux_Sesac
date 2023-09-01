package Day5;

// 고객의 고객아이디, 비밀번호, 비밀버호 수정가능
// 관리자는 관리자의 아이디, 비밃번호, 담당부서 있다
// 비밀번호 담당부서를 수정가능하다

public class Practice_customer {
    private String CustomerId;
    private String Password;

    public Practice_customer() {

    }

    ;
//    이거 왜만들지?

    public Practice_customer(String CustomerId, String Password) {
        this.CustomerId = CustomerId;
        this.Password = Password;
    }

    public Practice_customer(String password) {
    }

    public void setPassword(String Password) {
        Password = Password;
    }

    public String getPassword() {
        return Password;
    }

    public void setCustomerId(String customerId) {
        CustomerId = customerId;
    }

    public String getCustomerId() {
        return CustomerId;
    }
}