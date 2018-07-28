

class Planet:
    id = 0;
    x =0;
    y =0;
    radius =0;
    dockingSpots =0;
    currentProduction =0;
    remainingProduction =0;
    health =0;
    #owner;
    ifFull = False;

    def __init__(self, id, x, y, radius, dockingSpots, currentProduction, remainingProduction, health, owner, isFull):
       self.owner = owner;
       self.id = id;
       self.x = x;
       self.y = y;
       self.radius = radius;
       self.dockingSpots = dockingSpots;
       self.currentProduction = currentProduction;
       self.remainingProduction = remainingProduction;
       self.health = health;
       self.isFull = isFull;


    


