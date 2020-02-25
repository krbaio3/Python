

class Player:

    def __init__(self, health_points):
        self.health_points = health_points

    def getHealth(self):
        print("Vida", self.health_points)
        return self.health_points
