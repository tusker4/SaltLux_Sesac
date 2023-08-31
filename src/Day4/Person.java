package Day4;

//학번, 이름, 성별,-교사번호, 이름, 성별
//공통 멤버 구현
public class Person {
    //1privat member data
    private String name;
    private char gender;

    public Person() {
    }

    public Person(String name, char gender) {
        setName(name);//this.name=name;
        setGender(gender);
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setGender(char gender) {
        this.gender = gender;
    }

    public String getName() {
        return name;
    }

    public char getGender() {
        return gender;
    }
}