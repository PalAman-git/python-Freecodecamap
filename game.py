import random


def get_choices():# for getting the choices
    player_choice = input("Enter a choice (rock,paper,scissors): ")

    options = ['rock','paper','scissors'];
    computer_choice = random.choice(options);

    choices = { 'player':player_choice,'computer':computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player} and computer chose {computer}")

    if player == computer:
        return "it's a tie!"
    
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock Smashes scissors! You win!'
        else:
            return 'Paper covers rock! You lose.'
    
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper Covers the rock! You win!'
        else:
            return 'Scissors cut down the paper! You lose.'
    
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cut down the paper! You win!'
        else:
            return 'Rock smashes the paper! You lose.'


choices = get_choices();
result = check_win(choices['player'],choices['computer'])

print(result)