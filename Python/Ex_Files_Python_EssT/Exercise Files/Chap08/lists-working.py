#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # print_list(game)
    # print(game[1]) # returns 2nd item
    # print_list(game[1:3]) # returns 2nd and 3d item, not including 4th
    # print_list(game[1:5:2]) # Every second item ending at 5
    # i = game.index('Paper')
    # print(i)

    # game.append('Computer') # appends to end of list
    # print_list(game)

    # # insert to a particular index
    # game.insert(2, 'Bazookah')
    # print_list(game)

    # # remove item by value
    # game.remove('Bazookah')
    # print_list(game)

    # # return and remove item at end of list, simulate a stack
    # x = game.pop()
    # print(x)
    # print_list(game)

    # # return and remove item at a particular index
    # x = game.pop(3)
    # print(x)
    # print_list(game)

    # # to remove an index using del metod
    # del game[3]
    # print_list(game)

    # # remove items with a slice
    # del game[0:2] # removes first two, should only be 'Scissors' left
    # print_list(game)

    # join a list
    game = [ 'Rock', 'Paper', 'Scissors']
    print(','.join(game)) # -> Rock,Paper,Scissors
    print('/'.join(game)) # -> Rock/Paper/Scissor
    print_list(game)

    # length of list
    print(len(game)) 
    game.append('Bazookah')
    # Tuple
    game = ( 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    # game.append('Bazookah') # tuple object has no attribute 'append'
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
