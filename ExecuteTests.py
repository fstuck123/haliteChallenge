

from states.HaliteStates import HaliteStates

from persistence.Files import Files



file = "sample1"
state = HaliteStates();
persistence = Files("/home/fstuck/repros/hunger-games/haliteChallenge/data/");

state.addPlayer(Player(3))

persistence.saveStateRandom(state)


stateLoaded = persistence.accessFile(file)

stateBot = persistence.accessFile("sample")
n=0;


