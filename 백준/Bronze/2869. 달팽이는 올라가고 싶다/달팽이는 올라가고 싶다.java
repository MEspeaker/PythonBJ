import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int a= scan.nextInt();
        int b= scan.nextInt();
        int v= scan.nextInt();
        if(v<a)
            System.out.println(1);
        else{
            int value=(v-a)%(a-b);
            if(value==0)
                System.out.println((v-a)/(a-b)+1);
            else
                System.out.println((v-a)/(a-b)+2);
        }
    }
}