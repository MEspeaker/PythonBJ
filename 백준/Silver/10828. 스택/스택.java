import java.util.*;

public class Main {
    public static void main(String[]args){
        Stack<Integer> stack= new Stack<>();
        Scanner scan= new Scanner(System.in);
        int N= scan.nextInt();
        for(int i=0;i<N; i++){
            String M= scan.next();
            if(M.equals("push")){
                int O= scan.nextInt();
                stack.push(O);
            }
            else if(M.equals("pop")){
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else
                    System.out.println(stack.pop());
            }
            else if(M.equals("size")){
                System.out.println(stack.size());
            }
            else if (M.equals("empty")) {
                if (stack.isEmpty()) {
                    System.out.println(1);
                }
                else {
                    System.out.println(0);
                }
            }
            else if (M.equals("top")) {
                if (stack.isEmpty()) {
                    System.out.println("-1");
                } else
                    System.out.println(stack.peek());
            }
        }
    }
}