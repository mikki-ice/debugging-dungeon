# official python logo RGB colors
BLUE = "\033[38;2;48;105;152m"
YELLOW = "\033[38;2;255;212;59m"

# standard colors
GREEN = "\033[92m"
RED = "\033[91m"

# reset to default terminal settings
RESET = "\033[0m"

# clears screen \033[2J, 
# moves cursor to the top left \033[H 
# clears scrollback \033[3J 
def clear_screen():
    print("\033[H\033[2J\033[3J", end="")

clear_screen()