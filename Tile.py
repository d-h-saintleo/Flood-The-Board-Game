

class Tile:

    #Init
    def __init__(self, xInput, yInput):
    
        #Private Instance Variables:
        #Color
        self._Color = None
        #Grid Location (X and Y Axis):    
        self._Location = {"X":int(xInput), "Y":int(yInput)}    
        #Neighbor Grid Locations (X and Y Axis)
        self._NorthNeighbor = {"X":None, "Y":None}
        self._EastNeighbor = {"X":None, "Y":None}
        self._SouthNeighbor = {"X":None, "Y":None}
        self._WestNeighbor = {"X":None, "Y":None}
        #Absorbed
        self._Absorbed = False
        self._FullyAbsorbed = False      #All neighbors are absorbed
    
        #Calculate Neighbor Values
        self.CalculateNeighbors()
    
    
    #Override Objecy String Return - coordinates formated
    def __str__(self):
        return "(" + str(self._Location["X"]) + "," + str(self._Location["Y"]) + ")"    
    
    
    #Calculate Neighbor Coordinates
    def CalculateNeighbors(self):
        #North
        self._NorthNeighbor["X"] = self._Location["X"]
        self._NorthNeighbor["Y"] = self._Location["Y"] - 1
        #East
        self._EastNeighbor["X"] = self._Location["X"] + 1
        self._EastNeighbor["Y"] = self._Location["Y"]
        #South
        self._SouthNeighbor["X"] = self._Location["X"]
        self._SouthNeighbor["Y"] = self._Location["Y"] + 1
        #West
        self._WestNeighbor["X"] = self._Location["X"] - 1
        self._WestNeighbor["Y"] = self._Location["Y"]



    #Set the color
    def SetColor(self, inputColor):
        self._Color = str(inputColor)
    
    #Set Absorbed
    def SetAbsorbed(self):
        self._Absorbed = True
    
    #Set Fully Absorbed
    def SetFullyAbsorbed(self):
        self._FullyAbsorbed = True
    
    #Set Neighbor value to null (edges/corners)
    def SetNeighborToNull(self, inputNeighbor):
        if inputNeighbor == "North":
            self._NorthNeighbor["X"] = None
            self._NorthNeighbor["Y"] = None
        elif inputNeighbor == "East":
            self._EastNeighbor["X"] = None
            self._EastNeighbor["Y"] = None
        elif inputNeighbor == "South":
            self._SouthNeighbor["X"] = None
            self._SouthNeighbor["Y"] = None
        elif inputNeighbor == "West":
            self._WestNeighbor["X"] = None
            self._WestNeighbor["Y"] = None
        else:
            pass

    
    #Return Value Functions
    def X(self):
        return self._Location["X"]
    def Y(self):
        return self._Location["Y"]
    def Location(self):
        return self._Location
    def Coordinates(self):
        return "(" + str(self._Location["X"]) + "," + str(self._Location["Y"]) + ")"
    def Color(self):
        return self._Color
    def NorthNeighbor(self):
        return self._NorthNeighbor
    def EastNeighbor(self):
        return self._EastNeighbor
    def SouthNeighbor(self):
        return self._SouthNeighbor
    def WestNeighbor(self):
        return self._WestNeighbor
    def IsAbsorbed(self):
        return self._Absorbed
    def IsFullyAbsorbed(self):
        return self._FullyAbsorbed

    
