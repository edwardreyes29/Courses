// Hello World Remix
/* By Edward Reyes */
// iostream used for inputting and outputting
#include <iostream>
using namespace std;

int main() {
    string name;
    string food;
    
    cout << "Please enter your name: " << endl;
    cin >> name;
    cout << "What is your favorite food? " << endl;
    cin >> food;
    cout << "Hello, " << name << ", your favorite food is " << food;
    return 0;
}