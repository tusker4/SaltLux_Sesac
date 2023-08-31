package Day4;

public class Teacher extends Person {
    private String teacherNumber;

    public Teacher(String teacherNumber, String name, char gender) {
        super(name, gender);
        this.teacherNumber = teacherNumber;
    }

    public String getTeacherNumber() {
        return teacherNumber;
    }

}