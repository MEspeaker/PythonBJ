import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int a= scan.nextInt();
        String b= scan.next();
        int c= Integer.parseInt(b.substring(2,3));
        int d= Integer.parseInt(b.substring(1,2));
        int e= Integer.parseInt(b.substring(0,1));
        System.out.println(a*c);
        System.out.println(a*d);
        System.out.println(a*e);
        System.out.println(a*c+a*d*10+a*e*100);
    }
}