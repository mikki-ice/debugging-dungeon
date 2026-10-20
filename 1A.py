# premade map, list, each row is a string, each char is a column. top left is DUNGEON[0][0], bottom right DUNGEON[10][10], center DUNGEON[5][5]
DUNGEON = [
    "■■■■■■■■■■■",
    "■.△.■..▽..■", 
    "■■■.■.■■■.■", # to find 4th field here, first we have to choose 3rd row and than 4th character in list. so Y3, X4 (minus one because zero indexed)
    "■...■..▷■.■",  
    "■◁■■■■■.■.■",
    "■...▽...■.■", 
    "■.■■■■■■■.■",
    "■...◁..▷..■",
    "■.■■■■■.■■■",
    "■.■■■■.△■■■", # second position here (dot) is Y[9] X[2]
    "■■■■■■■■■■■",
]
# X = map width
# Y = map heigth


print(DUNGEON[10][10])
lengthY = len(DUNGEON) - 1
print("lenY: ", lengthY)
lengthX = len(DUNGEON[0]) - 1
print("lenZ: ", lengthX)

y = enumerate(DUNGEON, 0)
print(y)

player_pos_y = 3
player_pos_x = 1


for posY, line in enumerate(DUNGEON, 0):
    for posX, tile in enumerate(line, 0):
        if posY == player_pos_y and posX == player_pos_x:
            print("⏵", end="")
        else:
            print(tile, end="")
    print()

print("⏵   ⯈")
print("⏴   ⯇")
print("⏶   ⯅")
print("⏷   ⯆")


DUNGEON = [
    "           XXXXXXXXXXXXXXX",
    "           XXXXXXXXXXXXXXX",
    "           XXXXXXXXXXXXXXX",
    "           XXXXXXXXXXXXXXX",
    "           XXXXXXXXXXXXXXX",
    "   XXXXXXXXXXXXXXXXXXXXXXX",
    "   XXXXXXXXXXXXXXXXXXXXXXX",
    "   XXXXXXXXXXXXXXXXXXXXXXXYYYYYYYYY",
    "   XXXXXXXXXXXXXXXXXXXXXXXYYYYYYYYY",
    "   XXXXXXXXXXXXXXXXYYYYYYYYYYYYYYYY",
    "   XXXXXXXXXYYYYYYYYYYYYYYYYYYYYYYY",
    "   XXXXXXXXXYYYYYYYYYYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYY",
    "            YYYYYYYYYYYYYYY",
]


