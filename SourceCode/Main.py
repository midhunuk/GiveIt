import DataReader
import Game

cards = DataReader.GetPokemonCards()
players = Game.CreateSinglePlayerGame()
Game.ShuffleAndDistributeCard(players, cards)
print(Game.DisplayCurrentGameState(players))