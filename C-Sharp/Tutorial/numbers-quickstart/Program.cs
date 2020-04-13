using System;

namespace NumbersInCSharp
{
    class Program
    {
        static void WorkingWithInteger() {
            int a = 18;
            int b = 6;

            // addition
            int c = a + b;
            Console.WriteLine(c);

            // subtraction
            c = a - b;
            Console.WriteLine(c);

            // division
            c = a / b;
            Console.WriteLine(c);

        }

        static void OrderPrecedence()
        {
            int a = 5;
            int b = 4;
            int c = 2;
            int d = a + b * c;
            Console.WriteLine(d);
        }
        static void Main(string[] args)
        {
            WorkingWithInteger();
            OrderPrecedence();
        }
    }
}
