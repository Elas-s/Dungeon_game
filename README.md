# 🏰 Dungeon Game

A funny text adventure game written in Python. Explore a dungeon, fight (or sneak past) monsters, collect gold and potions, and try to escape alive... ideally with your pants intact.

## 🎮 How to play

### 🚪 The entrance
You stand before three doors. One smells funky. Pick one:

- **LEFT**: a goblin jumps out and slaps you with a half-eaten fish 🐟 (-20 health)
- **RIGHT**: a treasure chest with 50 gold and a potion ✨
- **STRAIGHT**: a sword and a shield ⚔️ (+20 health). The sword makes your hits stronger, the shield blocks 5 damage from every hit

### 👹 The rooms
Then you go through **5 rooms**, each with a random monster:

| Monster | HP | Their entrance |
|---|---|---|
| Goblin | 20 | Holding a half-eaten sandwich. Annoyed you interrupted lunch |
| Sleep-Deprived Wizard | 20 | Three empty coffee cups. *"I cast... wait, what was I doing?"* |
| Skeleton | 24 | Hasn't had a decent meal in 400 years |
| Zombie | 28 | Looks exhausted. Honestly, same |
| The Mimic | 30 | A beautiful treasure chest. It has teeth. OH NO |
| Troll | 30 | Smells like old cheese and bad decisions (so *that's* the funky smell!) |
| Werewolf | 30 | Howls at the moon. It's indoors. There is no moon |
| Vampire | 30 | Cape flowing dramatically. It practised that entrance |
| Ogre | 30 | Picks its teeth with what appears to be a sword |
| Dragon | 33 | A DRAGON?! Who designed this dungeon?! |
| Karen | 35 | A dragon would have been better |
| Demon | 40 | Crawls out of a portal. Disappointed. You weren't worth the trip |

In every room you choose:

- **FIGHT**: a turn-based battle. Your first hit is automatic, then each turn you **ATTACK**, drink a **POTION** (+30 health), or try to **RUN**. You can only run mid-fight if your health is low or the monster is still strong. No running from a nearly dead Goblin!
- **SNEAK**: slip past safely, make a noise from pure stress (-5 health)... or get caught and have to fight 👀
- **RUN**: a 50/50 chance. Fail, and you slip on absolutely nothing and the fight starts anyway 🍌
- **Anything else**: you hesitate, and the monster bites you for being weird (-15 health)

Beaten monsters drop gold, and sometimes a potion. Before a fight, you can also drink a potion if you have one.

### 🏆 The end
Survive all 5 rooms to escape with your gold! Your score is saved, and the **Hall of Fame** shows the top 5 escapes, how many games have been played and the average gold.

There are over 50 random funny messages, so no two games are the same.

## ▶️ How to run it

You need [Python 3](https://www.python.org/downloads/) installed.

```bash
git clone https://github.com/Elas-s/Dungeon_game.git
cd Dungeon_game
python game.py
```

## 📁 Project structure

| File | What it does |
|---|---|
| `game.py` | The main game: rooms, fights and choices |
| `player.py` | The `Player` class: health, gold, inventory and potions |
| `monsters.py` | All the monsters, with their health, damage and loot |
| `messages.py` | All the funny random messages |
| `scores.py` | Saves and loads high scores with SQLite |

## 🛠️ What I practised building this

- Variables, `if / elif / else` and `while` loops
- Functions with parameters and return values
- **Object-oriented programming**: a `Player` class with its own methods (`take_damage()`, `heal()`, `drink_potion()`...)
- Lists and **dictionaries** (each monster is a dictionary)
- Splitting code into **modules** (separate files that import each other)
- **SQL with SQLite**: saving scores, Hall of Fame (`ORDER BY`, `LIMIT`), total games (`COUNT`) and average gold (`AVG`)
- f-strings for clean output
- Input validation: the game keeps asking until you give a valid answer
- Randomness with the `random` module
- Debugging step by step
- Git and GitHub, with [Conventional Commits](https://www.conventionalcommits.org/)

## 🚀 Coming next

- Automated tests with pytest
- GitHub Actions to run the tests on every push
- A version with clickable buttons instead of typing
