# ----------------------------------------------------------------
# Carlos Rivas
# 04/18/2021.#
# ----------------------------------------------------------------
# CSC120 - Lab 09
# 2 PLayer Tic-Tac-Toe.
# -----------------------------------------------------------------
import sqlite3

#Data base Class
class Db:
    # init function and GUI
    def __init__(self, pwinner):
        self.pwinner = pwinner
        print('db status', self.pwinner)
        conn = sqlite3.connect('gamedb.sqlite')
        cur = conn.cursor()
        # Make some fresh tables using executescript()

        if self.pwinner == 'Player 1 wins!':
            p1 = 1
            p2 = 0
            cur.execute('''INSERT INTO Game (Player1, Player2) 
                    VALUES ( ?, ? )''', (p1,p2))
            cur.execute('SELECT MAX(id) FROM Game')
            id = cur.fetchone()[0]
            cur.execute('SELECT SUM(Player1) FROM game')
            sump1 = cur.fetchone()[0]
            cur.execute('SELECT SUM(Player2) FROM game')
            sump2 = cur.fetchone()[0]
            sco = id, sump1, sump2
            self.score = str(sco)
            conn.commit()
        elif self.pwinner == 'Player 2 wins!':
            p1 = 0
            p2 = 1
            cur.execute('''INSERT INTO Game (Player1, Player2) 
                    VALUES ( ?, ? )''', (p1,p2))
            cur.execute('SELECT MAX(id) FROM Game')
            id = cur.fetchone()[0]
            cur.execute('SELECT SUM(Player1) FROM game')
            sump1 = cur.fetchone()[0]
            cur.execute('SELECT SUM(Player2) FROM game')
            sump2 = cur.fetchone()[0]
            sco = id, sump1, sump2
            self.score = str(sco)
            conn.commit()
        elif self.pwinner == 'Draw!':
            p1 = 0
            p2 = 0
            cur.execute('''INSERT INTO Game (Player1, Player2) 
                    VALUES ( ?, ? )''', (p1,p2))
            cur.execute('SELECT MAX(id) FROM Game')
            id = cur.fetchone()[0]
            cur.execute('SELECT SUM(Player1) FROM game')
            sump1 = cur.fetchone()[0]
            cur.execute('SELECT SUM(Player2) FROM game')
            sump2 = cur.fetchone()[0]
            sco = id, sump1, sump2
            self.score = str(sco)
            conn.commit()

    # Output function
    def __str__(self):
        return self.score





