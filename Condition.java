public class Condition {
    public static void main(String[]args){

    int salary= 24000;
    // if (salary >10000){
    //     salary =salary +20000;
    //     }
    // else{
    //     salary= salary +1000;
    //     }


    //  Multiple if-else
    if (salary>10000){
        salary += 2000;
    } else if(salary >20000) {
        salary +=3000;
    } else{
        salary += 1000;
    }
    System.out.println(salary);
    }

}
