import datetime
from entities.Planet import Planet
from entities.Player import Player
from entities.Ship import Ship

class HaliteStates:
    # every entry corresponds to one turn, so it is a list of lists
    # if the files get too big, we can take care of compression



    def __init__(self):
        self.timestamp = datetime.datetime.now();
        self.players =[]
        self.ships = [];
        self.planets = [];
        self.commands = []

    def addPlayer(self, playerList):
        self.players.append(playerList);


    def addShips(self, shipList):
        self.ships.append(shipList);

    def addPlanets(self, planetList):
        self.planets.append(planetList);

    def addCommand(self, command):
        self.commands.append(command)



