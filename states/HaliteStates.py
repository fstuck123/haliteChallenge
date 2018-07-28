import datetime


class HaliteStates:
    # every entry corresponds to one turn, so it is a list of lists
    # if the files get too big, we can take care of compression
    players =[];
    ships = [];
    planets =[];
    commands =[]


    def __init__(self):
        self.timestamp = datetime.datetime.now();


    def addPlayer(self, playerList):
        self.players.append(playerList);


    def addShips(self, shipList):
        self.ships.append(shipList);

    def addPlanets(self, planetList):
        self.planets.append(planetList);

    def addCommand(self, command):
        self.commands.append(command)



