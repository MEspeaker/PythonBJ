import java.util.*;

public class Main {
    public static void main(String[]args){
        HashSet<String> set = new HashSet<>();
        Scanner scan= new Scanner(System.in);
        int N= scan.nextInt();
        int M= scan.nextInt();
        for (int i = 0; i < N; i++) {
            set.add(scan.next());
        }
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String qheh = scan.next();
            if(set.contains(qheh)){
                result.add(qheh);
            }
        }
        Collections.sort(result);
        System.out.println(result.size());
        for (String s : result) {
            System.out.println(s);
        }
    }
}