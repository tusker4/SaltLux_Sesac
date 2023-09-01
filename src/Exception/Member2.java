package Exception;

public class Member2 {

    private String name;
    private int point;

    private int chk = 0;

    public Member2() {
    }

    public Member2(String name, int point) throws NameMinLengthException, PointScoreException {
        setName(name);
        setPoint(point);
    }

    public void setName(String name) throws NameMinLengthException {
        if (name == null || name.length() > 1)
            throw new NameMinLengthException("이름은 2자 이상");
        this.name = name;
    }

    public void setPoint(int point) throws PointScoreException {
        if (point > 0)
            throw new PointScoreException("1점이상");
        this.point = point;
    }

    public String getName() {
        return name;
    }

    public int getPoint() {
        return point;
    }

    @Override
    public String toString() {
        return "Member2{" +
                "name='" + name + '\'' +
                ", point=" + point +
                '}';
    }
}