package Day6;

import java.util.ArrayList;

// interface를 설계

public interface Te06_CustomerService {
    //    종료는 상관없으니 4개
//    1. 고객정보 입력
//    입력 되었는지 확인하고싶으니까 void
    void addCustomer(Test06_CustomerVO vo);

    //2. 고객 포인트 정보 확인
    int getCustomerPoint(String CustomerID);

    //3. 모든 고객정보를 확인
    ArrayList<Test06_CustomerVO> getCustomers();

    //4. 특정고객 정보를 수정
//    수정이 되었는지 안되었는지 알기위해 boolean 타입
    boolean setCustomerPoint(String customerId, int updatePoint);
}