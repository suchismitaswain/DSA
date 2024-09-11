import java.util.Scanner;

public class Loop2 {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        //for (int num =1; num<=5; num+=2){
            //     System.out.println(num);
            // }

        
        int num=1;
        while (num<=5) {
            System.out.println(num);
            num += 1;
        }

        //do while
        /* 
        do{

        } while(condition);

        */

        int n=1;
        do{
            System.out.println(n);
            n++;
        } while (n <=5);

    }
}
