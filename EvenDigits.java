public class EvenDigits {
    public  static void main(String [] args){
        int[] nums ={12,345,2,6,7896};
    }
    static int findNumbers(int[]nums){
        int count =0;
        for (int num : nums){
            if (even(num)){
                count++;
            }
        }
        return count;
    }
    
}
