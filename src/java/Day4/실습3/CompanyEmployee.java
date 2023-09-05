package java.Day4.실습3;

public class CompanyEmployee {
    private int personID;
    private String personName;

    public CompanyEmployee() {

    }

    public CompanyEmployee(int personID, String personName) {
        setPersonID(personID);
        setPersonName(personName);
    }

    public void setPersonID(int personID) {
        this.personID = personID;
    }

    public void setPersonName(String personName) {
        this.personName = personName;
    }

    public int getPersonID() {
        return personID;
    }

    public String getPersonName() {
        return personName;
    }

}