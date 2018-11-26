#Game_GUI.py
#https://github.com/d-h-saintleo/Flood-The-Board-Game


#Python Module Imports
import time
import random
import functools
import webbrowser
from tkinter import *


#Source File Imports
import Colors
from Board import *



def CreateButtons():

    for y in range(0, b.Y()):
        for x in range(0, b.X()):

            buttons[y][x] = Button(window, bd=1, bg=b.Grid()[y][x].Color(), command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))
            buttons[y][x].config(height=1, width=2, state='normal')
            buttons[y][x].grid(column=x, row=y)



def UpdateButtons():

    for y in range(0, b.Y()):
        for x in range(0, b.X()):
            buttons[y][x].config(state='normal', bg=b.Grid()[y][x].Color())
            buttons[y][x].config(command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))
            buttons[y][x].grid(column=x, row=y)
            



def SwitchColor(c):
    b.SetColor(c)
    UpdateButtons()
    UpdateProgress()
    window.update()



def UpdateProgress():
    svProgress.set(str(b.FloodPercent()) + "%")
    svTurns.set("0 / 0")
    



def NewGame():
    window.destroy()
    
    
def ExitGame():
    svExit.set("True")
    window.destroy()
    
    
    
def OpenGitHub():
    webbrowser.open("https://github.com/d-h-saintleo/Flood-The-Board-Game",new=1)
    
    
def GetWindowSizeString(xInput, yInput):
    if xInput <= 10:
        x = 400
    elif xInput > 10 and xInput <=20:
        x = 625
    elif yInput > 20 and yInput <=30:
        x = 850
    else:
        x = 850
        
    if yInput <= 10:
        y = 275
    elif yInput > 10 and yInput <=20:
        y = 525
    elif yInput > 20 and yInput <=30:
        y = 750
    else:
        y = 750
        
    return str(x) + "x" + str(y)
    
    
    
#Initial Variables
boardWidthInput = 10
boardHeightInput= 10
boardColorsInput= 4
firstGame = True




while True:


    #Create Board
    if firstGame == True:
        boardWidthInput = 10
        boardHeightInput= 10
        boardColorsInput= 4
        firstGame = False

    
    b = Board(int(boardWidthInput), int(boardHeightInput), int(boardColorsInput), True)

    

    #Create GUI Window
    #==========================================================================
    window = Tk()
    window.title("Flood the Board Game (" + str(boardWidthInput) + "x" + str(boardHeightInput) + "x" + str(boardColorsInput) + ")")
    #Dynamically Create Window Size
    #geometryString = str(str((b.X() * 26) + 150) + "x" + str((b.Y() * 26) + 12))
    window.geometry(GetWindowSizeString(b.X(), b.Y()))


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

    
    
    

    #Spin Boxes
    #==========================================================================
    #Width
    svWidth = StringVar()
    spbWidth = Spinbox(window, from_=3, to=30, width=7, textvariable=svWidth)
    spbWidth.grid(column=b.X()+3, row=1)
    svWidth.set(boardWidthInput)
    #Height
    svHeight = StringVar()
    spbHieght = Spinbox(window, from_=8, to=30, width=7, textvariable=svHeight)
    spbHieght.grid(column=b.X()+3, row=2)
    svHeight.set(boardHeightInput)
    #Colors
    svColors = StringVar()
    spbColors = Spinbox(window, from_=2, to=10, width=7, textvariable=svColors)
    spbColors.grid(column=b.X()+3, row=3)
    svColors.set(boardColorsInput)


    
    #Labels
    #==========================================================================

    #Spacer Label
    lblTurnsTitle = Label(window, text="")
    lblTurnsTitle.config(height=1, width=2)
    lblTurnsTitle.grid(column=b.X()+1, row=0)
    #Options Title
    lblOptionsTitle = Label(window, text="Game Options:")
    lblOptionsTitle.config(height=1)
    lblOptionsTitle.grid(column=b.X()+2, row=0)
    #Width Title
    lblWidthTitle = Label(window, text="Width:")
    lblWidthTitle.config(height=1, width=10)
    lblWidthTitle.grid(column=b.X()+2, row=1)
    #Height Title
    lblHeightTitle = Label(window, text="Height:")
    lblHeightTitle.config(height=1)
    lblHeightTitle.grid(column=b.X()+2, row=2)
    #Colors Title
    lblColorsTitle = Label(window, text="Colors:")
    lblColorsTitle.config(height=1)
    lblColorsTitle.grid(column=b.X()+2, row=3)
    #Turns Title
    lblTurnsTitle = Label(window, text="Turns:")
    lblTurnsTitle.config(height=1)
    lblTurnsTitle.grid(column=b.X()+2, row=b.Y()-2)
    #Progress Title
    lblTurnsTitle = Label(window, text="Flood:")
    lblTurnsTitle.config(height=1)
    lblTurnsTitle.grid(column=b.X()+2, row=b.Y()-1)
    #Turns Count
    svTurns = StringVar()
    lblTurns = Label(window, textvariable=svTurns)
    lblTurns.config(height=1)
    lblTurns.grid(column=b.X()+3, row=b.Y()-2)
    svTurns.set("0 / 0")
    #Process Count
    svProgress = StringVar()
    lblProgress = Label(window, textvariable=svProgress)
    lblProgress.config(height=1)
    lblProgress.grid(column=b.X()+3, row=b.Y()-1)

    
    
    #Other Buttons
    #==========================================================================
    
    #New Game
    btnNewGame = Button(window, text="New Game")
    btnNewGame.config(height=1, width=8, bd=1, command=NewGame)
    btnNewGame.grid(column=b.X()+3, row=4)
    #Exit Game
    svExit = StringVar()
    btnExitGame = Button(window, text="Exit Game")
    btnExitGame.config(height=1, width=8, bd=1, command=ExitGame)
    btnExitGame.grid(column=b.X()+3, row=5)
    svExit.set("False")
    
    
    
    #File Menu Bar
    #==========================================================================
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Game", command=NewGame)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=ExitGame)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About")
    helpmenu.add_separator()
    helpmenu.add_command(label="GitHub", command=OpenGitHub)
    menubar.add_cascade(label="Help", menu=helpmenu)

    
    #Update Game Progress
    UpdateProgress()

    #Add Menu Bar
    window.config(menu=menubar)

    #Main GUI Loop
    window.mainloop()
    
    
    
    
    #After GUI Main Loop
    #==========================================================================
    
    #Get new board inputs and validate
    #Non integer values result in minimum value
    try:
        boardWidthInput = int(svWidth.get())
    except:
        boardWidthInput = 3
        
    try:
        boardHeightInput = int(svHeight.get())
    except:
        boardHeightInput = 8
    try:
        boardColorsInput = int(svColors.get())
    except:
        boardColorsInput = 2

    #Validate ranges
    if boardWidthInput < 3:
        boardWidthInput = 3
    elif boardWidthInput > 30:
        boardWidthInput = 30
    
    if boardHeightInput < 8:
        boardHeightInput = 8
    elif boardHeightInput > 30:
        boardHeightInput = 30
        
    if boardColorsInput < 2:
        boardColorsInput = 2
    elif boardColorsInput > 10:
        boardColorsInput = 10


    #Exit Window if exit button pressed
    #Known issue that red X window exit does not break the loop
    if str(svExit.get()) == "True":
        break
    
    
    
    
    
