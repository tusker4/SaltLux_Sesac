package Day3;

public class MinMaxPractice {
    //    메서드
    public static void main(String[] args) {
//        1. 입력
//  2. 처리 (result 함수에서해주고) 3. 출력
        System.out.println("최소값은 " + new MinMaxPractice().numMin(0, 1, 2));
    }

    public int numMin(int num1, int num2, int num3) {
//        1. 기본값 정의 (입력)
        int[] numbers = {num1, num2, num3};
//       1,2,3 으로 받으면 매개인자가 배열로 받는 메서드로 넘길 것이다.
//  2. 처리
//  3. 출력
        return numMin(numbers);
    }

    public int numMin(int[] numbers) {
//        1. 기본값 정의 (입력)
        int min = numbers[0];
//  2. 처리
        for (int i = 1; i < numbers.length; i++) {
            if (min > numbers[i]) {
                min = numbers[i];
            }
        }
//  3. 출력
        return min;
    }

}

//    선생님의 minMax