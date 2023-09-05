package java.Day6;

// VO :
public class Test06_CustomerVO {
    private String CustomerID;
    private int Point;

    public Test06_CustomerVO(String id, int point) {
    }

    public void Test06_CustomerVO(String CustomerID, int Point) {
        this.CustomerID = CustomerID;
        this.Point = Point;
//        setCustomerID(CustomerID)
//        setPoint(Point)
    }

    public String getCustomerID() {
        return CustomerID;
    }

    public int getPoint() {
        return Point;
    }

    public void setCustomerID(String customerID) {
        CustomerID = customerID;
    }

    public void setPoint(int point) {
        Point = point;
    }

}