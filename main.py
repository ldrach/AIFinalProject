import tkinter
import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0
player, opponent = 'x', 'o'
global board
board = [[" " for x in range(3)] for y in range(3)]


def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))


def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):

        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10

    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10

    # Else if none of them have won then return 0
    return 0


def isMovesLeft(b):
    for i in range(3):
        for j in range(3):
            if (b[i][j] == '_'):
                return True
    return False


def gameboard_single(b, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_singleplayer, i, j, b, l1, l2)
            button[i][j] = Button(
                b, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    b.mainloop()


def singlePlayer(b):
    b.destroy()
    b = Tk()
    b.title("Tic Tac Toe")
    l1 = Button(b, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(b, text="Computer : O",
                width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_single(b, l1, l2)


def get_text_singleplayer(i, j, b, l1, l2):
    global sign

    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        b.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        b.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif isfull():
        b.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if x:
        if sign % 2 != 0:
            move = computerActions(board)
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_singleplayer(move[0], move[1], b, l1, l2)


def computerActions(b):
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if not possiblemove:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i

        bestMove = findBestMove(b)
        move = [bestMove[0], bestMove[1]]
        return move


def multiPlayer(b):
    b.destroy()
    b = Tk()
    b.title("Tic Tac Toe")
    l1 = Button(b, text="Player 1 : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(b, text="Player 2 : O",
                width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_multi(b, l1, l2)


def gameboard_multi(b, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_multiplayer, i, j, b, l1, l2)
            button[i][j] = Button(
                b, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    b.mainloop()


def get_text_multiplayer(i, j, b, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        b.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        b.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif isfull():
        b.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")


# Check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "


# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if (i.count(" ") > 0):
            flag = False
    return flag


def minimax(b, depth, isMax):
    score = evaluate(board)

    # If Maximizer has won the game return his/her
    # evaluated score
    if score == 10:
        return score

    # If Minimizer has won the game return his/her
    # evaluated score
    if score == -10:
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if isfull():
        return 0

    # If this maximizer's move
    if isMax:
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if b[i][j] == ' ':
                    # Make the move
                    b[i][j] = player

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(b,
                                             depth + 1,
                                             not isMax))

                    # Undo the move
                    b[i][j] = ' '
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if b[i][j] == ' ':
                    # Make the move
                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))

                    # Undo the move
                    board[i][j] = ' '
        return best


def findBestMove(b):
    bestVal = -1000
    bestMove = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if b[i][j] == ' ':

                # Make the move
                b[i][j] = player

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False)

                # Undo the move
                board[i][j] = ' '

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


def start():
    menu = Tk()
    menu.title("Tic Tac Toe")
    single = partial(singlePlayer, menu)
    multi = partial(multiPlayer, menu)

    head = Button(menu, text="-- Welcome! Select a game mode! --",
                  activeforeground='black',
                  activebackground='white', bg='black',
                  fg='white', width=30, font='ariel', bd=5)
    singleButton = Button(menu, text="Single Player", command=single,
                          activeforeground='blue',
                          activebackground="white", bg="blue",
                          fg="white", width=30, font='ariel', bd=5)
    multiButton = Button(menu, text="MultiPlayer", command=multi, activeforeground='blue',
                         activebackground="white", bg="blue", fg="white",
                         width=30, font='ariel', bd=5)
    exitButton = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                        activebackground="yellow", bg="red", fg="yellow",
                        width=30, font='ariel', bd=5)
    head.pack(side='top')
    singleButton.pack(side='top')
    multiButton.pack(side='top')
    exitButton.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    start()
