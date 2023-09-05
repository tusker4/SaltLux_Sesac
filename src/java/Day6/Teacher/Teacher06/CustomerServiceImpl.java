package java.Day6.Teacher.Teacher06;

import java.util.ArrayList;

public class CustomerServiceImpl implements CustomerService {
    private ArrayList<CustomerVO> list;

    public CustomerServiceImpl() {
        list = new ArrayList<>();
    }

    @Override
    public void addCustomer(CustomerVO vo) {
        list.add(vo);
    }

    @Override
    public int getCustomerPoint(String customerId) {
        for (CustomerVO vo : list) {
            if (vo.getCustomerId().equals(customerId))
                return vo.getPoint();
        }
        return 0;
    }

    @Override
    public ArrayList<CustomerVO> getCustomers() {
        return list;
    }

    @Override
    public boolean setCustomerPoint(String customerId, int updatePoint) {
        for (CustomerVO vo : list) {
            if (vo.getCustomerId().equals(customerId)) {
                vo.setPoint(updatePoint);
                return true;
            }
        }
        return false;
    }
}