package java.Day5;

// 고객의 고객아이디, 비밀번호, 비밀버호 수정가능
// 관리자는 관리자의 아이디, 비밃번호, 담당부서 있다
// 비밀번호 담당부서를 수정가능하다

public class Practice_admin extends Practice_customer {
    private String AdminId;
    private String Department;

    public Practice_admin(String AdminId, String Password, String Department) {
        super(Password);
        setDepartment(Department);
    }

    public void setAdminId(String AdminId) {
        AdminId = AdminId;
    }

    public String getAdminId() {
        return AdminId;
    }

    public void setDepartment(String Department) {
        Department = Department;
    }

    public String getDepartment() {
        return Department;
    }

}