import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String M = scan.next();
        int intM = Integer.parseInt(M);
        int N=0;
        for (int i=intM-9*M.length(); i<intM; i++){
            int number= i;
            int sum= 0;
            while(number>0){
                sum+=number%10;
                number/=10;
            }
            if((sum+i)==intM){
                N=i;
                break;
            }
        }
        System.out.println(N);
    }
}