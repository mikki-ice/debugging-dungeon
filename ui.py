# official python logo RGB colors
BLUE = "\033[38;2;48;105;152m"
YELLOW = "\033[38;2;255;212;59m"

# standard colors
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE = "\033[38;2;255;165;0m"

# player arrow colors = font_color;background_color
PLAYER = "\033[1;92;47m"

# logo background
WHITE = "\033[47m"

# reset to default terminal settings
RESET = "\033[0m"

# clears screen \033[2J, 
# moves cursor to the top left \033[H 
# clears scrollback \033[3J 
def clear_screen():
    print("\033[H\033[2J\033[3J", end="")

# testing random things
if __name__ == "__main__":    
    clear_screen()
    print("\033[38;2;255;212;59m yellow \033[0m reseted")

    print(f"{ORANGE}this is bright orange{RESET}")