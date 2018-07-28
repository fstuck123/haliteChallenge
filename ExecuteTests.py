

from states.HaliteStates import HaliteStates

from persistence.Files import Files

from entities.Player import Player



file = "2018-07-28 18:39:14.334851_1"
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


