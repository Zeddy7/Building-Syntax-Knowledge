import random
choices = ('rock', 'paper', 'scissors')

def computer_choice():
    return random.choice(choices)

def play_game():
    tries = 0
    while tries < 3:
        computer = computer_choice() 
        ask = input('\nRock, paper, scissors: ').lower()
        

        if ask not in choices:
            print('\nInvalid')
        else:
            print('\nComputer chose:', computer)
            if (ask == 'rock' and computer == 'scissors') or (ask == 'paper' and computer == 'rock') or (ask == 'scissors' and computer == 'paper'):
                print('You won!')
            elif ask == computer:
                print('Tie')
            else:
                print('You lose')
            tries += 1

def main():
    while True:
        play_game()

        ask_again = input('\n\nDo you want to continue (y/n)? ')
        if ask_again == 'y':
            continue
        else:
            print('Thanks for playing!')
            break

main()