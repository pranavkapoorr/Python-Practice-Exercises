# coding: iso-8859-1
'''
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, 
this is significantly more than half an hour of coding, so we’re doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
Here are some more examples to work with:
winner_is_2 = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
winner_is_1 = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0],
    [2, 1, 0],
    [2, 1, 1]]
no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]
also_no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 0]]
'''
def checkWinner(listX):
    l1 = listX[0]
    l2 = listX[1]
    l3 = listX[2]
    if l1[0] == l2[1] and l1[0] == l3[2] or l1[0] == l2[0] and l1[0] == l3[0] or l1[0] == l1[1] and l1[0] == l1[2]:
        return l1[0]
    elif l1[1] == l2[1] and l1[1] == l3[1]:
        return l1[1]
    elif l1[2] == l1[1] and l1[2] == l1[0] or l1[2] == l2[2] and l1[2] == l3[2] or l1[2] == l2[1] and l1[2] == l3[0]:
        return l1[2]

listX = [[1, 2, 0],
         [2, 1, 0],
         [2, 1, 0]]
print("the winner is: " + str(checkWinner(listX)))
    