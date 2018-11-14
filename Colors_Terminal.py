

def Red():
    return "1"

def Blue():
    return "2"

def Green():
    return "3"

def Yellow():
    return "4"
    
def Purple():
    return "5"
    
def Cyan():
    return "6"
    
def Orange():
    return "7"
    
def White():
    return "8"
    
def Black():
    return "9"
    
def Pink():
    return "0"
    



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


    
