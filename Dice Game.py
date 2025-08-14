import random

# Roll the dice and return a number between 1 and 6
def roll():
    return random.randint(1, 6)

# Ask how many players, get their names, and initialize their scores
def game_players():
    while True:
        players_str = input('How many players (2 - 4)? ')
        if players_str.isdigit():
            players = int(players_str)
            if 2 <= players <= 4:
                break
            else:
                print('\nNumber of players must be between 2 and 4')
        else:
            print('Invalid input, please enter a number')
            
    players_scores = {}
    for number in range(players):
        names = input(f'Enter player {number+1} name: ')
        players_scores[names] = 0
        
    return players_scores
    
def play_game(player, player_total):
    round_score = 0
    
    print(f"\nThis is {player}'s turn")
    print(f'Your total score is: {player_total}')
    
    while True:
        
        ask = input('\nRoll the dice (y/n)? ').lower()
        
        if ask != 'y':
            break
        else:
            value = roll()
            if value == 1:
                round_score = 0
                print('You rolled a 1, you lose all round points')
                break
            else:
                round_score += value
                print(f'\nYou rolled a {value}')
                print(f'Your total round points so far: {round_score}')
    
    return player_total + round_score
    
def multiply_players():
    total = 15
    players_scores = game_players()
    
    while True:
        for name in players_scores:
            players_scores[name] = play_game(name, players_scores[name])
            print('Your total score after this round:', players_scores[name])
            
            if players_scores[name] >= total:
                print(f'\n{name} won with a total score of {players_scores[name]}')
                return
    
def main():
    while True:
        multiply_players()
        play_again = input('\n\nDo you want to play again (y/n)? ') 
        if play_again != 'y':
            print('\nThanks for playing!')
            break
        else:
            continue

if __name__ == '__main__':
    main()