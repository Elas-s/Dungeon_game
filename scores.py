import sqlite3
import os
DB_PATH = os.environ.get("DB_PATH","scores.db")

def create_table():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("CREATE TABLE if NOT EXISTS scores(name TEXT, gold INTEGER, survived INTEGER)")
    connection.close()

def save_score(name, gold, survived):
    create_table()
    connection = sqlite3.connect(DB_PATH)
    connection.execute("INSERT INTO scores (name,gold,survived) VALUES (?,?,?)", (name,gold,survived))
    connection.commit()
    connection.close()

def top_scores():
    connection = sqlite3.connect(DB_PATH)
    rows = connection.execute("SELECT name, gold FROM scores WHERE survived = 1 ORDER BY gold DESC LIMIT 5").fetchall()
    connection.close()
    return rows

def show_top_scores():
    rows = top_scores()
    print("\n🏆 HALL OF FAME 🏆")
    for name, gold in rows:
        print(name, "-", gold, "gold")

def total_games():
    connection = sqlite3.connect(DB_PATH)
    total =connection.execute("SELECT COUNT(*) FROM scores").fetchone()[0]
    connection.close()
    return total

def average_gold():
    connection = sqlite3.connect(DB_PATH)
    average = connection.execute("SELECT AVG(gold) FROM scores").fetchone()[0]
    connection.close()
    return average

#---------------- New hall of Fame--------------

def most_active_player():
    connection = sqlite3.connect(DB_PATH)
    top_played = connection.execute("SELECT LOWER(name) AS player, COUNT(*) AS games FROM scores GROUP BY player ORDER BY games DESC LIMIT 1").fetchone()
    connection.close()
    return top_played