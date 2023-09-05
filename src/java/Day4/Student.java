package java.Day4;

//객체
public class Student extends Person {
    //member data private 권장
    private String studentNumber;

    public Student() {
        super();  //부모의 기본 생성자 호출
    }

    public Student(String studentNumber, String name, char gender) {
        super(name, gender);
        setStudentNumber(studentNumber);
//        this.StudentNumber = StudentNumber
        //setName(name);
        //setGender(gender);
    }

    public void setStudentNumber(String studentNumber) {
        this.studentNumber = studentNumber;
    }

    public String getStudentNumber() {
        return studentNumber;
    }

}