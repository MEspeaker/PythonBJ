import java.util.*;

public class Main {
    public static void main(String[]args){
        Queue<Integer> q= new LinkedList<>();
        Scanner scan= new Scanner(System.in);
        int N= scan.nextInt();
        int lastNum=0;
        for(int i=0;i<N; i++){
            String M= scan.next();
            if(M.equals("push")){
                int O= scan.nextInt();
                q.offer(O);
                lastNum=O;
            }
            else if(M.equals("pop")){
                if (q.isEmpty()) {
                    System.out.println(-1);
                } else
                    System.out.println(q.poll());
            }
            else if(M.equals("size")){
                System.out.println(q.size());
            }
            else if (M.equals("empty")) {
                if (q.isEmpty()) {
                    System.out.println(1);
                }
                else {
                    System.out.println(0);
                }
            }
            else if (M.equals("front")) {
                if (q.isEmpty()) {
                    System.out.println(-1);
                } else
                    System.out.println(q.peek());
            }
            else if (M.equals("back")) {
                if (q.isEmpty()) {
                    System.out.println(-1);
                } else
                    System.out.println(lastNum);
            }
        }
    }
}