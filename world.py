# premade map, list, each row is a string, each char is a column. top left is DUNGEON[0][0], bottom right DUNGEON[10][10], center DUNGEON[5][5]
DUNGEON = [
    "###########",
    "#...#.....#", 
    "###.#.###.#", # to find 4th field here, first we have to choose 3rd row and than 4th character in list. so Y3, X4 (minus one because zero indexed)
    "#...#...#.#",  
    "#.#####.#.#",
    "#.......#.#", 
    "#.#######.#",
    "#.........#",
    "#.#####.###",
    "#.####..###", # second position here (dot) is Y[9] X[2]
    "##########Q",
]
# Y = line, whole string, map heigth 
# X = one char in line string, map width

class Map:
    def __init__(self, start_pos_x=1, start_pos_y=1):
        self._map = DUNGEON
        self._start_pos_x = start_pos_x
        self._start_pos_y = start_pos_y
        self._player_pos_x = start_pos_x
        self._player_pos_y = start_pos_y

    def is_walkable(self, x, y):
        max_y = len(self._map) - 1
        max_x = len(self._map[0]) - 1

        # checks if in range
        if not 0 <= y <= max_y:
            return False
        if not 0 <= x <= max_x:
            return False
        # check if its a wall
        if self._map[y][x] == ".":
            return True
        return False

    def display_map(self):
        mini_map = ""
        for pos_y, line in enumerate(self._map):
            for pos_x, tile in enumerate(line):
                if pos_y == self._player_pos_y and pos_x == self._player_pos_x:
                    mini_map += ">"
                else:
                    mini_map += tile
            mini_map += "\n"
        return mini_map
        
if __name__ == "__main__":               
    print(DUNGEON[10][10])
    lengthY = len(DUNGEON) - 1
    print("lenY: ", lengthY)
    lengthX = len(DUNGEON[0]) - 1
    print("lenZ: ", lengthX)
    map1 = Map()

    print(map1.display_map())