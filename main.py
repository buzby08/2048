import traceback
from datetime import datetime as dt
from random import randint
from tkinter import Label, Tk
from tkinter import messagebox as msg

# CONSTANTS 

FONT = ("Bodoni MT", 50)
BG_COLOUR = "white"
FG_COLOUR = "black"

# ------------------------------------

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
}


empty_tile = '|   |'
processing_key = False
start_time = None
stop_time = None

root = Tk()
root.title("2048")
root.config(bg=BG_COLOUR)

lbl0 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl1 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl2 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl3 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl4 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl5 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl6 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl7 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl8 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl9 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl10 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl11 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl12 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl13 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl14 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)
lbl15 = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)

info_lbl = Label(root, fg=FG_COLOUR, bg=BG_COLOUR)

lbl0.grid(row=0, column=0)
lbl1.grid(row=0, column=1)
lbl2.grid(row=0, column=2)
lbl3.grid(row=0, column=3)
lbl4.grid(row=1, column=0)
lbl5.grid(row=1, column=1)
lbl6.grid(row=1, column=2)
lbl7.grid(row=1, column=3)
lbl8.grid(row=2, column=0)
lbl9.grid(row=2, column=1)
lbl10.grid(row=2, column=2)
lbl11.grid(row=2, column=3)
lbl12.grid(row=3, column=0)
lbl13.grid(row=3, column=1)
lbl14.grid(row=3, column=2)
lbl15.grid(row=3, column=3)

lbl0["font"] = FONT
lbl1["font"] = FONT
lbl2["font"] = FONT
lbl3["font"] = FONT
lbl4["font"] = FONT
lbl5["font"] = FONT
lbl6["font"] = FONT
lbl7["font"] = FONT
lbl8["font"] = FONT
lbl9["font"] = FONT
lbl10["font"] = FONT
lbl11["font"] = FONT
lbl12["font"] = FONT
lbl13["font"] = FONT
lbl14["font"] = FONT
lbl15["font"] = FONT

info_lbl["font"] = FONT

info_lbl.grid(row=4, column=0, columnspan=4)

def initialise():
    global board

    lbl0["text"] = ""
    lbl1["text"] = ""
    lbl2["text"] = ""
    lbl3["text"] = ""
    lbl4["text"] = ""
    lbl5["text"] = ""
    lbl6["text"] = ""
    lbl7["text"] = ""
    lbl8["text"] = ""
    lbl9["text"] = ""
    lbl10["text"] = ""
    lbl11["text"] = ""
    lbl12["text"] = ""
    lbl13["text"] = ""
    lbl14["text"] = ""
    lbl15["text"] = ""

    info_lbl["text"] = ""

    with open("board_states.txt", "w") as f, \
    open("console.txt", "w") as console:
        f.write("")
        console.write("")
    board = [
        [],
        [],
        [],
        []
    ]

    for list in board:
        list.append(empty_tile)
        list.append(empty_tile)
        list.append(empty_tile)
        list.append(empty_tile)

    while True:
        row_0 = randint(0,3)
        row_1 = randint(0,3)
        column_0 = randint(0,3)
        column_1 = randint(0,3)
        if row_0 == row_1 and column_0 == column_1:
            continue
        else:
            break

    board[row_0][column_0] = '| 2 |'
    board[row_1][column_1] = '| 2 |'

def write(text):
    with open("console.txt", "a") as f:
        print(text, file=f)


