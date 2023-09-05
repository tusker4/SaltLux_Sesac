package java.Day6;

import java.util.*;

public class ListTest_02 {
    public static Collection getCollection(Collection<Integer> c) {
//       뭐가 나올지 모르니 Collection ,  Collection 을 가져다 놓을 거야
        System.out.println(c.add(1234));
//         int --> integer
//        System.out.println(c.add("hello"));
//        System.out.println(c.add(new Date()));

        System.out.println(c.add(1234));
//         int --> integer
//        System.out.println(c.add("hello"));
//        System.out.println(c.add(new Date()));

        return c;
    }

    public static void main(String[] args) {
        System.out.println(getCollection(new ArrayList()));
        System.out.println(getCollection(new HashSet()));
    }
}