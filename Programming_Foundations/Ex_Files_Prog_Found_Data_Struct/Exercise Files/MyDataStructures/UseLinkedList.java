import java.util.LinkedList;

public class UseLinkedList {
    public static void main(String args[]) {
        LinkedList travelBucketList = new LinkedList();
        
        // Add Items
        travelBucketList.add("(Santorini, Greece)");
        travelBucketList.addFirst("(Barcelona, Spain)");
        travelBucketList.addLast("(Tokyo, Japan)");
        travelBucketList.add(2, "(Galapagos Islands, Ecuador)");
        System.out.println(travelBucketList);
        
        // Access
        System.out.println(travelBucketList.get(2)); // use index -> extremely ineffecient
        System.out.println(travelBucketList.getFirst()); // more effecient
        // Not best datastructure to sort throught data if there is a lot of data
        
        // Search for a specific item to see if it's in the linked list
        // But computationally expensive
        System.out.println(travelBucketList.contains("(Barcelona, Spain)"));
        
        // Remove Items
        travelBucketList.removeFirst();
        travelBucketList.removeLast();
        travelBucketList.remove(1); // remove by index
        travelBucketList.remove("(Santorini, Greece)"); // remove by object
        System.out.print(travelBucketList);
    
    }
}