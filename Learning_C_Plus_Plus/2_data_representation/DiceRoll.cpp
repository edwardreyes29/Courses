#include <iostream>
#include <ctime>
#include <cstdlib> // c standard library for srand()
using namespace std;

int main() {
    int dice = 0;

    // seed the randomg number generator
    srand(time(0));

    dice = (rand() % 6) + 1;
    cout << "You rolled a " << dice << endl;

    return 0;
}