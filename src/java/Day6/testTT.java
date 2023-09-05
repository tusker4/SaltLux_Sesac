package java.Day6;

import java.util.HashSet;

public class testTT {
    public static HashSet getHashSet(HashSet<Integer> lotto) {
        int num = 0;
        while (true) {
            num = (int) (Math.random() * 45 + 1);
            lotto.add(num);
            if (lotto.size() == 6)
                break;
        }
        return lotto;
    }

    public static void main(String[] args) {
        System.out.println(getHashSet(new HashSet<>()));
    }
}