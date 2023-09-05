package java.Day4.실습3.해답;

public class Manager extends Employee {

    private String position;

    public Manager(String employeeNumber, String name, String position) {
        super(employeeNumber, name);
        setPosition(position);
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public String getPosition() {
        return position;
    }

    public String toString() {
        return super.toString() + " " + position;
    }

}