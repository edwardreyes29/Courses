# Guess the Number
import random

def main():
    number = random.randint(1,10)

    guess = 0
    print("Guess the number!")
    while (guess != number):
        guess = input("Pick a number from 1 to 10: ")
        guess = int(guess)
        if(guess == number):
            print("You guessed right!")
            break
        else:
            if (guess > number):
                print("The number is too high")
            else:
                print("The number is too low")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()