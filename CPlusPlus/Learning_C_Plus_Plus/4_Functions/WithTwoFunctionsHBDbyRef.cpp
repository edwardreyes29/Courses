#include <iostream>

using namespace std;
void printHBD();
void printHBD();
void printHBD(string, int&);
int main() {
    int myAge;
    printHBD();
    printHBD();
    cout << "Happy Birthda dear user\n";

    cout << "\nEnter your age \n";
    cin >> myAge;
    cout << "1. My age is: " << myAge << endl;
    printHBD("Edward", myAge);
    cout << "2. My age is: " << myAge << endl;
}

void printHBD() {
    cout << "Happy Birthday to you\n";
}

void printHBD(string name, int& age) {
    cout << "Happy Birthday " << name << endl;
    age = age + 10; // changes teh value of myAge
}