package Day3;

public class Day3_Array2dimension {
    public static void main(String[] args) {
        int[][] num1 = new int[2][3];

//        성적 1등 1명, 2등 2명, 3등 10명
        int[][] num2 = new int[3][]; // 인원이 다르기 때문에
        num2[0] = new int[1];
        num2[1] = new int[2];
        num2[2] = new int[10];
    }

}