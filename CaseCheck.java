import java.util.Scanner;

public class CaseCheck {
    public static void main(String [] args){
        Scanner in =new Scanner (System.in);
        char ch = in.next().trim().charAt(0);
            // .trim removes extra space
        //System.out.println(in.next().trim());


        // String word ="hello";
        // System.out.println(word.charAt(2));

        //System.out.println(ch);

        
        if(ch >='a' && ch <='z'){
            System.out.println("Lowercase");
        } else{
            System.out.println("Uppercase");
        }
        

        
    }
}
