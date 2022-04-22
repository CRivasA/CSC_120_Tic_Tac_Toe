# ----------------------------------------------------------------
# Carlos Rivas
# 04/18/2021.#
# ----------------------------------------------------------------
# CSC120 - Lab 09
# 2 PLayer Tic-Tac-Toe.
# -----------------------------------------------------------------
from tkinter import *
from board import Tic
from check_win import check_Win
from winner import Winner
import sqlite3

#Main function
def main():
    status = 'go'
    conn = sqlite3.connect('gamedb.sqlite')
    cur = conn.cursor()
     # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Game;
    CREATE TABLE Game(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Player1  INTEGER,
    Player2  INTEGER
);
    ''')
    conn.commit()

    while status == 'go':
        p1_list = []
        p2_list = []
        pwinner = None
        stt = stt1 = stt2 = stt3 = stt4 = stt5 = stt6 = stt7 = stt8 = stt9 = ACTIVE
        value1 = value2 = value3 = value4 = value5 = value6 = value7 = value8 = value9 = ' '
        for i in range(9):
            player = str((i%2)+1)
            print ('play', player)
            main = str(Tic(player, pwinner, stt, stt1, value1, stt2, value2, stt3, value3, stt4, value4, stt5, value5, stt6, value6,
                     stt7, value7, stt8, value8, stt9, value9))
            if main == 'stop':
                status = 'stop'
                break
            elif main == 'c1' and player == '1':
                stt1 = DISABLED
                value1 = 'X'
            elif main == 'c1' and player == '2':
                stt1 = DISABLED
                value1 = 'O'
            elif main == 'c2'and player == '1':
                stt2 = DISABLED
                value2 = 'X'
            elif main == 'c2' and player == '2':
                stt2 = DISABLED
                value2 = 'O'
            elif main == 'c3' and player == '1':
                stt3 = DISABLED
                value3 = 'X'
            elif main == 'c3' and player == '2':
                stt3 = DISABLED
                value3 = 'O'
            elif main == 'c4'and player == '1':
                stt4 = DISABLED
                value4 = 'X'
            elif main == 'c4' and player == '2':
                stt4 = DISABLED
                value4 = 'O'
            elif main == 'c5' and player == '1':
                stt5 = DISABLED
                value5 = 'X'
            elif main == 'c5' and player == '2':
                stt5 = DISABLED
                value5 = 'O'
            elif main == 'c6' and player == '1':
                stt6 = DISABLED
                value6 = 'X'
            elif main == 'c6' and player == '2':
                stt6 = DISABLED
                value6 = 'O'
            elif main == 'c7' and player == '1':
                stt7 = DISABLED
                value7 = 'X'
            elif main == 'c7' and player == '2':
                stt7 = DISABLED
                value7 = 'O'
            elif main == 'c8' and player == '1':
                stt8 = DISABLED
                value8 = 'X'
            elif main == 'c8' and player == '2':
                stt8 = DISABLED
                value8 = 'O'
            elif main == 'c9' and player == '1':
                stt9 = DISABLED
                value9 = 'X'
            elif main == 'c9' and player == '2':
                stt9 = DISABLED
                value9 = 'O'
            print(main, value1)
            if player == '1':
                p1_list.append(main)
            else:
                p2_list.append(main)

            win=str(check_Win(p1_list, p2_list))
            print(win, 'P1:', p1_list, '&', 'P2:', p2_list)
            if win == 'Player 1 wins':
                pwinner = 'Player 1 wins!'
                status = str(Winner(pwinner))
                break
            elif win == 'Player 2 wins':
                pwinner = 'Player 2 wins!'
                Winner(pwinner)
                status = str(Winner(pwinner))
                break
            print('cont', i)
            if i == 8:
                pwinner = 'Draw!'
                Winner(pwinner)
                status = str(Winner(pwinner))
                break


main()




