#Game_Terminal.py
#https://github.com/d-h-saintleo/Flood-The-Board-Game


#Source File Imports
from Board import *



#Inital Printed Message
print("Welcome to Flood the Board!")
print("==============================================================\n")
print("Instructions:")
print("  -Input the inital game parameters.")
print("  -Switch the color of the board until all tiles are the same color.")
print("  -To win the game, flood the board within the limited amount of turns.")
print("  -'Q' can be used anytime to exit the game.")
print("\n\n")
print("Game Parameters:")
print("==============================================================")



#Get Initial Inputs
while True:
    try:
        xInput = int(input("Input Board Width (1-15): "))
        if xInput > 0 and xInput < 16:
            break
        else:
            print("Invalid Input.\n")
        
    except:
        print("Invalid Input.\n")
        
while True:
    try:
        yInput = int(input("Input Board Height (1-15): "))
        if yInput > 0 and yInput < 16:
            break
        else:
            print("Invalid Input.\n")
        
    except:
        print("Invalid Input.\n")
        

while True:
    try:
        colorsInput = int(input("Input Number of Colors (2-10): "))
        if colorsInput > 1 and colorsInput < 11:
            break
        else:
            print("Invalid Input.\n")
        
    except:
        print("Invalid Input.\n")




#Create Board
board = Board(xInput, yInput, colorsInput, False)
#Color Set:
colorSet = board.ColorSet()
colorSetString = ""
for i in colorSet:
    colorSetString += i + ","
colorSetString = colorSetString[:-1]
#Turns variable
turns = 0
#Quit Early
quitEarly = False


#Loop until game is over (IsFlooded == True)
while board.IsFlooded() == False:
    #Print Separater
    print("\n==============================================================\n")
    #Print Board
    print(board)
    #Print Game Stats
    
    print("Flood:\t" + str(board.FloodPercent()) + "%")
    print("Turns:\t" + str(turns) + " / " + str(board.WinningScore()))
    print()
    
    #Get User Input - Color Change
    turnInput = ""
    while str(turnInput).upper() not in colorSet and str(turnInput).upper() != "Q":
        turnInput = str(input("Input Color (" + colorSetString + "): ")).upper()

    #Quit Early or
    if turnInput == "Q":
        quitEarly = True
        break
    else:
        #Set new color
        board.SetColor(turnInput)


    #Absorb
    board.Absorb()
    
    #Increment turns
    turns += 1
    

    


#Game Finished
#Print Final Board/Stats
if quitEarly == False:
    print("\n==============================================================\n")
    print(board)
    print("Flood:\t" + str(board.FloodPercent()) + "%")
    print("Turns:\t" + str(turns) + " / " + str(board.WinningScore()))
    print("\n")
    
    #Check if player won
    if turns <= board.WinningScore():
        print("You Win!\n\n")
    else:
        print("You Lost...\n\n")
    

    #Quit 
    quit = ""
    while str(quit).upper() != "Q":
        quit = str(input("'Q' to Quit: ")).upper()


    


