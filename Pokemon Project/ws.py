from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
import json 
import requests 

app = FastAPI()

pokemon_list = {}
DATA_URL = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"

class Ability(BaseModel):
    name : str 
    is_hidden : bool 

class Stats(BaseModel):
    name : str 
    base_stat : int 

class Type(BaseModel):
    name : str 

class Pokemon(BaseModel):
    id : int 
    name : str 
    height : int 
    weight : int 
    xp : int 
    image_url : str 
    pokemon_url : str 
    ability : list[Ability]
    stats : list[Stats]
    type : list[Type]

@app.on_event("startup")
def load_pokemon_data():

    response = requests.get(DATA_URL)
    if response.status_code != 200:
        raise Exception("Failed Pokémon")
    
    data = response.json()  
    for pokemon in data:
        pokemon_list[pokemon["id"]] = pokemon

@app.get("/pokemon/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    if pokemon_id in pokemon_list:
        return pokemon_list[pokemon_id]
    raise HTTPException(status_code=404, detail="Pokémon not found")


@app.get("/pokemon")
def get_all_pokemon():
    return pokemon_list[10]
    #return {"pokemon_count": len(pokemon_list), "pokemon": list(pokemon_list.values())}

# Create
@app.post("/pokemon")
def create_pokemon(pokemon: Pokemon):
    if pokemon.id in pokemon_list:
        raise HTTPException(status_code=400, detail="Pokémon with this ID already exists.")
    pokemon_list[pokemon.id] = pokemon.dict()  # Convert to dictionary and add to the list
    return {"message": "Pokémon added successfully", "pokemon": pokemon}

# Update
@app.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: Pokemon):
    if pokemon_id not in pokemon_list:
        raise HTTPException(status_code=404, detail="Pokémon not found.")
    pokemon_list[pokemon_id] = pokemon.dict()  
    return {"message": "Pokémon updated successfully", "pokemon": pokemon}

# Delete
@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    if pokemon_id not in pokemon_list:
        raise HTTPException(status_code=404, detail="Pokémon not found.")
    del pokemon_list[pokemon_id] 
    return {"message": "Pokémon deleted successfully"}