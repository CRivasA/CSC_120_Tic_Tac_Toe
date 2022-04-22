# ----------------------------------------------------------------
# Carlos Rivas
# 04/18/2021.#
# ----------------------------------------------------------------
# CSC120 - Lab 09
# 2 PLayer Tic-Tac-Toe.
# -----------------------------------------------------------------
from tkinter import *
import tkinter as tk
from Game_db import Db

#Board Class
class Winner:
    # init function and GUI
    def __init__(self,  pwinner):
        self.pwinner = pwinner
        self.score = ''

        # Log in Window GUI creation
        self.win = tk.Tk()
        self.win.title('Tic-Tac-Toe')
        self.win.geometry('300x150')

        # Frame containers creation
        self.line1_frame = tk.Frame(self.win)
        self.line2_frame = tk.Frame(self.win)
        self.line3_frame = tk.Frame(self.win)
        self.line4_frame = tk.Frame(self.win)

        # Win text label
        pwinner = self.pwinner
        self.lv_label = tk.Label(self.line1_frame, text=pwinner, font=("Helvetica", 14))
        self.lv_label.pack()

        # Quit and continue button
        quit_button = tk.Button(self.line2_frame, text='Continue', command=self.Continue, padx=10, bd=3)
        quit_button.pack()
        quit_button = tk.Button(self.line2_frame, text='Exit', command=self.Quit, padx=10, bd=3)
        quit_button.pack(side='left')

        # Score text label
        score_li=[]
        self.score = Db(self.pwinner)
        score = self.score
        sscore = str(score)
        Idsc=sscore[1]
        p1sc = sscore[4]
        p2sc = sscore[7]
        idscore = 'Game #'+Idsc
        fscore = 'Player1: ' + p1sc + '    Player2: ' + p2sc
        self.sc_label = tk.Label(self.line3_frame, text=idscore, font=("Helvetica", 12))
        self.sc_label.pack()
        self.sc1_label = tk.Label(self.line4_frame, text=fscore, font=("Helvetica", 12))
        self.sc1_label.pack()

        #Packing
        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()
        self.line4_frame.pack()
        tk.mainloop()

    # Quit function
    def Continue(self):
        self.win.after(1000, lambda: self.win.destroy())
        self.status = 'go'

    # Quit function
    def Quit(self):
        self.win.destroy()
        self.status = 'stop'

    # Output function
    def __str__(self):
        return self.status
