import sqlite3

def save_score(name, gold, survived):
    connection = sqlite3.connect("scores.db")
    connection.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, gold INTEGER, survived INTEGER)")
    connection.execute("INSERT INTO scores (name,gold,survived) VALUES (?,?,?)", (name,gold,survived))
    connection.commit()
    connection.close()

def show_top_scores():
    connection = sqlite3.connect("scores.db")
    rows = connection.execute("SELECT name, gold FROM scores Where survived =1 ORDER BY gold DESC LIMIT 5").fetchall()
    connection.close()
    print("\n🏆 HALL OF FAME 🏆")
    for name, gold in rows:
        print(name, "-", gold, "gold")
def total_games():
    connection = sqlite3.connect("scores.db")
    total =connection.execute("SELECT COUNT(*) FROM scores").fetchone()[0]
    connection.close()
    return total
def average_gold():
    connection = sqlite3.connect("scores.db")
    average = connection.execute("SELECT AVG(gold) FROM scores").fetchone()[0]
    connection.close()
    return average