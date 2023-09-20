"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

# Taking turns

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    total = 0
    i = 0
    roll_is_one = False
    while i < num_rolls:
        dice_roll = dice()
        if dice_roll == 1:
            roll_is_one = True
        else:
            total += dice_roll
        i += 1
    if roll_is_one == True:
        return 1
    else:
        return total

# free_bacon If a player chooses to roll zero dice, 
# she scores one more than the largest digit in her opponent's score.
def free_bacon(player_score):
    if player_score < 10:
        return player_score + 1
    
    player_score_str = str(player_score)
    digit_one = int(player_score_str[0])
    digit_two = int(player_score_str[1])
    
    bacon_score = max(digit_one, digit_two) + 1
    return bacon_score

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
        

# Playing a game

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).

    >>> select_dice(4, 24) == four_sided
    True
    >>> select_dice(16, 64) == six_sided
    True
    >>> select_dice(0, 0) == four_sided
    True
    """
    "*** YOUR CODE HERE ***"
    sum = score + opponent_score
    if sum % 7 == 0:
        return four_sided
    else:
        return six_sided

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def swine_swap(score, opponent_score):
    if score - opponent_score == opponent_score or opponent_score - score == score:
        temp = score
        score = opponent_score
        opponent_score = temp
        return score, opponent_score 
    else:
        return score, opponent_score
   

def play(strategy0, strategy1, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    score, opponent_score = 0, 0
    "*** YOUR CODE HERE ***"
    while score < goal and opponent_score < goal:
        # player 1's turn
        if who == 0:
            dice = select_dice(score, opponent_score)
            dice_roll_sum = take_turn(strategy0(score, opponent_score), opponent_score, dice)
            score += dice_roll_sum
            score, opponent_score = swine_swap(score, opponent_score)
            who = other(who)
        # player 2's turn
        else:
            dice = select_dice(score, opponent_score)
            dice_roll_sum = take_turn(strategy1(opponent_score, score), score, dice)
            opponent_score += dice_roll_sum
            score, opponent_score = swine_swap(score, opponent_score)
            who = other(who)

        
    return score, opponent_score  # You may wish to change this line.

#######################
# Phase 2: Strategies #
#######################

# Basic Strategy

BASELINE_NUM_ROLLS = 5
BACON_MARGIN = 8

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """ 
    "*** YOUR CODE HERE ***"
    def make_averaged_args(*args):
        total = 0
        i = 0
        while i < num_samples:
            total += fn(*args)
            i += 1
        return total / num_samples
    return make_averaged_args


