package java.Day5;

public class CustomerUser implements User {
    //        재정의한다.
    private String name;
    private int point;

    public CustomerUser(String name, int point) {
        this.point = point;
        setName(name);
    }

    public void setName(String name, int point) {
        this.name = name;
    }

    @Override
    public void setName(String name) {

    }

    public String getName() {
        return name;
    }

    ;

    public int getPoint() {
        return point;
    }
}