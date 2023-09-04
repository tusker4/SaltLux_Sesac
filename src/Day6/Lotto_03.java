package Day6;

import java.util.Arrays;
import java.util.HashSet;

// 로또 프로그램
// 1~ 45번까지 번호는 6개, 중복저장X (Hashset)
// 요구사항에 맞는 API를 찾는게 먼저다. -> Hashset

public class Lotto_03 {
    public static HashSet getHashset(HashSet<Integer> h) {
//        해당 클래스의 인스턴스(객체) 없이 호출될 수 있음을 의미
        int num = 0;
        while (true) {
            num = (int) (Math.random() * 45 + 1);
            h.add(num);
            if (h.size() == 6)
                break;
        }
        Object[] lottoArray = h.toArray();
        Arrays.sort(lottoArray);
        System.out.println(Arrays.toString(lottoArray));
        System.out.println(lottoArray);
        return h;
    }

    public static void main(String[] args) {
        System.out.println(getHashset(new HashSet<>()));
    }

}