import java.util.Scanner;

public class Switch {
    public static void main( String [] args){
        Scanner in = new Scanner(System.in);
        String fruit =in.next();

//         if (fruit.equals("mango"){
// `           // we can use .equals instend of == 
//             System.out.println("King of fruit");
//         } 
        
//         if (fruit.equals("apple")){
//             System.out.println("a sweet red fruit");
//         }


        switch (fruit) {
            case "Mango":
                System.out.println("King of fruits");
                break;
            case "Apple":
                System.out.println("sweet fruit");
                break;
            case "Orange":
                System.out.println("round fruits");
                break;
            case "Grapes":
                System.out.println("small fruits");
                break;
            default:
                System.out.println("Please enter a valid fruit : ");
        }
    }
}
