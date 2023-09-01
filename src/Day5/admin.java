package Day5;

// 고객의 고객아이디, 비밀번호, 비밀버호 수정가능
// 관리자는 관리자의 아이디, 비밃번호, 담당부서 있다
// 비밀번호 담당부서를 수정가능하다

public class admin extends customer {
    public String department;

    public admin(String Id, long password, String department) {
        super(Id, password);
        setDepartment(department);
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getDepartment() {
        return department;
    }
}