def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    1 dice scores 3.0 on average
    2 dice scores 6.0 on average
    3 dice scores 9.0 on average
    4 dice scores 12.0 on average
    5 dice scores 15.0 on average
    6 dice scores 18.0 on average
    7 dice scores 21.0 on average
    8 dice scores 24.0 on average
    9 dice scores 27.0 on average
    10 dice scores 30.0 on average
    10
    """
    "*** YOUR CODE HERE ***"
    i = 1
    max_score_i = 0
    while i <= 10:
        make_averaged_dice = make_averaged(roll_dice, num_samples = 1000)
        average_score = make_averaged_dice(i, dice)
        print(i, "dice scores", average_score, "on average")
        if average_score > max_score_i:
            max_score_i = i
        i += 1
    return max_score_i

    
    

        


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(BASELINE_NUM_ROLLS)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(5) win rate:', average_win_rate(always_roll(5)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score):
    """This strategy rolls 0 dice if that gives at least BACON_MARGIN points,
    and rolls BASELINE_NUM_ROLLS otherwise.

    >>> bacon_strategy(0, 0)
    5
    >>> bacon_strategy(70, 50)
    5
    >>> bacon_strategy(50, 70)
    0
    """
    "*** YOUR CODE HERE ***"
    # BASELINE_NUM_ROLLS = 5
    # BACON_MARGIN = 8
    if free_bacon(opponent_score) >= BACON_MARGIN:
        return 0
    else:
        return BASELINE_NUM_ROLLS 
    
def swap_score(score, opponent_score):
    return opponent_score, score

def is_swappable(score, opponent_score):
    if opponent_score // score == 2:
        return True
    else:
        return False

def swap_strategy(score, opponent_score):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls BASELINE_NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least BACON_MARGIN points and rolls
    BASELINE_NUM_ROLLS otherwise.

    >>> swap_strategy(23, 60) # 23 + (1 + max(6, 0)) = 30: Beneficial swap
    0
    >>> swap_strategy(27, 18) # 27 + (1 + max(1, 8)) = 36: Harmful swap
    5
    >>> swap_strategy(50, 80) # (1 + max(8, 0)) = 9: Lots of free bacon
    0
    >>> swap_strategy(12, 12) # Baseline
    5
    """
    "*** YOUR CODE HERE ***"
    # adding max(opponent_score)
    # rolling 0 dice may result in a harmful swine_swap
    score += free_bacon(opponent_score)
    if is_swappable(score, opponent_score) == True and score < opponent_score:
        return 0
    elif score - opponent_score == opponent_score:
        return BASELINE_NUM_ROLLS
    elif free_bacon(opponent_score) >= BACON_MARGIN:
        return 0
    else:
        return BASELINE_NUM_ROLLS
    


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** at the start of the game we want to roll fairly high dices to try and get a lead
        if our opponent starts to get a lead on us we want to roll 5's to lower risk but hopefully catch up

        if opponent_score is at least greater than double our score
        we want to apply swap strategy to hopefully swap

        when our score is fairly high, say, greater than 60 and apply bacon strategy, 
        except the higher our score the less BASELINE_NUM_ROLLS

        do some checks if we are in a great score deficit, apply swap strategy to
        help get us out of it

        the higher score we get, the less risky we want to approach ours rolls
        # if we are in a lead by a multiple of 2
        # need to watch out for swaps
        # attempt fair sized rolls
        # decrease as we have a higher score

    ***
    """
    "*** YOUR CODE HERE ***"
    dice = select_dice(score, opponent_score)

    if score < 10 and opponent_score < 10:
        return 6 
    elif score < 20 and opponent_score > score and opponent_score >= 40:
        if opponent_score > (score * 2):
            return swap_strategy(score, opponent_score)
        if opponent_score > (score * 2) and dice == four_sided:
            return bacon_strategy(score, opponent_score)
        if dice == four_sided:
            return swap_strategy(score, opponent_score)
        return 8 
    elif opponent_score > (score * 2):
        return swap_strategy(score, opponent_score)
    elif score > 60: 
        if score > 70:
            if score > 80:
                if score > 90:
                    if bacon_strategy(score, opponent_score) == 5:
                        return 3 
                    else:
                        return 0
            if bacon_strategy(score, opponent_score) == 5:
                return 4 
            else:
                return 0 
        if bacon_strategy(score, opponent_score) == 5 and dice == six_sided:
            return 8 
        else:
            return 0
    elif score > (opponent_score * 2):
        if score >= 50:
            if score > 60:
                if score > 70:
                    return 4
                return 5
            return 6 
        elif score < 50:
            return 8 
    elif dice == four_sided and score > opponent_score:
        return bacon_strategy(score, opponent_score)
    elif dice == four_sided and score < opponent_score:
        return swap_strategy(score, opponent_score)
    else:
        return 8 


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.

def get_int(prompt, min):
    """Return an integer greater than or equal to MIN, given by the user."""
    choice = input(prompt)
    while not choice.isnumeric() or int(choice) < min:
        print('Please enter an integer greater than or equal to', min)
        choice = input(prompt)
    return int(choice)

def interactive_dice():
    """A dice where the outcomes are provided by the user."""
    return get_int('Result of dice roll: ', 1)

def make_interactive_strategy(player):
    """Return a strategy for which the user provides the number of rolls."""
    prompt = 'Number of rolls for Player {0}: '.format(player)
    def interactive_strategy(score, opp_score):
        if player == 1:
            score, opp_score = opp_score, score
        print(score, 'vs.', opp_score)
        choice = get_int(prompt, 0)
        return choice
    return interactive_strategy

def roll_dice_interactive():
    """Interactively call roll_dice."""
    num_rolls = get_int('Number of rolls: ', 1)
    turn_total = roll_dice(num_rolls, interactive_dice)
    print('Turn total:', turn_total)

def take_turn_interactive():
    """Interactively call take_turn."""
    num_rolls = get_int('Number of rolls: ', 0)
    opp_score = get_int('Opponent score: ', 0)
    turn_total = take_turn(num_rolls, opp_score, interactive_dice)
    print('Turn total:', turn_total)

def play_interactive():
    """Interactively call play."""
    strategy0 = make_interactive_strategy(0)
    strategy1 = make_interactive_strategy(1)
    score0, score1 = play(strategy0, strategy1)
    print('Final scores:', score0, 'to', score1)

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--interactive', '-i', type=str,
                        help='Run interactive tests for the specified question')
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.interactive:
        test = args.interactive + '_interactive'
        if test not in globals():
            print('To use the -i option, please choose one of these:')
            print('\troll_dice', '\ttake_turn', '\tplay', sep='\n')
            exit(1)
        try:
            globals()[test]()
        except (KeyboardInterrupt, EOFError):
            print('\nQuitting interactive test')
            exit(0)
    elif args.run_experiments:
        run_experiments()
