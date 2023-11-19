def rps(p1, p2):
    first_scenario = 'Player 1 won!'
    second_scenario = 'Player 2 won!' 
    draw_scenario = 'Draw!'
    if p1 == p2:
        return draw_scenario
    elif p1 == 'scissors' and p2 == 'paper' or p1 == 'paper' and p2 == 'rock' or p1 == 'rock' and p2 == 'scissors':
        return first_scenario
    else:
        return second_scenario
