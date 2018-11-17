#https://github.com/d-h-saintleo/Flood-The-Board-Game
    
#Python Module Imports
import math
import random
#Source File Imports
import Colors_Terminal as Colors
from Tile import *




class Board:
    
    def __init__(self, sizeX, sizeY, colorSetSize):

        #Instance Private Variables
        self._Grid = []
        self._GridSize = {"X":int(sizeX), "Y":int(sizeY)}
        self._ColorSize = int(colorSetSize)
        self._ColorSet = []
        self._FloodColor = None
        self._WinningScore = None
        
        
        #Get Colors
        self._ColorSet = Colors.Set(colorSetSize)
        


        #Add Tiles
        for row_y in range(0, sizeY):
            self._Grid.append([])
            for column_x in range(0, sizeX):
                self._Grid[row_y].append(Tile(column_x, row_y))
                #Set random color to tile
                self._Grid[row_y][column_x].SetColor(self._ColorSet[random.randint(0,len(self._ColorSet)-1)])
                #Set neighbors to null if edge/corner
                self.FindNullNeighbors(column_x, row_y)
                
                
        #Set flood color to the first tile
        self._FloodColor = self._Grid[0][0].Color()
        
        #Set Starting Tile to absorbed
        self._Grid[0][0].SetAbsorbed()
        
        #Absorb any neighbors
        self.Absorb()
        
        #Calculate the score to win
        self.CalculateWinningScore()
        
        
        
        
    #Find corners and edges and mark neighbors as null
    def FindNullNeighbors(self, x, y):
        #North
        if self._Grid[y][x].NorthNeighbor()["X"] < 0 or \
            self._Grid[y][x].NorthNeighbor()["Y"] < 0 or \
            self._Grid[y][x].NorthNeighbor()["X"] >= self._GridSize["X"] or \
            self._Grid[y][x].NorthNeighbor()["Y"] >= self._GridSize["Y"]:
                self._Grid[y][x].SetNeighborToNull("North")
        #East
        if self._Grid[y][x].EastNeighbor()["X"] < 0 or \
            self._Grid[y][x].EastNeighbor()["Y"] < 0 or \
            self._Grid[y][x].EastNeighbor()["X"] >= self._GridSize["X"] or \
            self._Grid[y][x].EastNeighbor()["Y"] >= self._GridSize["Y"]:
                self._Grid[y][x].SetNeighborToNull("East")
        
        #South
        if self._Grid[y][x].SouthNeighbor()["X"] < 0 or \
            self._Grid[y][x].SouthNeighbor()["Y"] < 0 or \
            self._Grid[y][x].SouthNeighbor()["X"] >= self._GridSize["X"] or \
            self._Grid[y][x].SouthNeighbor()["Y"] >= self._GridSize["Y"]:
                self._Grid[y][x].SetNeighborToNull("South")
        
        #West
        if self._Grid[y][x].WestNeighbor()["X"] < 0 or \
            self._Grid[y][x].WestNeighbor()["Y"] < 0 or \
            self._Grid[y][x].WestNeighbor()["X"] >= self._GridSize["X"] or \
            self._Grid[y][x].WestNeighbor()["Y"] >= self._GridSize["Y"]:
                self._Grid[y][x].SetNeighborToNull("West")
        
    
    
    #Absorb Tiles
    def Absorb(self):
        
        absorbedCount = 1

        #Loop though tiles until no more tiles can be absorbed
        while absorbedCount > 0:

            #Reset count
            absorbedCount = 0
            
            #Loop through tiles
            for row in self._Grid:
                for tile in row:
                    #If a tile is already absorbed, check the neighbors
                    if tile.IsAbsorbed() == True and tile.IsFullyAbsorbed() == False:
                        
                        #Check Neighbor Colors, and if they match and are not already absorbed, absorb them, (exceptions for edges/corner null coordinates)
                        #North
                        try:
                            if self._Grid[tile.NorthNeighbor()["Y"]][tile.NorthNeighbor()["X"]].Color() == tile.Color() and self._Grid[tile.NorthNeighbor()["Y"]][tile.NorthNeighbor()["X"]].IsAbsorbed() == False:
                                self._Grid[tile.NorthNeighbor()["Y"]][tile.NorthNeighbor()["X"]].SetAbsorbed()
                                absorbedCount += 1
                        except:
                            pass
                        #East
                        try:
                            if self._Grid[tile.EastNeighbor()["Y"]][tile.EastNeighbor()["X"]].Color() == tile.Color() and self._Grid[tile.EastNeighbor()["Y"]][tile.EastNeighbor()["X"]].IsAbsorbed() == False:
                                self._Grid[tile.EastNeighbor()["Y"]][tile.EastNeighbor()["X"]].SetAbsorbed()
                                absorbedCount += 1
                        except:
                            pass
                        #South
                        try:
                            if self._Grid[tile.SouthNeighbor()["Y"]][tile.SouthNeighbor()["X"]].Color() == tile.Color() and self._Grid[tile.SouthNeighbor()["Y"]][tile.SouthNeighbor()["X"]].IsAbsorbed() == False:
                                self._Grid[tile.SouthNeighbor()["Y"]][tile.SouthNeighbor()["X"]].SetAbsorbed()
                                absorbedCount += 1
                        except:
                            pass
                        #West
                        try:
                            if self._Grid[tile.WestNeighbor()["Y"]][tile.WestNeighbor()["X"]].Color() == tile.Color() and self._Grid[tile.WestNeighbor()["Y"]][tile.WestNeighbor()["X"]].IsAbsorbed() == False:
                                self._Grid[tile.WestNeighbor()["Y"]][tile.WestNeighbor()["X"]].SetAbsorbed()
                                absorbedCount += 1
                        except:
                            pass
                            
    
    
    
    #Change Flood Color and update Tiles
    def SetColor(self, inputColor):
        
        #Update Flood Color Value
        self._FloodColor = str(inputColor)
        
        #Change all absorbed tiles to new color
        for row in self._Grid:
            for tile in row:
                if tile.IsAbsorbed() == True:
                    tile.SetColor(self._FloodColor)
                
        #Absorb New Tiles
        self.Absorb()
                
            
    #Check if all tiles have been absorbed into flood, return boolean
    def IsFlooded(self):
        flooded = True
        for row in self._Grid:
            for tile in row:
                if tile.IsAbsorbed() == False:
                    flooded = False
        return flooded
    
    
    #Return integer of the percentage of tiles absorbed, rounded up
    def FloodPercent(self):
        tilesAbsorbed = 0
        totalTiles = int(self._GridSize["X"]) * int(self._GridSize["Y"])
        for row in self._Grid:
            for tile in row:
                if tile.IsAbsorbed() == True:
                    tilesAbsorbed +=1
                    
        return int(math.floor(100 * (tilesAbsorbed / totalTiles)))
    
    
    #Calculate the winning score based on size of board and number of colors
    def CalculateWinningScore(self):
        #X and Y = Board Size
        #C = Number of colors
        #Formula:
        #   (sqrt(X * Y) * (C / 3.75)) = Rounded
        self._WinningScore = round(math.sqrt(self._GridSize["X"] * self._GridSize["Y"]) * (self._ColorSize / 3.75))
        
    
    #Override Object String Return - Print Board of Colors
    def __str__(self):
        string = ""
        c  = ""
        a = ""
        for row in self._Grid:
            for tile in row:

                if tile.IsAbsorbed() == True:
                    a = "#"
                else:
                    a = " "
                string += "[" + tile.Color() + a + "]"
            string += "\n"
            
        return string
        
        
    
    
        
    #Return Functions
    def Grid(self):
        return self._Grid
    def FloodColor(self):
        return self._FloodColor
    def Color(self):
        return self._FloodColor
    def ColorSet(self):
        return self._ColorSet
    def Size(self):
        return self._GridSize
    def X(self):
        return self._GridSize["X"]
    def Y(self):
        return self._GridSize["Y"]
    def WinningScore(self):
        return self._WinningScore
    def Tiles(self):
        return self._GridSize["Total"]
    def ColorGrid(self):
        colorGrid = []
        for row_y in range(0, self._GridSize["Y"]):
            colorGrid.append([])
            for column_x in range(0, self._GridSize["X"]):
                colorGrid[row_y].append(self._Grid[row_y][column_x].Color())
        return colorGrid
        
        
    def PrintNeighbors(self, x, y):
        print("N:")
        print(self._Grid[y][x].NorthNeighbor())
        print("\nE:")
        print(self._Grid[y][x].EastNeighbor())
        print("\nS:")
        print(self._Grid[y][x].SouthNeighbor())
        print("\nW:")
        print(self._Grid[y][x].WestNeighbor())
        
        
        

