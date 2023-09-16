## Game of Hog CS61 Project

In Hog, two players alternate turns trying to reach 100 points first. <br>
On each turn, the current player chooses some number of dice to roll, up to 10. <br>
His/Her turn score is the sum of the dice outcomes, <br>
unless any of the dice come up a 1, in which case the score for his/her turn is only 1 point (the Pig out rule). <br>

## Special Rules

1. Free bacon: If a player chooses to roll zero dice, he/she scores one more than the largest digit in her opponent's score.
    Player 1 has 42, Player 0 gains 1 + max(4, 2) = 5 points <br>
2. Hog wild: If the sum of both players' total scores is a multiple of seven (e.g., 14, 21, 35), <br>
    then the current player rolls four-sided dice instead of the usual six-sided dice. <br>
3. Swine swap: If at the end of a turn one of the player's total score is exactly double the other's, <br>
    then the players swap total scores. 


