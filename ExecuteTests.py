

from states.HaliteStates import HaliteStates

from persistence.Files import Files



state = HaliteStates();
print(state.timestamp)


persistence = Files("/home/fstuck/repros/hunger-games/haliteChallenge/data/");
states = persistence.accessFile("sample");


n=0;


