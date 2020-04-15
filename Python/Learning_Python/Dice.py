# Dice roller simulator

import random

class Die:
    def rollDie(self):
        return random.randint(1,6)

def main():
    die1 = Die()
    die2 = Die()

    answer = 'yes'
    while(answer in ('y', 'ye', 'yes')):
        print(die1.rollDie() + die2.rollDie())
        answer = input('Do you want to roll again? ')

    print("Goodbye!")


if __name__ == "__main__":
    main()