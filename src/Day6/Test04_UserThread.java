package Day6;

class UserA extends Thread {
    private int count;

    public void run() {
        while (true) {
            System.out.println(++count + "" + toString());
            if (count >= 50)
                break;

        }
    }
}

class UserB implements Runnable {
    private int count;

    public void run() {
        while (true) {
            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            countPrint();
            if (count >= 50)
                break;
        }
    }

    private synchronized void countPrint() {
//        스레드를 일할때는 동시에 일한다 -> 동시에 일하는 거 막을때 synchronized
//        static 처럼 동시에 돌아가는 걸 예방해서 동시성을 막을 때
        System.out.println(++count + "" + Thread.currentThread().toString());
    }

}

public class Test04_UserThread {
    public static void main(String[] args) {
        UserB data = new UserB();
        Thread t1 = new Thread(data);  // 구조패턴
        Thread t2 = new Thread(data);
        t1.start();
        t2.start();
//        UserA t1 = new UserA();
//        UserA t2 = new UserA();
//        t1.run();
//        t2.run();
//
//        t1.start();
//        t2.start();
    }
}