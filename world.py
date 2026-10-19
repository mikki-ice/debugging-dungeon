# premade map, list, each row is a string, each char is a column. top left is DUNGEON[0][0], bottom right DUNGEON[10][10], center DUNGEON[5][5]
DUNGEON = [
    "###########",
    "#...#.....#", 
    "###.B.###.#", # to find 4th field here, first we have to choose 3rd row and than 4th character in list. so Y2, X4 (minus one because zero indexed)
    "#...#...#.#",  
    "#.#####.#.#",
    "#.......#.#", 
    "#.#######.#",
    "#.........#",
    "#.#####.###",
    "#.####..###", # second position here (dot) is Y[9] X[2]
    "###########",
]
# Y = line, whole string, map heigth 
# X = one char in line string, map width

class Map:
    # list of facing directions
    DIRECTIONS = ("N", "E", "S", "W")

    def __init__(self, start_pos_x=1, start_pos_y=1):
        self._map = DUNGEON
        self._start_pos_x = start_pos_x
        self._start_pos_y = start_pos_y
        self._player_pos_x = start_pos_x
        self._player_pos_y = start_pos_y
        self._direction = self.DIRECTIONS[1]

    def is_walkable(self, x, y):
        max_y = len(self._map) - 1
        max_x = len(self._map[0]) - 1

        # checks if in range
        if not 0 <= y <= max_y:
            return False
        if not 0 <= x <= max_x:
            return False
        # check if its a path
        if self._map[y][x] == "." or self._map[y][x] == "B":
            return True
        return False

    def is_boss_tile(self):
        x = self._player_pos_x
        y = self._player_pos_y
        if self._map[y][x] == "B":
            return True
        return False

    # shows map
    def display_map(self):
        mini_map = ""
        face = ""
        for pos_y, line in enumerate(self._map):
            for pos_x, tile in enumerate(line):
                if pos_y == self._player_pos_y and pos_x == self._player_pos_x:
                    if self._direction == "N":
                        face = "^"
                    if self._direction == "S":
                        face = "v"
                    if self._direction == "E":
                        face = ">"
                    if self._direction == "W":
                        face = "<"        
                    mini_map += face
                else:
                    mini_map += tile
            mini_map += "\n"
        return mini_map

    # turning face
    def turn_right(self):
        facing_now = self.DIRECTIONS.index(self._direction)
        turning = (facing_now + 1) % 4
        self._direction = self.DIRECTIONS[turning]

    def turn_left(self):
        facing_now = self.DIRECTIONS.index(self._direction)
        turning = (facing_now - 1) % 4
        self._direction = self.DIRECTIONS[turning]

    # checks tile in front of player, if not a wall, move
    def move_forward(self):
        front_x = self._player_pos_x
        front_y = self._player_pos_y
        if self._direction == "N":
            front_y = front_y - 1
        elif self._direction == "E":
            front_x = front_x + 1
        elif self._direction == "S":
            front_y = front_y + 1
        elif self._direction == "W":
            front_x = front_x - 1
        if self.is_walkable(front_x, front_y):
            self._player_pos_y = front_y
            self._player_pos_x = front_x
            return True
        else:
            return False


# testing random things
if __name__ == "__main__":         

    print(DUNGEON[10][10])
    lengthY = len(DUNGEON) - 1
    print("lenY: ", lengthY)
    lengthX = len(DUNGEON[0]) - 1
    print("lenZ: ", lengthX)
    map1 = Map()
    print(map1.display_map())
    print(map1.move_forward())
    print(map1._direction)
    print(DUNGEON[2][4])