def move_left():
    def merge(num0: int, num1: int, num2: int, num3: int, merged: list):

        if (merged[0] is False and merged[1] is False) and (num0 == num1 and num0 != 0):
            num0 = num0 + num1
            num1 = 0
            merged[0] = True

        if (merged[1] is False and merged[2] is False) and (num1 == num2 and num1 != 0):
            num1 = num1 + num2
            num2 = 0
            merged[1] = True

        if (merged[2] is False and merged[3] is False) and (num2 == num3 and num2 != 0):
            num2 = num2 + num3
            num3 = 0
            merged[2] = True

        return {"num0": num0, "num1": num1, "num2":num2, "num3": num3, "merged": merged}



    loc_board = board
    new_loc_board = [
        [],
        [],
        [],
        []
    ]

    for index, row in enumerate(loc_board):
        merged = [False, False, False, False]
        num0 = 0 if row[0] == empty_tile else int(row[0].replace("| ", "") \
                                                    .replace(" |", ""))
        num1 = 0 if row[1] == empty_tile else int(row[1].replace("| ", "") \
                                                    .replace(" |", ""))
        num2 = 0 if row[2] == empty_tile else int(row[2].replace("| ", "") \
                                                    .replace(" |", ""))
        num3 = 0 if row[3] == empty_tile else int(row[3].replace("| ", "") \
                                                    .replace(" |", ""))

        result = merge(num0, num1, num2, num3, merged)
        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]



        merged_after_move = []
        row_after_move = []

        if num0 != 0:
            row_after_move.append(num0)
            merged_after_move.append(merged[0])

        if num1 != 0:
            row_after_move.append(num1)
            merged_after_move.append(merged[1])

        if num2 != 0:
            row_after_move.append(num2)
            merged_after_move.append(merged[2])

        if num3 != 0:
            row_after_move.append(num3)
            merged_after_move.append(merged[3])

        while len(row_after_move) < 4:
            row_after_move.append(0)
            merged_after_move.append(False)

        num0 = row_after_move[0]
        num1 = row_after_move[1]
        num2 = row_after_move[2]
        num3 = row_after_move[3]


        result = merge(num0, num1, num2, num3, merged_after_move)
        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]

        num0 = empty_tile if num0 == 0 else f"| {num0} |"
        num1 = empty_tile if num1 == 0 else f"| {num1} |"
        num2 = empty_tile if num2 == 0 else f"| {num2} |"
        num3 = empty_tile if num3 == 0 else f"| {num3} |"

        new_row = [num0, num1, num2, num3]


        new_loc_board[index] = new_row

    return new_loc_board


def move_right():
    def merge(num0: int, num1: int, num2: int, num3: int, merged: list):
        if (merged[2] is False and merged[3] is False) and (num3 == num2 and num3 != 0):
            num3 = num3 + num2
            num2 = 0
            merged[3] = True

        if (merged[1] is False and merged[2] is False) and (num2 == num1 and num2 != 0):
            num2 = num2 + num1
            num1 = 0
            merged[2] = True

        if (merged[0] is False and merged[1] is False) and (num1 == num0 and num1 != 0):
            num1 = num1 + num0
            num0 = 0
            merged[1] = True

        return {"num0": num0, "num1": num1, "num2": num2, "num3": num3, "merged": merged}

    loc_board = board
    new_loc_board = [[], [], [], []]

    for index, row in enumerate(loc_board):
        merged = [False, False, False, False]
        num0 = 0 if row[0] == empty_tile else int(row[0].replace("| ", "").replace(" |", ""))
        num1 = 0 if row[1] == empty_tile else int(row[1].replace("| ", "").replace(" |", ""))
        num2 = 0 if row[2] == empty_tile else int(row[2].replace("| ", "").replace(" |", ""))
        num3 = 0 if row[3] == empty_tile else int(row[3].replace("| ", "").replace(" |", ""))

        result = merge(num0, num1, num2, num3, merged)


        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]

        new_row = []
        new_merged = []

        if num3 != 0:
            new_row.insert(0, num3)
            new_merged.insert(0, merged[3])

        if num2 != 0:
            new_row.insert(0, num2)
            new_merged.insert(0, merged[2])

        if num1 != 0:
            new_row.insert(0, num1)
            new_merged.insert(0, merged[1])

        if num0 != 0:
            new_row.insert(0, num0)
            new_merged.insert(0, merged[0])

        while len(new_row) < 4:
            new_row.insert(0, 0)
            new_merged.insert(0, False)

        num0 = new_row[0]
        num1 = new_row[1]
        num2 = new_row[2]
        num3 = new_row[3]

        result = merge(num0, num1, num2, num3, new_merged)

        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]

        num0 = empty_tile if num0 == 0 else f"| {num0} |"
        num1 = empty_tile if num1 == 0 else f"| {num1} |"
        num2 = empty_tile if num2 == 0 else f"| {num2} |"
        num3 = empty_tile if num3 == 0 else f"| {num3} |"

        row = [num0, num1, num2, num3]
        new_loc_board[index] = row

    return new_loc_board

