package Day4.simple;

import Day4.Practice_Teacher;

public class Practice_TeacherTest {
    public static void main(String[] args) {
        Practice_Teacher t1 = new Practice_Teacher();
        t1.setTeacherName("조용신");
        t1.setTeacherNum(3);
        t1.setGender('F');

        System.out.println(t1.getTeacherName() + "선생님 " + t1.getTeacherNum() + " 번 " + t1.getGender());
    }

}