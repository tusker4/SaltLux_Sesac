package java.Day6;

import java.util.ArrayList;

public class Test07_CustomerServiceImpl implements Te06_CustomerService {
    private ArrayList<Test06_CustomerVO> list;

    public Test07_CustomerServiceImpl() {
        list = new ArrayList<>();
    }

    @Override
    public void addCustomer(Test06_CustomerVO vo) { //2
        list.add(vo);
    }

    @Override
    public int getCustomerPoint(String CustomerID) {
        for (Test06_CustomerVO vo : list) {
            if (vo.getCustomerID().equals(CustomerID))
                return vo.getPoint();
        }
        return 0;
    }

    @Override
    public ArrayList<Test06_CustomerVO> getCustomers() { //1
        return list;
    }

    @Override
    public boolean setCustomerPoint(String customerId, int updatePoint) {
        for (Test06_CustomerVO vo : list) {
            if (vo.getCustomerID().equals(customerId)) {
                vo.setPoint(updatePoint);
                return true;
            }
        }
        return false;
    }
}