def move_up():

    def merge(num0: int, num1: int, num2: int, num3: int, merged: list):

        if (merged[0] is False and merged[1] is False) and (num0 == num1 and num0 != 0):
            num0 = num0 + num1
            num1 = 0
            merged[0] = True

        if (merged[1] is False and merged[2] is False) and (num1 == num2 and num1 != 0):
            num1 = num1 + num2
            num2 = 0
            merged[1] = True

        if (merged[2] is False and merged[3] is False) and (num2 == num3 and num2 != 0):
            num2 = num2 + num3
            num3 = 0
            merged[2] = True

        return {"num0": num0, "num1": num1, "num2":num2, "num3": num3, "merged": merged}

    def move_and_merge(column):
        merged = [False, False, False, False]
        indx0 = column[0]
        indx1 = column[1]
        indx2 = column[2]
        indx3 = column[3]

        num0 = 0 if indx0 == empty_tile else int(indx0.replace("| ", "")\
        .replace(" |", ""))
        num1 = 0 if indx1 == empty_tile else int(indx1.replace("| ", "")\
        .replace(" |", ""))
        num2 = 0 if indx2 == empty_tile else int(indx2.replace("| ", "")\
        .replace(" |", ""))
        num3 = 0 if indx3 == empty_tile else int(indx3.replace("| ", "")\
        .replace(" |", ""))

        result = merge(num0, num1, num2, num3, merged)
        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]

        merged_after_move = []
        row_after_move = []

        if num0 != 0:
            row_after_move.append(num0)
            merged_after_move.append(merged[0])

        if num1 != 0:
            row_after_move.append(num1)
            merged_after_move.append(merged[1])

        if num2 != 0:
            row_after_move.append(num2)
            merged_after_move.append(merged[2])

        if num3 != 0:
            row_after_move.append(num3)
            merged_after_move.append(merged[3])

        while len(row_after_move) < 4:
            row_after_move.append(0)
            merged_after_move.append(False)

        num0 = row_after_move[0]
        num1 = row_after_move[1]
        num2 = row_after_move[2]
        num3 = row_after_move[3]

        result = merge(num0, num1, num2, num3, merged_after_move)

        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]

        num0 = empty_tile if num0 == 0 else f"| {num0} |"
        num1 = empty_tile if num1 == 0 else f"| {num1} |"
        num2 = empty_tile if num2 == 0 else f"| {num2} |"
        num3 = empty_tile if num3 == 0 else f"| {num3} |"
        return [num0, num1, num2, num3]

    loc_board = board
    new_loc_board = [[],[],[],[]]

    for i, _ in enumerate(new_loc_board):
        for _ in range(4):
            new_loc_board[i].append(empty_tile)

    column0 = [loc_board[0][0], loc_board[1][0], loc_board[2][0], loc_board[3][0]]
    column1 = [loc_board[0][1], loc_board[1][1], loc_board[2][1], loc_board[3][1]]
    column2 = [loc_board[0][2], loc_board[1][2], loc_board[2][2], loc_board[3][2]]
    column3 = [loc_board[0][3], loc_board[1][3], loc_board[2][3], loc_board[3][3]]

    column0 = move_and_merge(column0)
    column1 = move_and_merge(column1)
    column2 = move_and_merge(column2)
    column3 = move_and_merge(column3)

    for i, v in enumerate(column0):
        new_loc_board[i][0] = v
    for i, v in enumerate(column1):
        new_loc_board[i][1] = v
    for i, v in enumerate(column2):
        new_loc_board[i][2] = v
    for i, v in enumerate(column3):
        new_loc_board[i][3] = v

    return new_loc_board




