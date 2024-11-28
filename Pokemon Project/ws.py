from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel, HttpUrl, Field  
import json 
import requests 
import timeit

app = FastAPI()

pokemon_dict = {}
DATA_URL = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"

class Ability(BaseModel):
    name : str 
    is_hidden : bool 

class Stats(BaseModel):
    name : str 
    base_stat : int = Field(gt = 0)

class Type(BaseModel):
    name : str 

class Update(BaseModel):
    name : str 
    height : int 
    weight : int 
    xp : int 
    image_url : HttpUrl
    pokemon_url : HttpUrl
    ability : list[Ability]
    stats : list[Stats]
    type : list[Type]

class Pokemon(BaseModel):
    id : int = Field(gt=0)
    name : str 
    height : int = Field(ge = 0)
    weight : int = Field(ge= 0)
    xp : int 
    image_url : HttpUrl
    pokemon_url : HttpUrl
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
        pokemon_dict[pokemon["id"]] = pokemon

@app.get("/pokemon/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    if pokemon_id in pokemon_dict:
        return pokemon_dict[pokemon_id]
    raise HTTPException(status_code=404, detail="Pokémon not found")


@app.get("/pokemon")
def get_all_pokemon():
    return {"pokemon_count": len(pokemon_dict), "pokemon": list(pokemon_dict.values())}


def is_url_accessible(url: str) -> bool:
    try:
        response = requests.head(url, timeout=5)  
        return response.status_code == 200
    except requests.RequestException:
        return False



@app.post("/pokemon")
def create_pokemon(pokemon: Pokemon):
    if pokemon.id in pokemon_dict:
        raise HTTPException(status_code=400, detail="Pokémon with this ID already exists.")
    
    if not is_url_accessible(pokemon.image_url):
        raise HTTPException(status_code=400, detail="Invalid or inaccessible image URL.")
    if not is_url_accessible(pokemon.pokemon_url):
        raise HTTPException(status_code=400, detail="Invalid or inaccessible Pokémon URL.")

    pokemon_dict[pokemon.id] = pokemon.dict()  # Convert to dictionary and add to the list
    return {"message": "Pokemon added", "pokemon": pokemon}


#UPDATE
@app.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: Pokemon):
    if pokemon_id not in pokemon_dict:
        raise HTTPException(status_code=404, detail="Pokémon not found.")
    
    if not is_url_accessible(pokemon.image_url):
        raise HTTPException(status_code=400, detail="Invalid or inaccessible image URL.")
    if not is_url_accessible(pokemon.pokemon_url):
        raise HTTPException(status_code=400, detail="Invalid or inaccessible Pokémon URL.")

    pokemon_dict[pokemon_id] = pokemon.dict()  
    return {"message": "Pokemon updated", "pokemon": pokemon}




#DELETE

@app.delete("/pokemon/{pokemon_id}")
def delete_by_id(pokemon_id : int , pokemon : Pokemon):
    if pokemon_id not in pokemon_dict:
        raise HTTPException(status_code=404, detail = "NOT FOUND.")
    del pokemon_dict[pokemon.id]
    return {"messsage":"Pokemon deleted"}




