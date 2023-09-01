package Day5;

public class customer {
    public String Id;
    public long password;

    public customer() {

    }

    public customer(String Id, long password) {
        this.Id = Id;
        this.password = password;
    }

    public void setId(String id) {
        Id = id;
    }

    public void setPassword(long password) {
        this.password = password;
    }

    public String getId() {
        return Id;
    }

    public long getPassword() {
        return password;
    }
}