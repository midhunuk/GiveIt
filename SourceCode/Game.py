import random
import Player
import tabulate

def CreateSinglePlayerGame():
    players = [Player.Player(0,"Myself"), Player.Player(1,"CPU")]
    return players

def ShuffleAndDistributeCard(players, cards):
    numberOfPlayers = len(players)
    random.shuffle(cards)
    while(len(cards) > numberOfPlayers):
        for player in players:
            player.AddCardToPlayer(cards.pop())

def DisplayCurrentGameState(players):
    resultHeader = ["Player Name", "Number of card left"]
    data = []
    for player in players:
        data.append({player.RemainingCardsCount(), player.Name})
    return tabulate.tabulate(data, headers=resultHeader, tablefmt="grid")

