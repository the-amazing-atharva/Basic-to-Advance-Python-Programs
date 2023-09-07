def rpsWinner(move1, move2):
    # Check all six possible combinations with a winner and return it:
    if move1 == 'rock' and move2 == 'paper':
        return 'player two'
    elif move1 == 'rock' and move2 == 'scissors':
        return 'player one'
    elif move1 == 'paper' and move2 == 'scissors':
        return 'player two'
    elif move1 == 'paper' and move2 == 'rock':
        return 'player one'
    elif move1 == 'scissors' and move2 == 'rock':
        return 'player two'
    elif move1 == 'scissors' and move2 == 'paper':
        return 'player one'
    # For all other combinations, it is a tie:
    else:
        return 'tie'
