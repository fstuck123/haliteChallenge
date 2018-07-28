

from states.HaliteStates import HaliteStates

from persistence.Files import Files

from entities.Player import Player



file = "sample1"
state = HaliteStates();
persistence = Files("/home/fstuck/repros/hunger-games/haliteChallenge/data/");
p = Player(4)

'''
playerList =[]
playerList.append(Player(3))
playerList.append(Player(4))
playerList.append(Player(6))
playerList.append(Player(60))
state.addPlayer(playerList)
'''

persistence.file = file
#persistence.saveStateRandom(state)



stateBot = persistence.accessFile(file)
n=0;

haliteSavedStates = persistence.accessFile("sample55")

n =3;