def move_down():

    def merge(num0: int, num1: int, num2: int, num3: int, merged: list):

        if (merged[2] is False and merged[3] is False) and (num2 == num3 and num2 != 0):
            num3 = num2 + num3
            num2 = 0
            merged[3] = True

        if (merged[1] is False and merged[2] is False) and (num1 == num2 and num1 != 0):
            num2 = num1 + num2
            num1 = 0
            merged[2] = True

        if (merged[0] is False and merged[1] is False) and (num0 == num1 and num0 != 0):
            num1 = num0 + num1
            num0 = 0
            merged[1] = True

        return {"num0": num0, "num1": num1, "num2":num2, "num3": num3, "merged": merged}

    def move_and_merge(column):
        merged = [False, False, False, False]
        indx0 = column[0]
        indx1 = column[1]
        indx2 = column[2]
        indx3 = column[3]

        num0 = 0 if indx0 == empty_tile else int(indx0.replace("| ", "")\
        .replace(" |", ""))
        num1 = 0 if indx1 == empty_tile else int(indx1.replace("| ", "")\
        .replace(" |", ""))
        num2 = 0 if indx2 == empty_tile else int(indx2.replace("| ", "")\
        .replace(" |", ""))
        num3 = 0 if indx3 == empty_tile else int(indx3.replace("| ", "")\
        .replace(" |", ""))

        result = merge(num0, num1, num2, num3, merged)
        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]

        merged_after_move = []
        row_after_move = []

        if num3 != 0:
            row_after_move.insert(0, num3)
            merged_after_move.insert(0, merged[3])

        if num2 != 0:
            row_after_move.insert(0, num2)
            merged_after_move.insert(0, merged[2])

        if num1 != 0:
            row_after_move.insert(0, num1)
            merged_after_move.insert(0, merged[1])

        if num0 != 0:
            row_after_move.insert(0, num0)
            merged_after_move.insert(0, merged[0])

        while len(row_after_move) < 4:
            row_after_move.insert(0, 0)
            merged_after_move.insert(0, False)

        num0 = row_after_move[0]
        num1 = row_after_move[1]
        num2 = row_after_move[2]
        num3 = row_after_move[3]

        result = merge(num0, num1, num2, num3, merged_after_move)

        num0 = result["num0"]
        num1 = result["num1"]
        num2 = result["num2"]
        num3 = result["num3"]
        merged = result["merged"]

        num0 = empty_tile if num0 == 0 else f"| {num0} |"
        num1 = empty_tile if num1 == 0 else f"| {num1} |"
        num2 = empty_tile if num2 == 0 else f"| {num2} |"
        num3 = empty_tile if num3 == 0 else f"| {num3} |"
        return [num0, num1, num2, num3]

    loc_board = board
    new_loc_board = [[],[],[],[]]
    for i, _ in enumerate(new_loc_board):
        for _ in range(4):
            new_loc_board[i].append(empty_tile)

    column0 = [loc_board[0][0], loc_board[1][0], loc_board[2][0], loc_board[3][0]]
    column1 = [loc_board[0][1], loc_board[1][1], loc_board[2][1], loc_board[3][1]]
    column2 = [loc_board[0][2], loc_board[1][2], loc_board[2][2], loc_board[3][2]]
    column3 = [loc_board[0][3], loc_board[1][3], loc_board[2][3], loc_board[3][3]]

    column0 = move_and_merge(column0)
    column1 = move_and_merge(column1)
    column2 = move_and_merge(column2)
    column3 = move_and_merge(column3)

    for i, v in enumerate(column0):
        new_loc_board[i][0] = v
    for i, v in enumerate(column1):
        new_loc_board[i][1] = v
    for i, v in enumerate(column2):
        new_loc_board[i][2] = v
    for i, v in enumerate(column3):
        new_loc_board[i][3] = v

    return new_loc_board


def has_won():
    for row in board:
        for tile in row:
            if tile == "| 2048 |":
                return True
    return False



