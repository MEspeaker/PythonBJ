import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[n+1];
        if(n==0){
            System.out.println(0);
        }
        else{
            arr[0]=0;
            arr[1]=1;
            for (int i = 2; i < n+1; i++) {
                arr[i]=arr[i-1]+arr[i-2];
            }
            System.out.println(arr[n]);
        }
    }
}