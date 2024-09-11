import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String []args){

        ArrayList<Integer> list = new ArrayList<>(iitialCapacity:5);
        
        list.add(67);
        list.add(234);
        list.add(654);
        list.add(43);
        list.add(654);
        list.add(8765);
        
        System.out.println(list);
        list.set(0,99);
        list.remove(2);

        System.out.println(list);
    }
}
