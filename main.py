from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

food_database = {
    "banana": { "calories": 89, "protein": 1.1, "carbs": 23, "fat": 0.3 },
    "chicken breast": { "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6 },
    "rice": { "calories": 130, "protein": 2.4, "carbs": 28, "fat": 0.3 },
    "broccoli": { "calories": 55, "protein": 3.7, "carbs": 11, "fat": 0.6 },
    "egg": { "calories": 68, "protein": 6, "carbs": 0.6, "fat": 4.8 },
    "apple": { "calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2 }
}

from fastapi import HTTPException

@app.get("/food/{name}")
def get_food(name: str):
    print("User searched for:", name)
    food = food_database.get(name.lower())
    if food:
        return { "name": name, "calories": food["calories"] }
    raise HTTPException(status_code=404, detail="Food not found")
