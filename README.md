![Tests](https://github.com/Elas-s/Dungeon_game/actions/workflows/tests.yml/badge.svg)
# 🏰 Dungeon Game

A funny text adventure game written in Python. Explore a dungeon, fight (or sneak past) monsters, collect gold and potions, and try to escape alive... ideally with your pants intact.

## 🎮 How to play

### 🚪 The entrance
You stand before three doors. One smells funky. Pick one:

- **LEFT**: a goblin jumps out and slaps you with a half-eaten fish 🐟 (-10 health)
- **RIGHT**: a treasure chest with 50 gold and a potion ✨
- **STRAIGHT**: a sword and a shield ⚔️. The sword makes your hits stronger, the shield blocks 5 damage from every hit

You start with **100 health**, and that's also the maximum.

### 👹 The rooms
Then you go through **5 rooms**, each with a random monster:

| Monster | HP | Their entrance |
|---|---|---|
| Goblin | 20 | Holding a half-eaten sandwich. Annoyed you interrupted lunch |
| Sleep-Deprived Wizard | 20 | Three empty coffee cups. *"I cast... wait, what was I doing?"* |
| Skeleton | 24 | Hasn't had a decent meal in 400 years |
| Zombie | 28 | Looks exhausted. Honestly, same |
| Mimic | 30 | A beautiful treasure chest. It has teeth. OH NO |
| Troll | 30 | Smells like old cheese and bad decisions (so *that's* the funky smell!) |
| Werewolf | 30 | Howls at the moon. It's indoors. There is no moon |
| Vampire | 30 | Cape flowing dramatically. It practised that entrance |
| Ogre | 30 | Picks its teeth with what appears to be a sword |
| Dragon | 33 | A DRAGON?! Who designed this dungeon?! |
| Karen | 35 | A dragon would have been better |
| Demon | 40 | Crawls out of a portal. Disappointed. You weren't worth the trip |

In every room you choose:

- **FIGHT**: a turn-based battle. Your first hit is automatic, then each turn you **ATTACK**, drink a **POTION** (+30 health, up to your max of 100), or try to **RUN**. You can only run mid-fight if your health is low or the monster is still strong. No running from a nearly dead Goblin!
- **SNEAK**: slip past safely, make a noise from pure stress (-5 health)... or get caught and have to fight 👀
- **RUN**: a 50/50 chance. Fail, and you slip on absolutely nothing and the fight starts anyway 🍌
- **Anything else**: you hesitate, and the monster bites you for being weird (-15 health)

Beaten monsters drop gold, and sometimes a potion. Before a fight, you can also drink a potion if you have one.

### 🏆 The end
Survive all 5 rooms to escape with your gold! Your score is saved, and the **Hall of Fame** shows the top 5 escapes, how many games have been played, the average gold and the most active player.

There are over 50 random funny messages, so no two games are the same.

## ▶️ How to run it

You need [Python 3](https://www.python.org/downloads/) installed.

```bash
git clone https://github.com/Elas-s/Dungeon_game.git
cd Dungeon_game
python game.py
```

## 🌐 The API

The game also has a **REST API** built with [FastAPI](https://fastapi.tiangolo.com/), so other programs (like a web page) can read the scores as JSON.

This project uses [uv](https://docs.astral.sh/uv/). Start the API with:

```bash
uv run uvicorn api:app --reload
```

Then open http://127.0.0.1:8000/docs to try every endpoint in your browser.

| Endpoint | What it returns |
|---|---|
| `GET /` | A welcome message |
| `GET /scores` | The top 5 escapes, with name and gold |
| `GET /stats` | Games played, average gold and the most active player |

Example answer from `GET /stats`:

```json
{"games": 13, "average_gold": 104.9, "most_active": {"name": "Elass", "games": 5}}
```

## 🧪 Running the tests

```bash
pip install pytest
pytest
```

The tests also run automatically on GitHub every time I push (see the badge at the top).

## 📁 Project structure

| File | What it does |
|---|---|
| `game.py` | The main game: rooms, fights and choices |
| `player.py` | The `Player` class: health, gold, inventory and potions |
| `monsters.py` | All the monsters, with their health, damage and loot |
| `messages.py` | All the funny random messages |
| `scores.py` | Saves and loads high scores with SQLite |
| `api.py` | The FastAPI app with the `/scores` and `/stats` endpoints |
| `test_player.py` | Automated tests for the `Player` class |
| `.github/workflows/tests.yml` | Runs the tests on GitHub on every push |

## 🛠️ What I practised building this

- Variables, `if / elif / else` and `while` loops
- Functions with parameters and return values
- **Object-oriented programming**: a `Player` class with its own methods (`take_damage()`, `heal()`, `drink_potion()`...)
- Lists and **dictionaries** (each monster is a dictionary)
- Splitting code into **modules** (separate files that import each other)
- **SQL with SQLite**: saving scores, Hall of Fame (`ORDER BY`, `LIMIT`), total games (`COUNT`), average gold (`AVG`) and most active player (`GROUP BY`, `LOWER`)
- A **REST API** with FastAPI: JSON endpoints and automatic `/docs`
- f-strings for clean output
- Input validation: the game keeps asking until you give a valid answer
- Randomness with the `random` module
- Debugging step by step
- **Automated testing with pytest**, including test-driven development (red, green, refactor)
- **Continuous integration** with GitHub Actions
- Git and GitHub, with [Conventional Commits](https://www.conventionalcommits.org/)

## 🚀 Coming next

- Saving scores through the API (`POST /scores`) and API tests
- Running everything with **Docker**
- A web page to see the Hall of Fame and play the game in the browser
