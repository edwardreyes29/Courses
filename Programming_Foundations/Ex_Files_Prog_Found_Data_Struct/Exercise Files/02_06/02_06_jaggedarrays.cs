using System;

class Program
{
    static void Main()
    {
        int[][] jagged = new int[3][]; // Column number not fixed, since each array can have as many columns as it wants
        
        // Set row 0
        jagged[0] = new int[2]; // 2 is length, so indexes will be 0 & 1
        jagged[0][0] = 8;
        jagged[0][1] = 10;
        
        // Set row 1
        jagged[1] = new int[9]; // Default value is 0, so this row will have 9 zeros
        
        // Set row 2
        jagged[2] = new int[4] {20, 30, 40, 50};
        
        Console.WriteLine("At row, col 0: " + jagged[2][0]);
    }
}
