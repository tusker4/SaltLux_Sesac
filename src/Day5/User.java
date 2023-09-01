package Day5;

public interface User { //생성자 X
    // 이름 수정, 확인, 포인트 확인
// 누가 뭘 개발하든 이건 무조건 있어야 한다.
    public abstract void setName(String name); // public abstract 생략 가능

    String getName();

    int getPoint();
}