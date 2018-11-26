https://github.com/d-h-saintleo/Flood-The-Board-Game

# Flood The Board Game
- [x] Version 1 - Terminal
  - [x] Version 1.0 - First terminal version
  - [x] Version 1.1 - Updates to help facilitate GUI implementation
  - [x] Version 1.2 - GUI proof of concept
- [X] Version 2 - GUI
  - [x] Version 2.0 - First GUI Release (**see "Known Issues"**)
  - [ ] Version 2.1 - v2.0 Errors fixed
- [ ] Version 3 - Final Version

# Requirements:
Python 3.0 or greater (https://www.python.org/downloads/)

# Instructions:
1. Download the Zip file containing all the files
2. Extract the folder containing the source files
3. With all the files in the same folder:
   - Run the "Game_Terminal.py" file to play the full Terminal version of the game
     - Terminal version demonstrates all of the internals/features of the game
   - Run the "Game_GUI.py" to test the incomplete GUI version of the game
     - GUI version to interface with the internals of the game

# Game Instructions:
* The objective of the game is to flood the entire board with the same color in a limited amount of turns based on the size and complexity of the board. In order to do this, you must switch the color of the flood to a color of the neighboring tiles that are touching the flood until all tiles are the same color.

* **Terminal**: To get started, you first must select the width and heighth of the board as well as the number of colors to be used. Then you must select a color in order to switch the color of the flood. The board will update and display your current progress as you switch colors until the board is completely flood, or you exit the game.

* **GUI**: To get started, you first must select the width and heighth of the board as well as the number of colors to be used. Then you must click on any tile in order to switch the color of the flood to that tile's color. The board will update and display your current progress as you switch colors until the board is completely flood, or you exit the game.


# Known Issues:

- Window "X" button continues to start a new game rather than exit the game
	- "Exit Game" button and "File/Exit" from menu bar will properly exit the game
	- Callback function needed to properly exit mutliple games/windows loop
- Turns does not update on the GUI
	- Variable errors raised
	- Potential fix is to move turns tracking to be a function of Board() rather than Game().
- Minimum Height restricted to 8 due to current GUI limitations
	- Fixable, but needs additional GUI layout code

# Other Needed Additions:
- File Menu Bar:
	- Instructions Window
- Flag to mark that a game win/lose message has already been displayed
- Once GUI issue that is limiting max height to 8 is fixed, borders on the tiles can be removed to make the tiles look more connected
	- Potentially have this a checkbox toggle
- Additional window scaling
	- Intervals of 5, instead of the current: 10
- General code clean up
