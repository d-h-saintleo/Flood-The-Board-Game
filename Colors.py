

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


def Set(size):
    if size == 1:
        return [Red()]
    elif size == 2:
        return [Red(), Blue()]
    elif size == 3:
        return [Red(), Blue(), Green()]
    elif size == 4:
        return [Red(), Blue(), Green(), Yellow()]
    elif size == 5:
        return [Red(), Blue(), Green(), Yellow(), Purple()]
    elif size == 6:
        return [Red(), Blue(), Green(), Yellow(), Purple(), Cyan()]
    elif size == 7:
        return [Red(), Blue(), Green(), Yellow(), Purple(), Cyan(), Orange()]
    elif size == 8:
        return [Red(), Blue(), Green(), Yellow(), Purple(), Cyan(), Orange(), White()]
    elif size == 9:
        return [Red(), Blue(), Green(), Yellow(), Purple(), Cyan(), Orange(), White(), Black()]
    elif size == 10:
        return [Red(), Blue(), Green(), Yellow(), Purple(), Cyan(), Orange(), White(), Black(), Pink()]
    else:
        return None


    
