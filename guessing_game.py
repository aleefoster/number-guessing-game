import os
import random


def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


def get_random_number():
    random_number = random.randrange(1, 100)
    return random_number    


def start_game(game_number, high_score):
    clear_screen()
    playing = True
    random_number = get_random_number()
    guess_number = 1
    
    if game_number > 1:
        print("Current high score: {}".format(high_score))
    print("Enter a number between 1 and 100.")
    while playing:
        guess = input("Guess #{}:  ".format(guess_number))
        guess_number += 1
        if guess.upper() == "QUIT":
            print("Thanks for playing!")
            break
        elif int(guess) < 1 or int(guess) > 100:
            print("Your guess is out of range, try again!")
        elif int(guess) > random_number:
            print("Your guess is too high, try again!")
        elif int(guess) < random_number:
            print("Your guess is too low, try again!")
        elif int(guess) == random_number:
            print("Congratulations!  You guessed the number in {} tries!".format(guess_number))
            if game_number == 1:
                high_score = guess_number
            else:
                if guess_number < high_score:
                    print("You beat the high score! Good job!")
                    high_score = guess_number    
            game_number += 1
            playing = False
            
    else:
        if input("Play again? (y/n)  ").lower() != 'n':
            start_game(game_number, high_score)
        else:
            print("Thanks for playing!")


if __name__ == '__main__':
    clear_screen()        
    print("Welcome to Guess the Number!")
    print("To play, enter a number between 1 and 100. Try to guess the number in as few attempts as possible! Have fun!")
    input("Press return to start!")
    clear_screen()
    game_number = 1
    high_score = 0
    start_game(game_number, high_score)
 