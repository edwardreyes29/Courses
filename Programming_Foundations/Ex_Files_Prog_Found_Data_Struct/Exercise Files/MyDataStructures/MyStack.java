import java.util.Stack;
public class MyStack {
    public static void main(String[] args) {
        Stack myStack = new Stack();
        myStack.push("hi");
        myStack.pop();
        myStack.pop(); // produced error
    }
}