package Day6.Teacher.Teacher06;

import java.util.ArrayList;

public interface CustomerService {
    //1. 고객정보 입력    //아이디, 포인트
    void addCustomer(CustomerVO vo);

    //2. 고객 포인트정보 확인    //아이디
    int getCustomerPoint(String customerId);

    //3. 모든 고객 정보 확인
    ArrayList<CustomerVO> getCustomers();

    //4. 특정 고객 정보를 수정    //아이디    //포인트수정
    boolean setCustomerPoint(String customerId, int updatePoint);
}