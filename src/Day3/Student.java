package Day3;

// 이 요구사항은 데이터에 집중되어있다.
//학생 정보는 학번, 이름, 전화번호, 성별이다.
//특히 성별은 M F 저장할 예정이다.
//2명의 학생정보를 입력, 확인
public class Student {
    public static void main(String[] args) {

        System.out.println();
        System.out.println(name);
        System.out.println(phone);
        System.out.println(gender);

    }

    public void Student1() {
        int id = 2;
        String name = "강감찬";
        String phone = "010-1211-2222"; // 숫자에 0이 먼저들어가기 때문에
        Character gender = 'M';//        성별은 'M', 'F' 로 저장.... 싱글이기때문에 Charactor?
    }

    public void Student2() {
        int id = 3;
        String name = "남성희";
        String phone = "010-2222-2222"; // 숫자에 0이 먼저들어가기 때문에
        Character gender = 'F';//        성별은 'M', 'F' 로 저장.... 싱글이기때문에 Charactor?
    }
}