//import java.util.Scanner

public class Reverse {
    public static void main(String[] args) {
        //Scanner in = new Scanner(System.in);
        int num= 28479;
        int ans =0;
        int rem=0;

        while (num>0) {
            rem = num %10;
            num /=10;

            ans=ans *10+ rem;
        }
        System.out.println(ans);
    }
}
