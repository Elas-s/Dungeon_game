# 🏰 Dungeon Game

A funny text adventure game written in Python. Explore a dungeon, fight (or sneak past) monsters, collect gold and potions, and try to escape alive... ideally with your pants intact.

## 🎮 How to play

You start at the dungeon entrance and choose one of three doors. Then you go through 5 rooms, each with a monster. In every room you decide:

- **FIGHT**: take some damage, but win gold (and maybe a potion)
- **SNEAK**: you might slip past... or you might not 👀

Before a fight you can drink a potion for +30 health. Survive all 5 rooms to escape with your gold!

Every message is picked at random, so no two games are the same.

## ▶️ How to run it

You need [Python 3](https://www.python.org/downloads/) installed.

```bash
git clone https://github.com/Elas-s/Dungeon_game.git
cd Dungeon_game
python game.py
```

## 🛠️ What I practised building this

- Variables, `if / elif / else` and `while` loops
- Functions with parameters and return values (`fight()`, `ask()`, `show_stats()`)
- Lists for the inventory and the random messages
- Randomness with the `random` module
- Input validation: the game keeps asking until you give a valid answer
- Debugging and testing rare events
- Git and GitHub for version control

## 🚀 Coming next

- A version with clickable buttons instead of typing
- Saving high scores

