import java.util.Scanner;

public class Largest {
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        //Find largest number
        //int max= a;
        // if (b>max){
        //     max =b;
        // }
        // if (c>max){
        //     max =c;
        // }
        //System.out.println("The largest number is :" + max);
    

        // int max = 0;

        // if (a>b){
        //     max=a;
        // } else{
        //     max=b;
        // }
        // if (c>max){
        //     max=c;
        // }
        //System.out.println("The largest number is :" + max);
    

        //int max=Math.max(c, Math.max(a,b));
        System.out.println(Math.max(34,57));
    }
        
}
