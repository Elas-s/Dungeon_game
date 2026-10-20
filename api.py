from fastapi import FastAPI
from scores import top_scores, total_games, average_gold, most_active_player, create_table,save_score
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def hello():
    return {"message": "Welcome to the dungeon API"}

@app.get("/scores")
def get_scores():
    result = []
    for name , gold in top_scores():
        result.append({"name": name, "gold": gold})
    return result

@app.get("/stats")
def get_stats():
    if total_games() == 0:
        return {"games": 0,"average_gold": 0,"most_active": None}
    active_name, active_games = most_active_player()
    most_active = {"name": active_name.title(), "games": active_games}
    return {"games": total_games() , "average_gold": round(average_gold(),1) ,"most_active": most_active }
