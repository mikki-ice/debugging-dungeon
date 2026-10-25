# CS50P: Debugging Dungeon
#### Video Demo:  <URL>

## Description
Debugging Dungeon is a simple text-based RPG with a map navigation and random combat encounters. 

Game story is about CS50P students who have finally finished their Final Project and are running pytest as a final check before submission. Suddenly, their code became self-aware! They got trapped inside their own Final Project! Main game objective is to debug code and terminate The Infinite Loop.

## Gameplay
The player navigates a predefined map shaped like Python logo, using [W] to move forward and [A]/[D] to turn. While exploring, there is a 10% chance for random encounter after every successful step. Random encounters are a fights between player and game bugs (monsters). 

Each round starts with player choosing an action: [A] fight, [H] heal, [R] run away. Then monster attacks, and the next round begins. Combat loop ends after victory, defeat or successful escape. The player wins the game by reaching the final boss tile and successfully terminating The Infinite Loop.

### Controls

**Exploration**
- W - Move forward
- A / D - Turn left or right
- C - Character statistics
- QUIT - Exit the game


**Combat**
- A - Attack
- H - Drink Coffee
- R - Run away

## Game Mechanics
### Player and monsters statistics

Player's health is represented by "Sanity Points", while monsters health is called "Integrity". Both uses attack, defense and dexterity as a main combat statistics. Player also gains XP (Python Experience) and level ups.
### Random Damage, Critical Hits and Dodging

Regular damage is calculated using simple formula: attacker's attack minus defender's defense. To make it a bit more random, a damage multiplier between 0.8 and 1.2 is applied.
Critical chance is calculated by multiplying attacker's dexterity by 0.5 to get percentage.
Dodge is calculated by adding 3 to defender's dexterity, but max 50% chance to dodge.
### Python Experience (XP) and leveling
        
After each successful bug termination, player is awarded some Python Experience. Once enough XP has been collected, player levels up. Each level up restores player's Sanity and increases their combat statistics.
### Coffee and healing

Player can use a coffee during combat as a way to regenerate percentage of Sanity (health). Its possible to carry max two coffees. After every four  successful steps on the map, one used coffee is regenerated. 
### Final boss

Final boss uses same mechanics as regular encounters. The only difference is that, because its an Infinite Loop, player cannot run away from a fight. After terminating boss, the game is completed, and our Final Project is finally fixed and bug-free. 


## Project Structure
- **`project.py`** - Displays welcome screen, gets player's name and runs main game loop
- **`player.py`** - Defines the Player class and creates player with given name. Class contains methods for taking damage, healing, managing coffee and leveling up.
- **`monster.py`** - Defines Monster class and **`generate_monster()`** function which uses dictionary of monsters templates to create a new Monster object.
- **`world.py`** - Contains dungeon map as list of strings, with visual design for it. Map is set as a class, allowing for future "list of strings maps" to be used as additional levels. Map class contains logic for movement on a map and checking if tile is walkable (not a wall)
- **`combat.py`** - Handles all combat calculations, start of combat and round loop, combat log and encounter interface
- **`ui.py`** - Contains **`clear_screen()`** function and ANSI escape codes used throughout the project.
- **`test_project.py`** - Tests functions from main project.py file, uses **`monkeypatch`** to control random values and simulates user input.
- **`test_*.py`** - Additional tests for individual modules. Many tests uses **`monkeypatch`** to replace random results with set values so test can be performed.
- **`requirements.txt`** - Contains pip installable libraries needed to run project.

## Design Choices
My original idea was to create a traditional RPG featuring a warrior exploring a labyrinth and fighting skeletons. But I wanted something a bit more original. After struggling with few bugs and errors myself, I decided to implement them as a monsters in my game.

Then I started thinking about the map. Do I want a visible map, or just text-based feedback like "you hit the wall!" without actually seeing a wall? I wanted to see something, to have some visual feedback. Okay, I finally had some visuals, but why to use just randomly generated labyrinth? No, lets make a map shaped like the Python logo! And then I got lost in a rabbit hole of ANSI escape codes and Unicode characters. After making few version i finally had a map that did'n look too bad. My big discovery was that using list of strings is a common way to represents maps in games!

Random encounters were something that I had in my mind from day one. Each step would have a chance to trigger an encounter, similar to walking through tall grass in Pokemon. The challenge was balancing the encounter rate: not too often, but often enough so player can level up before final boss fight.

Object-oriented design was already planned in my head and on paper, while learning about it during my CS50P classes. I knew there will be Monster class for all monster types and Player class. The idea for Map class came later, so I could potentially have multiple levels with different maps.

My original plans for the game were much bigger, with several levels, chests, NPCs and equipment. But I realised that it might be too much to implement and polish properly. Besides, I think the purpose of the Final Project is to show that we, students, understand how to write a code, and not to make huge games/apps. Those ideas are still with me and probably I will expand the game in the future.
        
## Installation and Usage

The game requires Python 3 and the dependencies listed in
`requirements.txt`.

Install dependencies:

```bash
pip install -r requirements.txt
```
To run the game:
```bash
python project.py
```
