class Player:
    def __init__(self,id, name):
        self.Id = id
        self.Name = name
        self.IsCalling = False
        self.__cards = []

    def AddCardToPlayer(self, card):
        self.__cards.append(card)

    def RemoveCardFromPlayer(self, card):
        self.__cards.remove(card)
    
    def RemainingCardsCount(self):
        return len(self.__cards)

    