def colour():
    lbl0["bg"] = colour_dict[lbl0["text"]]
    lbl1["bg"] = colour_dict[lbl1["text"]]
    lbl2["bg"] = colour_dict[lbl2["text"]]
    lbl3["bg"] = colour_dict[lbl3["text"]]
    lbl4["bg"] = colour_dict[lbl4["text"]]
    lbl5["bg"] = colour_dict[lbl5["text"]]
    lbl6["bg"] = colour_dict[lbl6["text"]]
    lbl7["bg"] = colour_dict[lbl7["text"]]
    lbl8["bg"] = colour_dict[lbl8["text"]]
    lbl9["bg"] = colour_dict[lbl9["text"]]
    lbl10["bg"] = colour_dict[lbl10["text"]]
    lbl11["bg"] = colour_dict[lbl11["text"]]
    lbl12["bg"] = colour_dict[lbl12["text"]]
    lbl13["bg"] = colour_dict[lbl13["text"]]
    lbl14["bg"] = colour_dict[lbl14["text"]]
    lbl15["bg"] = colour_dict[lbl15["text"]]





def check_for_empty_tile():
    for row in board:
        if empty_tile in row:
            return True  # Found an empty tile, the board is not full


    return False

def all_tiles_filled(current_board_state):
    running_flag = True

    def stop_running():
        nonlocal running_flag
        running_flag = False

    root.after(5000, stop_running)
    current_board_to_modify = current_board_state

    if check_for_empty_tile() is False:
        return False

    # Check if the set of elements in the current board is equal to the set after the move
    after_right = move_right()
    after_left = move_left()
    after_up = move_up()
    after_down = move_down()

    if not running_flag:
        return None


    global board

    if current_board_to_modify != after_right:
        return False
    if current_board_to_modify != after_left:
        return False
    if current_board_to_modify != after_down:
        return False
    if current_board_to_modify != after_up:
        return False


    return True

def print_board(func_name: str, write: bool = True, clear=True):
    if clear is True:
        with open("console.txt", "w") as f:
            f.write("")
    if write is True:
        with open("board_states.txt", "a") as f:
            f.write("\n" + "-"*30 + "\n")
            for row in board:
                f.write("".join(row) + '\n')

    if all_tiles_filled(board) is True:
        info_lbl["text"] = "The game is over. There are no more moves"
    elif has_won() is True:
        info_lbl["text"] = "You have won. You have created the 2048 tile"
    else:
        info_lbl["text"] = ""

    lbl0["text"] = board[0][0]
    lbl1["text"] = board[0][1]
    lbl2["text"] = board[0][2]
    lbl3["text"] = board[0][3]
    lbl4["text"] = board[1][0]
    lbl5["text"] = board[1][1]
    lbl6["text"] = board[1][2]
    lbl7["text"] = board[1][3]
    lbl8["text"] = board[2][0]
    lbl9["text"] = board[2][1]
    lbl10["text"] = board[2][2]
    lbl11["text"] = board[2][3]
    lbl12["text"] = board[3][0]
    lbl13["text"] = board[3][1]
    lbl14["text"] = board[3][2]
    lbl15["text"] = board[3][3]

    colour()




def w_key_pressed():
    global board

    board = move_up()
    print_board(w_key_pressed.__name__, write=False)
    root.after(500, lambda: move_key_clicked_cont())

def a_key_pressed():
    global board
    board = move_left()
    print_board(a_key_pressed.__name__, write=False)
    root.after(500, lambda: move_key_clicked_cont())

def s_key_pressed():
    global board

    board = move_down()
    print_board(s_key_pressed.__name__, write=False)
    root.after(500, lambda: move_key_clicked_cont())

def d_key_pressed():
    global board

    board = move_right()
    print_board(d_key_pressed.__name__, write=False)
    root.after(500, lambda: move_key_clicked_cont())

def move_key_clicked_cont():
    board_filled = all_tiles_filled(board)
    free_space = check_for_empty_tile()

    if has_won() is True:
        info_lbl["text"] = "You have created the 2048 tile. Well done!"
        return

    if board_filled is True:
        info_lbl["text"] = "The game is over. There are no more moves"

    if free_space is True:
        while True:
            row = randint(0,3)
            column = randint(0, 3)
            if board[row][column] == empty_tile:
                board[row][column] = "| 2 |"
                break



    print_board(move_key_clicked_cont.__name__, )

    check_console()

