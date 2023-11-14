# 2048

To access the code for the game, please click the link below. The code is written entirely in **python**, so please ensure this is installed on your machine, and that your file editor supports this.
(Click here to access the code)[https://github.com/buzby08/2048/blob/000c679c98bae734e32fd22c0139f58cc1e842e4/main.py]

# Description and Rules for the Game 2048:
2048 is a captivating puzzle game that challenges your strategic thinking and planning skills. The game is played on a 4x4 grid, and the goal is to reach the elusive "2048" tile.

**How to Play:**
1. Objective: Combine numbered tiles on the 4x4 grid to reach the tile with the number "2048".
2. Tile Movement: Use the arrow keys (Up, Down, Left, Right) to shift all the tiles in the desired direction.
3. Tile Merging: When two tiles with the same number collide as a result of a move, they merge into a new tile with the sum of their values.
4. Tile Generation: After each move, a new tile with a value of "2" is randomly added to an empty spot on the board.
5. Game Over: The game ends when there are no valid moves left, or when the player achieves the "2048" tile.

**Special Features:**
1. Tile Colors: Each tile is represented by a different color for visual distinction.
2. Console Commands: The game supports console commands for advanced features, such as adding specific tiles or clearing the board.

**Winning:**
If you successfully merge tiles to create a tile with the value "2048", congratulations, you win the game!

**Losing:**
The game ends if there are no more valid moves left, and the board is full.

**Tips:**
1. Plan your moves strategically to avoid reaching a point where no more merges are possible.
2. Use console commands wisely for experimentation and testing.

___

# Constants:

The following items are constants in the main.py file. Edit these to your liking.

  - **FONT** - This is used to change the font family and / or size. It is formatted
               as ``FONT = ("font_family", font_size) ``.
               **If you are running the code on your local machine**, the font family you
               are using needs to be installed.
               **If you are running the code on replit**, it needs to be installed on replit,
               and I think only Arial is installed.
  - **BG_COLOUR** - This is used to change the background colour of the _window_ only, not
                  the widgets colour. To change this, look at colour_dict
  - **FG_COLOUR** - This is used to change the foreground colour of the _labels_. Pick a
                    colour that will be visable with the different background colours of
                    the labels, found in colour_dict
  - **colour_dict** - This dictionary has the different background colours of the labels
                      depending on what number they are. This currently only goes up to
                      the tile 2048, but you can add more numbers and colours so you can
                      get tiles higher than 2048.

# Defaults:
 Here are the default values for the above constants. 
 | Constant    | Value                             |
| ----------- | --------------------------------- |
| FONT        | `("Arial", 20)`                   |
| BG_COLOUR   | `"white"`                         |
| FG_COLOUR   | `"black"`                         |
| colour_dict | _**ON NEXT LINE, BELOW TABLE**_   |

 ``` python 
 colour_dict = {
    "|   |": "light gray",
    "| 2 |": "light salmon",
    "| 4 |": "salmon",
    "| 8 |": "coral",
    "| 16 |": "dark orange",
    "| 32 |": "orange",
    "| 64 |": "dark goldenrod",
    "| 128 |": "gold",
    "| 256 |": "yellow",
    "| 512 |": "dark khaki",
    "| 1024 |": "khaki",
    "| 2048 |": "dark olive green"
} ```


# Description and Rules for the Game 2048:
2048 is a captivating puzzle game that challenges your strategic thinking and planning skills. The game is played on a 4x4 grid, and the goal is to reach the elusive "2048" tile.

**How to Play:**
1. Objective: Combine numbered tiles on the 4x4 grid to reach the tile with the number "2048".
2. Tile Movement: Use the arrow keys (Up, Down, Left, Right) to shift all the tiles in the desired direction.
3. Tile Merging: When two tiles with the same number collide as a result of a move, they merge into a new tile with the sum of their values.
4. Tile Generation: After each move, a new tile with a value of "2" is randomly added to an empty spot on the board.
5. Game Over: The game ends when there are no valid moves left, or when the player achieves the "2048" tile.

**Special Features:**
1. Tile Colors: Each tile is represented by a different color for visual distinction.
2. Console Commands: The game supports console commands for advanced features, such as adding specific tiles or clearing the board.

**Winning:**
If you successfully merge tiles to create a tile with the value "2048", congratulations, you win the game!

**Losing:**
The game ends if there are no more valid moves left, and the board is full.

**Tips:**
1. Plan your moves strategically to avoid reaching a point where no more merges are possible.
2. Use console commands wisely for experimentation and testing.

___

# Constants:

The following items are constants in the main.py file. Edit these to your liking.

  - **FONT** - This is used to change the font family and / or size. It is formatted
               as ``FONT = ("font_family", font_size) ``.
               **If you are running the code on your local machine**, the font family you
               are using needs to be installed.
               **If you are running the code on replit**, it needs to be installed on replit,
               and I think only Arial is installed.
  - **BG_COLOUR** - This is used to change the background colour of the _window_ only, not
                  the widgets colour. To change this, look at colour_dict
  - **FG_COLOUR** - This is used to change the foreground colour of the _labels_. Pick a
                    colour that will be visable with the different background colours of
                    the labels, found in colour_dict
  - **colour_dict** - This dictionary has the different background colours of the labels
                      depending on what number they are. This currently only goes up to
                      the tile 2048, but you can add more numbers and colours so you can
                      get tiles higher than 2048.

# Defaults:
 Here are the default values for the above constants. 
 | Constant    | Value                             |
| ----------- | --------------------------------- |
| FONT        | `("Arial", 20)`                   |
| BG_COLOUR   | `"white"`                         |
| FG_COLOUR   | `"black"`                         |
| colour_dict | _**ON NEXT LINE, BELOW TABLE**_   |

 ``` python 
 colour_dict = {
    "|   |": "light gray",
    "| 2 |": "light salmon",
    "| 4 |": "salmon",
    "| 8 |": "coral",
    "| 16 |": "dark orange",
    "| 32 |": "orange",
    "| 64 |": "dark goldenrod",
    "| 128 |": "gold",
    "| 256 |": "yellow",
    "| 512 |": "dark khaki",
    "| 1024 |": "khaki",
    "| 2048 |": "dark olive green"
} ```
