#Game_GUI.py
#https://github.com/d-h-saintleo/Flood-The-Board-Game


#Python Module Imports
import time
import random
import functools
from tkinter import *

#Source File Imports
import Colors
from Board import *



#Label text variable - changeable text for label
#https://stackoverflow.com/questions/43965856/update-label-elements-in-tkinter



def CreateButtons():

    for y in range(0, b.Y()):
        for x in range(0, b.X()):
            if b.Grid()[y][x].IsAbsorbed() == True:
                t = "O"
            else:
                t = ""

            buttons[y][x] = Button(window, text=t, bg=b.Grid()[y][x].Color(), command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))
            buttons[y][x].config(height=1, width=2, state='normal')
            buttons[y][x].grid(column=x, row=y)



def UpdateButtons():

    for y in range(0, b.Y()):
        for x in range(0, b.X()):
            if b.Grid()[y][x].IsAbsorbed() == True:
                t = "O"
                buttons[y][x].config(height=1, width=2, state='normal', bg=b.Grid()[y][x].Color(), text=t)
                buttons[y][x].config(command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))
            else:
                t = ""
                buttons[y][x].config(height=1, width=2, state='normal', bg=b.Grid()[y][x].Color(), text=t)
                buttons[y][x].config(command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))

            #buttons[y][x].config(height=1, width=2, state='normal', bg=b.Grid()[y][x].Color(), text=t)
            buttons[y][x].grid(column=x, row=y)
            



def SwitchColor(c):
    b.SetColor(c)
    UpdateButtons()
    #UpdateProgress()
    window.update()



def UpdateProgress():
    #progress1.set(str(b.FloodPercent()) + "%")
    #turns.set("10/50")
    pass



#Create Board
x1 = 15
y1 = 15
c1 = 4
b = Board(x1,y1,c1,True)
g = b.ColorGrid()




#Create GUI Window
#==========================================================================
window = Tk()
window.title("Fldoo teh Board (" + str(x1) + "x" + str(y1) + "x" + str(c1) + "(")
#Dynamically Create Window Size
#geometryString = str(str((b.X() * 26) + 100) + "x" + str((b.Y() * 26) + 12))
geometryString = str(str((b.X() * 21) + 100) + "x" + str((b.Y() * 26) + 12))
geometryString = "600x550"
window.geometry(geometryString)


#Change Window Icon
window.iconbitmap("icon.ico")


#Create Buttons
#==========================================================================
buttons = []
for y in range(0, b.Y()):
    buttons.append([])
    for x in range(0, b.X()):
        buttons[y].append(None)

CreateButtons()





#Labels
#==========================================================================
"""
#Spacer Label
lblTurnsTitle = Label(window, text="")
lblTurnsTitle.config(height=1, width=2)
lblTurnsTitle.grid(column=b.X()+1, row=0)
#Turns Title
lblTurnsTitle = Label(window, text="Turns:")
lblTurnsTitle.config(height=1)
lblTurnsTitle.grid(column=b.X()+2, row=0)
#Progress Title
lblTurnsTitle = Label(window, text="Flood:")
lblTurnsTitle.config(height=1)
lblTurnsTitle.grid(column=b.X()+2, row=1)
#Turns Count
turns = StringVar()
lblTurns = Label(window, textvariable=turns)
lblTurns.config(height=1)
lblTurns.grid(column=b.X()+3, row=0)
#Process Count
progress1 = StringVar()
lblProgress = Label(window, textvariable=progress1)
lblProgress.config(height=1)
lblProgress.grid(column=b.X()+3, row=1)
"""






#Update Game Progress
UpdateProgress()


#Main GUI Loop
window.mainloop()




