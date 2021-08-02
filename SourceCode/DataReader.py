import json
import Card

def GetPokemonCards():
    fileName = "CardData\Pokemon\pokedex.json"
    try:
        file = open(fileName, 'r', encoding="utf8")
        pokemonData = json.load(file)
        file.close()
    except:
        print("Error while opening file.")
    
    cards = []
    for pokemon in pokemonData:
        card = Card.Card(pokemon["id"],pokemon["name"]["english"], pokemon["base"])
        cards.append(card)
    return cards