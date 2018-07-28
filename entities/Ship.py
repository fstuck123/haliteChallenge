


class Ship:
    id =0;
    x =0;
    y=0
    radius =0;
    health = 0;
    dockstations =0;
    planetID =0
    thrust = 0;
    angle =0;


    def __init__(self, id, x, y, radius, health, dockstations, planetID):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
        self.health = health
        self.dockstations = dockstations
        self.planetID = planetID



    def addCommand(self, thrust, angle, dock, undock):
        self.thrust = thrust
        self.angle = angle;
        self.dock = dock;
        self.undock = undock;
