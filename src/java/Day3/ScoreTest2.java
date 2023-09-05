package java.Day3;

//N명의 성적, 평균보다 낮은 사람은 몇명입니까? 소수점 버림
//        test 코드를 보고 구현메서드를 만들라는 것 : TDD
public class ScoreTest2 {

    public static void main(String[] args) {
        int[] data1 = {10, 20, 30};
        int[] data2 = {11, 12, 13, 12, 11};
        ScoreTest2 s = new ScoreTest2();
        System.out.println("실행결과는" + s.execute(data1) + " 명 입니다.");
        System.out.println("실행결과는" + s.execute(data2) + " 명 입니다.");

    }

    public int execute(int[] data) {
//        평균구하기
        int sum = 0;
        int count = 0;

        for (int i = 0; i < data.length; i++) {
            sum += data[i];
        }
        double avg = sum / data.length;
        System.out.println(avg);

//        몇명 입니까?
        for (int i = 0; i < data.length; i++) {
            if (avg > data[i]) {
                count++;
            }
        }
        return count;
    }
}