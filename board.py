# ----------------------------------------------------------------
# Carlos Rivas
# 04/18/2021.#
# ----------------------------------------------------------------
# CSC120 - Lab 09
# 2 PLayer Tic-Tac-Toe.
# -----------------------------------------------------------------

from tkinter import *
import tkinter as tk

#Board Class
class Tic:
    # init function and GUI
    def __init__(self, player, pwinner, stt, stt1, value1, stt2, value2, stt3, value3, stt4, value4, stt5, value5, stt6, value6,
                 stt7, value7, stt8, value8, stt9, value9):
        self.player = player
        self.pwinner = pwinner
        self.stt =stt
        self.stt1 = stt1
        self.value1 = value1
        self.stt2 = stt2
        self.value2 = value2
        self.stt3 = stt3
        self.value3 = value3
        self.stt4 = stt4
        self.value4 = value4
        self.stt5 = stt5
        self.value5 = value5
        self.stt6 = stt6
        self.value6 = value6
        self.stt7 = stt7
        self.value7 = value7
        self.stt8 = stt8
        self.value8 = value8
        self.stt9 = stt9
        self.value9 = value9

        # Log in Window GUI creation
        self.option_win = tk.Tk()
        self.option_win.title('Tic-Tac-Toe')
        self.option_win.geometry('300x250')

        # Frame containers creation
        self.line1_frame = tk.Frame(self.option_win)
        self.line2_frame = tk.Frame(self.option_win)
        self.line3_frame = tk.Frame(self.option_win)
        self.line4_frame = tk.Frame(self.option_win)
        self.line5_frame = tk.Frame(self.option_win)
        self.line6_frame = tk.Frame(self.option_win)

        # Option text label
        self.label = tk.Label(self.line1_frame, text="Player:")
        self.log_value = tk.StringVar()
        self.lv_label = tk.Label(self.line1_frame, text=self.player)
        self.log_value.set('')
        self.label.pack(side='left')
        self.lv_label.pack(side='left')

        # Win text label
        self.lv_label = tk.Label(self.line6_frame, text=self.pwinner, font=("Helvetica", 14))
        self.lv_label.pack()

        #buttons
        stt = self.stt
        stt1 = self.stt1
        value1 = self.value1
        stt2 = self.stt2
        value2 = self.value2
        stt3 = self.stt3
        value3 = self.value3
        stt4= self.stt4
        value4 = self.value4
        stt5 = self.stt5
        value5 = self.value5
        stt6 = self.stt6
        value6 = self.value6
        stt7 = self.stt7
        value7 = self.value7
        stt8 = self.stt8
        value8 = self.value8
        stt9 = self.stt9
        value9 = self.value9

        button1 = tk.Button(self.line2_frame, text=value1, command=self.c1, state=stt1, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button1.pack(side=tk.LEFT)
        button2 = tk.Button(self.line2_frame, text=value2, command=self.c2, state=stt2, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button2.pack(side=tk.LEFT)
        button3 = tk.Button(self.line2_frame, text=value3, command=self.c3,  state=stt3, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button3.pack()
        button4 = tk.Button(self.line3_frame, text=value4, command=self.c4, state=stt4, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button4.pack(side=tk.LEFT)
        button5 = tk.Button(self.line3_frame, text=value5, command=self.c5, state=stt5, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button5.pack(side=tk.LEFT)
        button6 = tk.Button(self.line3_frame, text=value6, command=self.c6, state=stt6, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button6.pack()
        button7 = tk.Button(self.line4_frame, text=value7, command=self.c7, state=stt7, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button7.pack(side=tk.LEFT)
        button8 = tk.Button(self.line4_frame, text=value8, command=self.c8, state=stt8, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button8.pack(side=tk.LEFT)
        button9 = tk.Button(self.line4_frame, text=value9, command=self.c9, state=stt9, padx=10, bd=3, relief=tk.RAISED, borderwidth=5)
        button9.pack()

        # Quit button
        quit_button = tk.Button(self.line5_frame, text='Exit', command=self.Quit, padx=10, bd=3)
        quit_button.pack()

        # Setting the frames
        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()
        self.line4_frame.pack()
        self.line5_frame.pack(side='bottom')
        tk.mainloop()

    #Board function
    def c1(self):
        self.option_win.destroy()
        self.option = 'c1'

    def c2(self):
        self.option_win.destroy()
        self.option = 'c2'

    def c3(self):
        self.option_win.destroy()
        self.option = 'c3'

    def c4(self):
        self.option_win.destroy()
        self.option = 'c4'

    def c5(self):
        self.option_win.destroy()
        self.option = 'c5'

    def c6(self):
        self.option_win.destroy()
        self.option = 'c6'

    def c7(self):
        self.option_win.destroy()
        self.option = 'c7'

    def c8(self):
        self.option_win.destroy()
        self.option = 'c8'

    def c9(self):
        self.option_win.destroy()
        self.option = 'c9'

    #Quit function
    def Quit(self):
        self.option_win.destroy()
        self.option = 'stop'
        self.log_value.set(f'Session ended')

    # Output function
    def __str__(self):
        return self.option





