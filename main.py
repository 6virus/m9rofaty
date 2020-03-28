# ///////////////////////////////////////////////////////////////////////////////////
# Authors: Abdullah Najjar, Bahaa Najjar, Mudaa Najjar
# Date: 25 February, 2020
# Description: M9rofaty is an IOS application that helps the user to financially plan
# their budget on a monthly basis.
# Version: 0.1
# Bugs: allow CalculateCategories to take input & do its thing
# ///////////////////////////////////////////////////////////////////////////////////
# imports
from tkinter import Tk, Label, Button

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("M9rofaty")

        self.label = Label(master, text="Welcome to our app!")
        self.label.pack()

        self.incomebutton = Button(master, text="Enter", command=self.income)
        self.incomebutton.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    #To take the input-income from the user
    def income(self): 
        print("Income is: ")

        #income = input('Enter your monthly income?\n')
        #CalculateCategories(income)

        # Divide up the salary for the best case senario to visualize it for the user
        #def CalculateCategories(arg):
            # if ArithmeticError
            #print("qoq!")
            #CalculateCategories()

            # I/O function
            # def CalculateCategories(arg):
            #     # if ArithmeticError
            #     print("qoq!")
            # CalculateCategories()

root = Tk()
my_gui = MyGUI(root)
root.mainloop()
