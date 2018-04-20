# coding: iso-8859-1
'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

-Rock beats scissors
-Scissors beats paper
-Paper beats rock
'''

while True:
    p1 = input("player1 -> ")
    p2 = input("player2 -> ")
    if p1 == "scissors" and p2 == "rock" :
        print("player 1 loses and player 2 wins")
    elif p1 == "paper" and p2 == "scissors" :
        print("player 1 loses and player 2 wins")
    elif p1 == "rock" and p2 == "paper" :
        print("player 1 loses and player 2 wins")
        break
    elif p2 == "scissors" and p1 == "rock" :
        print("player 1 loses and player 2 wins")
    elif p2 == "paper" and p1 == "scissors" :
        print("player 1 loses and player 2 wins")
    elif p2 == "rock" and p1 == "paper" :
        print("player 1 wins and player 2 looses")
        break
    elif p1 == "quit" or p2 == "quit":
        break 
    