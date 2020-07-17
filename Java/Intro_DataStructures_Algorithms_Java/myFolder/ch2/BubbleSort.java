
/*
    Pseudo-code:

    for i = 0 to A.length - 2   // second last element
        for j = 0 to A.length - 2 - i
            if A[j] > A[j+1]
                tmp = A[j+1]
                A[j+1] = A[j]
                A[j] = tmp
*/
public class BubbleSort {
    public static void main(String[] args) {
        int[] array = {12, 8, 7, 5, 2};

        for (int i = 0; i < array.length; i++) 
            System.out.print(array[i] + " ");
        System.out.println();

        bubblesort(array);

        for (int i = 0; i < array.length; i++) 
            System.out.print(array[i] + " ");
        System.out.println();

    }

    public static void bubblesort(int[] arr) {
        int temp = 0;
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = 0; j < arr.length-1-i; j++) {
                if (arr[j] > arr[j+1]) {
                    temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
}