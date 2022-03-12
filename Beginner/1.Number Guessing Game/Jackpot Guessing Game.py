from tkinter import *
import math
root = Tk()

root.title("Guess the Jackpot")
root.geometry("375x375+200+200")
root.configure(background='orange')


class Jackpot:

    lower = IntVar()
    upper = IntVar()
    upper.set(100)
    guess = IntVar()
    jackpot_value = IntVar()
    chances = round(math.log(upper.get()-lower.get() , 2))
    #result_lbl.configure(text = f"You have {chances} tries to Guess !!")

    def __init__(self):

        self.wfont = ('Times New Roman', 20)
        self.lfont = ('Comic Sans MS', 18)
        # Welcome label
        self.welcome = Label(root, text = '!! Welcome to the GameWorld !!', font = self.wfont, fg = 'Black', bg = 'orange', anchor = 'center')
        self.welcome.grid(row = 0, column = 0, sticky = EW, padx = 5, pady = 10,
                        columnspan = 2)
        
        # lower bound label
        self.lower_lbl = Label(root, text = 'Lower Bound', font = self.lfont, bg = 'blue', fg = 'yellow')
        self.lower_lbl.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)
        # Upper bound label
        self.upper_lbl = Label(root, text = 'Upper Bound', font = self.lfont, bg = 'blue', fg = 'yellow')
        self.upper_lbl.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)
        # Guess label
        self.guess_lbl = Label(root, text = '??? Guess the Jackpot ???', font = self.wfont, bg = 'orange', fg = 'Black')
        self.guess_lbl.grid(row = 3, column = 0, sticky = EW, padx = 5, pady = 10, columnspan = 2)
        # Result label
        self.result_lbl = Label(root, text = 'Make Your First Guess Buddy', font = self.lfont, bg = 'orange', fg = 'darkViolet'
                                ,wraplength=370, justify="center")
        self.result_lbl.grid(row = 6, column = 0, sticky = N, padx = 5, pady = 10, columnspan = 2)
    
        # lower bound Entry
        self.lower_ent = Entry(root, textvariable = self.lower, font = self.lfont, bg = 'white',  fg = 'red')
        self.lower_ent.grid(row = 1, column = 1, sticky = W, padx = 5, pady = 5)
        # Upper bound Entry
        self.upper_ent = Entry(root, textvariable = self.upper, font = self.lfont, bg = 'white',  fg = 'red')
        self.upper_ent.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
        # User Guess Entry
        self.guess_ent = Entry(root, textvariable = self.guess, font = self.lfont, bg = 'white',  fg = 'red')
        self.guess_ent.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 10, sticky = EW)

        # User Guess Submit Button
        self.guess_ent = Button(root, text = "Submit", font = self.lfont, fg = 'Black', command = self.jackpotcheck)
        self.guess_ent.grid(row = 5, column = 1, padx = 5, pady = 10, sticky = W)

        #Start the loop
        root.mainloop()

    def jackpotcheck(self):

        if self.lower.get()==self.upper.get():
            self.result_lbl.configure(text = "Enter Distinct Values of Lower to Upper Bound range.")
        

    def typecheck(self):
        pass
        

#Calling the class
a = Jackpot()
