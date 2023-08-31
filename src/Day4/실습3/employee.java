package Day4.실습3;

public class employee extends CompanyEmployee {

    public employee() {
        super();  //부모의 기본 생성자 호출
    }

    public employee(int personID, String personName) {
        super(personID, personName);
        //setName(personID);
        //setGender(personName);
    }
}