import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int N= scan.nextInt();
        long value=1;
        if(N==0)
            System.out.println(1);
        else{
            for(int i=1;i<=N;i++){
                value*=i;
            }
            System.out.println(value);
        }

    }
}