def check_console():
    global board, start_time, stop_time
    with open("console.txt", "r") as f:
        try:
            lines = f.readlines()
            line = lines[-1]
        except IndexError:
            return
        if "clear_tile" in line:
            line.replace("clear_tile", "")
            try:
                choords = lines[1].split("|")
                row=int(choords[0].strip())
                column=int(choords[1].strip())
                board[row][column] = empty_tile
                print_board(check_console.__name__)
            except:
                msg.showerror("Chords error", f"The chords u provided were invalid. try again: \n Chords: {lines[1]}")
        elif "clear" in line:
            board = [
                [],
                [],
                [],
                []
            ]
            for row in board:
                row.append(empty_tile)
                row.append(empty_tile)
                row.append(empty_tile)
                row.append(empty_tile)

            print_board(check_console.__name__)
        elif "timer start" in line:
            start_time = dt.now()
        elif "timer stop" in line:
            stop_time = dt.now()
        elif "timer get" in line:
            try:
                if stop_time is None:
                    msg.showerror("Timer error", "The timer has not been stopped")
                    return

                elif start_time is None:
                    msg.showerror("Timer error", "The timer has not been started")
                    return

                time = stop_time-start_time
                time = time.strftime("%h:%m:%s:%f")
                msg.showinfo("Timer result", f"Your timer lasted for: \n{time}. ")
                start_time = None
                stop_time = None

            except Exception as e:
                msg.showerror("Timer error", f"Either start time or end time is unbound. \n{e}")
        else:
            print("else statement")
            try:
                lines = f.readlines()
                line = lines[-2]
                if "add_tile " in line:
                    line = line.replace("add_tile ", "")
                    line = int(line.strip())
                    try:
                        choords = lines[-1].split("|")
                        row=int(choords[0].strip())
                        column=int(choords[1].strip())
                        board[row][column] = f"| {line} |"
                    except:
                        board[0][0] = f"| {line} |"
                    lines.pop(-1)
                print_board(check_console.__name__)

            except IndexError:
                return

    with open("console.txt", "w") as f:
        try:
            lines.pop(-1)
        except IndexError:
            return
        f.writelines(lines)



def key_clicked(key: str):
    global processing_key

    if processing_key:
        return

    else:
        processing_key = True

    if key == 'w':
        w_key_pressed()
    elif key == 'a':
        a_key_pressed()
    elif key == 's':
        s_key_pressed()
    elif key == 'd':
        d_key_pressed()
    elif key == 'enter':
        print_board(key_clicked.__name__)
    elif key == 'escape':
        initialise()
        print_board(key_clicked.__name__)
    elif key == 'p':
        check_console()

    root.bind('w', lambda event: key_clicked('w'))
    root.bind('<Up>', lambda event: key_clicked('w'))
    root.bind('a', lambda event: key_clicked('a'))
    root.bind('<Left>', lambda event: key_clicked('a'))
    root.bind('s', lambda event: key_clicked('s'))
    root.bind('<Down>', lambda event: key_clicked('s'))
    root.bind('d', lambda event: key_clicked('d'))
    root.bind('<Right>', lambda event: key_clicked('d'))


    def reset_processing_key():
        global processing_key
        processing_key = False

    root.after(500, reset_processing_key)


try:
    initialise()
    print_board("__main__")
    root.bind('w', lambda event: key_clicked('w'))
    root.bind('a', lambda event: key_clicked('a'))
    root.bind('s', lambda event: key_clicked('s'))
    root.bind('d', lambda event: key_clicked('d'))
    root.bind('<Up>', lambda event: key_clicked('w'))
    root.bind('<Left>', lambda event: key_clicked('a'))
    root.bind('<Down>', lambda event: key_clicked('s'))
    root.bind('<Right>', lambda event: key_clicked('d'))
    root.bind('<Return>', lambda event: key_clicked('enter'))
    root.bind('<Escape>', lambda event: key_clicked('escape'))
    root.bind('p', lambda event: key_clicked('p'))


except KeyboardInterrupt:
    pass

except Exception as e:
    traceback_str = traceback.format_exc()  # Get the traceback as a string
    write(traceback_str)
    exit()

root.mainloop()

