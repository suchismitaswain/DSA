public class SearchIn2Darray {
    public static void main(String[] args){
        int[][] arr ={
                {23,4,1},
                {18,12,3,9},
                {78,99,34,56},
                {18,12}
        };
        int target=24;
        int[] ans =search(arr,target);
        System.out.println(search(arr,target));
    }

    static int search(int[][] arr,int target){
        int max= Integer.MIN_VALUE;
        for (int row =0;row <arr.length; row++){
            for (int col =0; col <arr[row].lengh; col++){
                if (arr[row][col ==target]){
                    max =arr[row][col];
                }
            }
        }
        return max;
    }
}
