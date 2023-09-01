package Exception;

public class ExceptionTest_01 {
    public static void main(String[] args) {
        int[] size = {44, 55};
        try {
            for (int i = 0; i < 3; i++) {
                System.out.println(size[i]);
            }
        } catch (ArrayIndexOutOfBoundsException e) {
            e.printStackTrace();
//  오류를알려주고 종료
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("end");
    }
}