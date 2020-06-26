#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX_CHIPS = 100;
const float MAX_TURN = .5;
int main() {
    // This variable keeps track of whose turn it is. We can name it
    // player1Turn, then when it's true, it's play 1's turn, whent it's false
    // it's, player 2's turn
    bool player1Turn = true;
    bool gameOver = false; // declare a boolean variable for gameOver to determine when the game is done
    int chipsInPile = 0;
    int chipsTaken = 0;
    int maxPerTurn = 0;
    char userChoice;

    //ask th players for their names, then store in an array
    string playerName[2];
    cout << "Player 1, please enter your name: \n";
    cin >> playerName[0];
    cout << "Player 2, please enter your name: \n";
    cin >> playerName[1];


    // seed the random number generator
    srand(time(0));

    do {
        gameOver = false;
        // start game with random number of chiprs in the pile.
        chipsInPile = (rand() % MAX_CHIPS ) + 1; // pile of chips between 1 and 100
        cout << "This round will start with " << chipsInPile << " chips in the pile\n";

        while (gameOver == false) {
            do {
                maxPerTurn = static_cast<int>(chipsInPile * MAX_TURN);
                if (player1Turn) {
                cout << playerName[0] << " How many chips would you like?\n";
                }
                else {
                    cout << playerName[1] << " How many chips would you like?\n";
                }
                cout << "You can only take ";
                if (maxPerTurn == 0) {
                    cout << " 1\n";
                } 
                else {
                    cout << maxPerTurn << endl;
                }
                // chipsTaken = (rand() % maxPerTurn) + 2;
                cin >> chipsTaken;
            } while ((chipsTaken > maxPerTurn) && (chipsInPile > 1));

            chipsInPile = chipsInPile - chipsTaken;
            cout << "There are " << chipsInPile << " left in the pile\n";

            if (chipsInPile == 0){
                gameOver = true;
                if (player1Turn) {
                    cout << playerName[1] << ", congratulations you won\n";
                } 
                else {
                    cout << playerName[0] << " How many chips would you like?\n";
                }
            } else {
                player1Turn = !player1Turn;
            }
        }
        cout << "Do you wish to play again? (Y\\N)\n";
        cin >> userChoice;
    } while ((userChoice == 'y') || (userChoice == 'Y'));
    return 0;
}