import java.util.Scanner;

public class Input {
    public static void main(String [] args){
        Scanner in =new Scanner(System.in);
        int[] arr = new int[5];
        arr[0] =23;
        arr[1] = 45;
        arr[2]= 233;
        arr[3]=543;
        arr[4]=3;
        System.out.println(arr[3]);

        for (int i=0; i<arr.length; i++){
            arr[i] =in.nextInt();
        }
        System.out.println(Arrays.toString(arr));
    //     
    // for (int i=0;i<arr.length; i++){
    //         System.out.println(arr[i] + " ");
    //     }

    //     for (int num :arr){
    //         System.out.println(num + " ");
    //     }
    //  System.out.println(arr[  ]);

        String[] str =new String[4];
        for(int i=0; i< str.length; i++){
            str[i] =in.next();
        }

        System.out.println(Arrays.toString(str));
    }
}
