# ----------------------------------------------------------------
# Carlos Rivas
# 04/18/2021.#
# ----------------------------------------------------------------
# CSC120 - Lab 09
# 2 PLayer Tic-Tac-Toe.
# -----------------------------------------------------------------

#Board Class
class check_Win:
    # init function
    def __init__(self, p1_list, p2_list):
        self.p1_list = p1_list
        self.p2_list = p2_list
        self.winner = ''
        if 'c1' in self.p1_list and 'c2' in self.p1_list and 'c3' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c1' in self.p2_list and 'c2' in self.p2_list and 'c3' in self.p2_list:
            self.winner = 'Player 2 wins'
        if 'c4' in self.p1_list and 'c5' in self.p1_list and 'c6' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c4' in self.p2_list and 'c5' in self.p2_list and 'c6' in self.p2_list:
            self.winner = 'Player 2 wins'
        if 'c7' in self.p1_list and 'c8' in self.p1_list and 'c9' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c7' in self.p2_list and 'c8' in self.p2_list and 'c9' in self.p2_list:
            self.winner = 'Player 2 wins'
        elif 'c1' in self.p1_list and 'c5' in self.p1_list and 'c9' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c1' in self.p2_list and 'c5' in self.p2_list and 'c9' in self.p2_list:
            self.winner = 'Player 2 wins'
        elif 'c3' in self.p1_list and 'c5' in self.p1_list and 'c7' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c3' in self.p2_list and 'c5' in self.p2_list and 'c7' in self.p2_list:
            self.winner = 'Player 2 wins'
        elif 'c1' in self.p1_list and 'c4' in self.p1_list and 'c7' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c1' in self.p2_list and 'c4' in self.p2_list and 'c7' in self.p2_list:
            self.winner = 'Player 2 wins'
        elif 'c2' in self.p1_list and 'c5' in self.p1_list and 'c8' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c2' in self.p2_list and 'c5' in self.p2_list and 'c8' in self.p2_list:
            self.winner = 'Player 2 wins'
        elif 'c3' in self.p1_list and 'c6' in self.p1_list and 'c9' in self.p1_list:
            self.winner = 'Player 1 wins'
        elif 'c3' in self.p2_list and 'c6' in self.p2_list and 'c9' in self.p2_list:
            self.winner = 'Player 2 wins'
    # Output function
    def __str__(self):
        return self.winner







