#Game_GUI.py
#https://github.com/d-h-saintleo/Flood-The-Board-Game


#Python Module Imports
import time
import random
import functools
import webbrowser
from tkinter import *


#Source File Imports
from Board import *



#Create the initial tiles/buttons
def CreateButtons():

    for y in range(0, b.Y()):
        for x in range(0, b.X()):
            buttons[y][x] = Button(frameBoard, bd=int(ivBorderSize.get()), fg="black", bg=b.Grid()[y][x].Color(), command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))
            buttons[y][x].config(height=1, width=2, state='normal')
            buttons[y][x].grid(column=x, row=y)


#Update color of tiles/buttons
def UpdateButtons():


    for y in range(0, b.Y()):
        for x in range(0, b.X()):
            if b.Grid()[y][x].IsAbsorbed() == True:
                t = str(svMarker.get())
            else:
                t = ""
            
            buttons[y][x].config(state='normal', text=t, bg=b.Grid()[y][x].Color())
            buttons[y][x].config(command=functools.partial(SwitchColor, b.Grid()[y][x].Color()))
            buttons[y][x].grid(column=x, row=y)
            


#Switch the color of the board and update
def SwitchColor(c):
    b.SetColor(c)
    UpdateButtons()
    UpdateProgress()
    window.update()


#Update game progress (board %, turns, win/lose)
def UpdateProgress():
    
    svProgress.set(str(b.FloodPercent()) + "%")
    
    #Increment turns if game is not finished
    if bool(gameFinished.get()) == False:
        ivTurns.set(int(ivTurns.get()) + 1)
        svTurns.set(str(ivTurns.get()) + " / " + str(b.WinningScore()))
    
    #Check for win
    if b.FloodPercent() == 100 and bool(gameFinished.get()) == False:
        gameFinished.set(True)
        if int(ivTurns.get()) <= b.WinningScore():
            svWin.set("You Win!")
            lblWin.config(fg="green")
        else:
            svWin.set("You Lose!")
            lblWin.config(fg="red")

    #Check for lose (display lose before 100% complete)
    if int(ivTurns.get()) > b.WinningScore(): 
        svWin.set("You Lose!")
        lblWin.config(fg="red")
        
        


#New Game (destroy window to be rebuilt)
def NewGame():
    window.destroy()
    
    
#Exit Game (destroy window and do not rebuild)
def ExitGame():
    svExit.set("True")
    window.destroy()
    
    
#Open the project github link in web browser
def OpenGitHub():
    webbrowser.open("https://github.com/d-h-saintleo/Flood-The-Board-Game",new=1)

    
    
def on_close():
      ExitGame()
    

#Initial Variables
boardWidthInput = 10
boardHeightInput= 10
boardColorsInput= 4
firstGame = True
bordersTF = True
markersTF = False


