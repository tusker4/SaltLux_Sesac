package Day5.Exception;

public class ExceptionTest_02 {
    public static void main(String[] args) throws ClassNotFoundException {
        String s = new String();
//        try {
        Class.forName("java.lang.String");
//        } catch (ClassNotFoundException e) {
//            e.printStackTrace();
//        }
        System.out.println("end");
    }
}