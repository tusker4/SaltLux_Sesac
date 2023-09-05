import java.util.Random;
import java.util.Scanner;

public class Answer {
    public static void main(String[] args) {
        // 사용자 입력 숫자 처리
        Scanner s = new Scanner(System.in);
        int num;

        int correct = 0;
        for (int i = 0; i < 10; i++) {
            // 컴퓨터 랜덤 숫자 처리
            Random rnd = new Random();
            int comNum = rnd.nextInt(2);

            System.out.print("홀, 짝을 선택해 주세요 (홀: 0, 짝: 1) =>");
            num = s.nextInt();

            if (num == 0 || num == 1) {
                if (comNum == num) {
                    System.out.println("맞쳤습니다!!!");
                    correct++;
                } else {
                    System.out.println("틀렸습니다!!!");
                }
            } else {
                System.out.println("잘못 입력하셨습니다!!!");
            }
        }
        if (correct >= 7) { // 10, 9, 8, 7
            System.out.println("## 축하합니다. 오늘 운세가 상당히 좋습니다!!!");
        } else if (correct >= 5) { // 6, 5
            System.out.println("# 당신의 오늘 운세는 나쁘지 않습니다.");
        } else if (correct >= 3) { // 4, 3
            System.out.println("# 오늘 조심하세요~");
        } else {
            System.out.println("@@@@ 오늘은 아무것도 하지 마세요!");
        }

        s.close();
    }


}
