from dataclasses import dataclass
import random
from typing import List
from fastapi import FastAPI, HTTPException
import uvicorn

@dataclass(frozen=True)
class Film:
    title: str
    director: str
    year: int
    actors: List[str]

app = FastAPI()

DATA_FILMS = [
    Film("Drive", "Nicolas Winding Refn", 2011, ["Ryan Gosling", "Carey Mulligan", "Bryan Cranston", "Albert Brooks"]),
    Film("The Dark Knight", "Christopher Nolan", 2008 ,["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Maggie Gyllenhaal", "Gary Oldman", "Michael Caine", "Morgan Freeman"]),
    Film("Interstellar", "Christopher Nolan", 2014, ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Mackenzie Foy", "Michael Caine"]),
    Film("The Gentelmen", "Guy Ritchie", 2019, ["Matthew McConaughey", "Charlie Hunnam", "Henry Golding", "Hugh Grant", "Michelle Dockery", "Jeremy Strong", "Eddie Marsan"]),
    Film("Spider-Man", "Sam Raimi", 2002, ["Tobey Maguire", "Willem Dafoe", "Kirsten Dunst", "James Franco", "Cliff Robertson", "Rosemary Harris", "J.K. Simmons"])
]

@app.get("/")
async def home():
    return {"message": "Welcome to films app!"}

@app.get("/list_of_films")
async def list_of_films():
    return {"Films": DATA_FILMS}

@app.get("/get_by_id/{Index}")
async def get_by_id(Index: int):
    if(Index < 0 or Index > (len(DATA_FILMS)-1)):
        raise HTTPException(404, f"Index {Index} is out of range {len(DATA_FILMS)}.")
    else:
        return {"film": DATA_FILMS[Index]}

@app.get("/movie_for_tonight")
async def random_film():
    return random.choice(DATA_FILMS)

@app.post("/add_film")
async def add_film(film: Film):
    DATA_FILMS.append(film)
    return {"message": f"film '{film.title}' was addded."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
