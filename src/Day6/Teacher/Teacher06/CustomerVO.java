package Day6.Teacher.Teacher06;

//VO:ValueObject -->DATA 중심의 클래스
public class CustomerVO {
    private String customerId;
    private int point;

    public CustomerVO() {
    }

    public CustomerVO(String customerId, int point) {
        setCustomerId(customerId);
        setPoint(point);
    }

    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }

    public void setPoint(int point) {
        this.point = point;
    }

    public String getCustomerId() {
        return customerId;
    }

    public int getPoint() {
        return point;
    }

    @Override
    public String toString() {
        return customerId + "=" + point;
    }
}