#Main Loop
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
    #window.geometry(GetWindowSizeString(b.X(), b.Y()))
    

    #Change Window Icon
    window.iconbitmap("icon.ico")
    
    
    
    #Frames
    #==========================================================================
    frameBoard = Frame(window, bd=10, relief="raised")
    frameBoard.grid(column=0, row=0, rowspan=2)
    frameOptions = Frame(window)
    frameOptions.grid(column=1, row=0, sticky="n")
    frameProgress = Frame(window)
    frameProgress.grid(column=1, row=1, sticky="s")

    
    #Checkbuttons
    #==========================================================================
    
    #Borders Checkbox
    ivBorderSize = IntVar()
    cbBorders = Checkbutton(frameOptions, text="Borders", onvalue=2, offvalue=0, variable=ivBorderSize)
    cbBorders.config(height=1)
    cbBorders.grid(column=0, row=2)
    
    
    #Markers Checkbox
    svMarker = StringVar()
    cbMarkers = Checkbutton(frameOptions, text="Markers", onvalue="X", offvalue="", variable=svMarker)
    cbMarkers.config(height=1)
    cbMarkers.grid(column=1, row=2)
    
    if bordersTF == True:
        cbBorders.select()
    else:
        cbBorders.deselect()
    if markersTF == True:
        cbMarkers.select()
    else:
        cbMarkers.deselect()

            
    
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
    spbWidth = Spinbox(frameOptions, from_=3, to=30, width=8, justify="center", textvariable=svWidth)
    spbWidth.grid(column=0, row=1)
    svWidth.set(boardWidthInput)
    #Height
    svHeight = StringVar()
    spbHieght = Spinbox(frameOptions, from_=3, to=30, width=8, justify="center", textvariable=svHeight)
    spbHieght.grid(column=1, row=1)
    svHeight.set(boardHeightInput)
    #Colors
    svColors = StringVar()
    spbColors = Spinbox(frameOptions, from_=2, to=10, width=8, justify="center", textvariable=svColors)
    spbColors.grid(column=2, row=1)
    svColors.set(boardColorsInput)
    

    
    #Labels
    #==========================================================================
    
    #Width Title
    lblWidthTitle = Label(frameOptions, text="Width:")
    lblWidthTitle.config(height=1)
    lblWidthTitle.grid(column=0, row=0)
    #Height Title
    lblHeightTitle = Label(frameOptions, text="Height:")
    lblHeightTitle.config(height=1)
    lblHeightTitle.grid(column=1, row=0)
    
    #Colors Title
    lblColorsTitle = Label(frameOptions, text="Colors:")
    lblColorsTitle.config(height=1)
    lblColorsTitle.grid(column=2, row=0)
    #Turns Title
    lblTurnsTitle = Label(frameProgress, text="Turns:")
    lblTurnsTitle.config(height=1)
    lblTurnsTitle.grid(column=0, row=1)
    #Progress Title
    lblTurnsTitle = Label(frameProgress, text="Flood:")
    lblTurnsTitle.config(height=1)
    lblTurnsTitle.grid(column=0, row=2)
    #Turns Count
    ivTurns = IntVar()
    svTurns = StringVar()
    lblTurns = Label(frameProgress, textvariable=svTurns)
    lblTurns.config(width=8)
    lblTurns.grid(column=1, row=1)
    ivTurns.set(-1)
    #Process Count
    svProgress = StringVar()
    lblProgress = Label(frameProgress, textvariable=svProgress)
    lblProgress.config(width=8)
    lblProgress.grid(column=1, row=2)
    #Win Message Label
    svWin = StringVar()
    lblWin = Label(frameProgress, textvariable=svWin)
    lblWin.config(width=8, font="arial 18 bold", fg="black")
    lblWin.grid(column=1, row=0)
    svWin.set("")
    
    
    

    
    
    
    #Other Buttons
    #==========================================================================
    
    #New Game
    btnNewGame = Button(frameOptions, text="New Game")
    btnNewGame.config(height=1, width=8, bd=2, command=NewGame)
    btnNewGame.grid(column=2, row=2)
    #Exit Game
    svExit = StringVar()
    #btnExitGame = Button(frameOptions, text="Exit Game")
    #btnExitGame.config(height=1, width=8, bd=2, command=ExitGame)
    #btnExitGame.grid(column=0, row=4)
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
    helpmenu.add_command(label="About", command=OpenGitHub)
    menubar.add_cascade(label="Help", menu=helpmenu)

    
    #Game already won/finished variable
    gameFinished = BooleanVar()
    gameFinished.set(False)
        
    
    #Update Game Progress
    UpdateProgress()
    
    #Update the buttons for initial absorb
    UpdateButtons()

    #Add Menu Bar
    window.config(menu=menubar)

    
    
    #Add detection for window close
    window.protocol("WM_DELETE_WINDOW",  on_close)
    
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
        boardHeightInput = 3
    try:
        boardColorsInput = int(svColors.get())
    except:
        boardColorsInput = 2

    #Validate ranges
    if boardWidthInput < 3:
        boardWidthInput = 3
    elif boardWidthInput > 30:
        boardWidthInput = 30
    
    if boardHeightInput < 3:
        boardHeightInput = 3
    elif boardHeightInput > 30:
        boardHeightInput = 30
        
    if boardColorsInput < 2:
        boardColorsInput = 2
    elif boardColorsInput > 10:
        boardColorsInput = 10

    
    #Get Borders and Markers status
    if int(ivBorderSize.get()) == 0:
        bordersTF = False
    else:
        bordersTF = True
    if str(svMarker.get()) == "":
        markersTF = False
    else:
        markersTF = True


    #Exit Window if exit button pressed
    #Known issue that red X window exit does not break the loop
    if str(svExit.get()) == "True":
        break
    
    
    
    
