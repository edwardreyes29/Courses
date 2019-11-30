// Linked List
public class LinkedListFromScratch {
    Node head; // currently null
    
    public void add(int data) {
        // LL is empty
        if (this.head == null) {
            this.head = new Node(data);
        } else {
        // LL is not empty
            // Add to front of the list, make new node head of the list
            Node nodeToAdd = new Node(data);
            nodeToAdd.next = this.head; // let previous head be next node
            this.head = nodeToAdd; // set current head be new node
            
        }
    }
    
    public static void main(String[] args) {
        LinkedListFromScratch myList = new LinkedListFromScratch();
        myList.add(10);
        myList.add(18);
        myList.add(20);
        System.out.println(myList.head.data); // 20
        System.out.println(myList.head.next.data); // 18
        System.out.println(myList.head.next.next.data); // 10
    }
}

// Node
class Node {
    int data;
    Node next;
    
    Node(int d) { this.data = d;}
}