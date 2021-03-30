import tkinter
import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0

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
            move = computerActions()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_singleplayer(move[0], move[1], b, l1, l2)


def computerActions():
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
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]


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
        if (i.count(' ') > 0):
            flag = False
    return flag


def start():
    menu = Tk()
    menu.title("Tic Tac Toe")
    single = partial(singlePlayer, menu)
    multi = partial(multiPlayer, menu)

    head = Button(menu, text="-- Welcome! Select a game mode! --",
                  activeforeground='grey',
                  activebackground='white', bg='grey',
                  fg='grey', width=50, font='ariel', bd=5)
    singleButton = Button(menu, text="Single Player", command=single,
                          activeforeground='red',
                          activebackground="yellow", bg="red",
                          fg="yellow", width=50, font='summer', bd=5)
    multiButton = Button(menu, text="Multi Player", command=multi, activeforeground='red',
                         activebackground="yellow", bg="red", fg="yellow",
                         width=50, font='summer', bd=5)
    exitButton = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                        activebackground="yellow", bg="red", fg="yellow",
                        width=50, font='summer', bd=5)
    head.pack(side='top')
    singleButton.pack(side='top')
    multiButton.pack(side='top')
    exitButton.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    start()
