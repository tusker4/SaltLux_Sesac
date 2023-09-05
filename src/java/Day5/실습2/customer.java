package java.Day5.실습2;

public class customer {
    private String customerName;
    private int point;

    public customer(String customerName, int point) {
        this.customerName = customerName;
        this.point = point;
    }

    public void setCustomerName(String customerName) {
        if (customerName.length() >= 2) {
            this.customerName = customerName;
        }
    }

    public void setPoint(int point) {
        if (point >= 1) {
            this.point = point;
        }
    }

    public String getCustomerName() {
        return customerName;
    }

    public int getPoint() {
        return point;
    }
}