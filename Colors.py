#Colors.py
#https://github.com/d-h-saintleo/Flood-The-Board-Game


#Color Hex Values
def Red():
    return "#ff0000"

def Blue():
    return "#0000ff"

def Green():
    return "#008000"

def Yellow():
    return "#ffff00"
    
def Black():
    return "#000000"
    
def White():
    return "#ffffff"

def Gray():
    return "#808080"

def Orange():
    return "#ffa500"

def Purple():
    return "#800080"

def Cyan():
    return "#00ffff"

def Pink():
    return "#ffc0cb"


    
#Return list of values (color hex or integers)
def Set(size, returnHex):

    #Return color hex values set(GUI version)
    if returnHex == True:
        return  [Red(), Blue(), Green(), Yellow(), Purple(), Cyan(), Orange(), White(), Black(), Pink()][0:size] 
    
    #Return single integer values set(terminal version)
    elif returnHex == False:
        set = []
        for i in range(0, size):
            set.append(str(i))
        return set
    
        
