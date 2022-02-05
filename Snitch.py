import random as random
"""
Class Snitch -> Creates an object which stores an
arbitrary x y z location. Methods are used to update
the x y z location based off of a given newLocation
value, and uses adjustPostion() to adjust
"""
class Snitch():
    """
    X, Y, Z location within 3D space
    """
    x = 0
    y = 0
    z = 0

    """
    Instantiates with new locations given in constructor

    :param newX: Starting X location 
    :param newY: Starting Y location 
    :param newZ: Starting Z location 
    """

    def __init__(self, xLocation, yLocation, zLocation):
        self.x = xLocation
        self.y = yLocation
        self.z = zLocation

    """
    Updates the X location with goal to be reached 
    -> if x < newLocation then move closer by one
    -> otherwise move back one space by one 

    :param newLocation: Goal X to be reached 
    """
    def updatedPosX(self, newLocation):
        if (self.x < newLocation):
            self.x += 1
        else:
            self.x -= 1

    """
    Updates the Y location with goal to be reached 
    -> if y < newLocation then move closer by one
    -> otherwise move back one space by one 

    :param newLocation: Goal Y to be reached 
    """

    def updatedPosY(self, newLocation):
        if (self.y < newLocation):
            self.y += 1
        else:
            self.y -= 1

    """
    Updates the Z location with goal to be reached 
    -> if z < newLocation then move closer by one
    -> otherwise move back one space by one 

    :param newLocation: Goal Z to be reached 
    """

    def updatedPosZ(self, newLocation):
        if (self.z < newLocation):
            self.z += 1
        else:
            self.z -= 1

    """
    Adjusts the position for x y z with the given
    goal locations that are trying to be reached

    :param randomX: x trying to be reached
    :param randomY: y trying to be reached
    :param randomZ: z trying to be reached
    """

    def adjustPosition(self, randomX, randomY, randomZ):
        self.updatedPosX(randomX)
        self.updatedPosY(randomY)
        self.updatedPosZ(randomZ)


"""
Class Field -> Creates a field object which uses 
a snitch and updates the location with chosen random
points within the bounds of the pitch

It uses xArr yArr zArr to keep track of the specific
locations that the snitch passes through 
"""
class Field():
    """
    gSnitch : snitch object within the field
    randomX, randomY, randomZ : random locations being reached
    XBOUND, YBOUND, ZBOUND : bounds of the field
    xArr, yArr, zArr : arrays used to store x y z location
    """
    gSnitch = Snitch(50, 0, 0)
    randomX = 0
    randomY = 0
    randomZ = 0

    XBOUND = 500
    YBOUND = 500
    ZBOUND = 500

    xArr = []
    yArr = []
    zArr = []

    """
    Instantiates each of the fields used 

    :param snitch: Snitch object being used 
    :param boundX: boundary of X variable 
    :param boundY: boundary of Y variable 
    :param boundZ: boundary of Z variable 

    """

    def __init__(self, snitch, boundX,
                 boundY, boundZ):

        self.gSnitch = snitch
        self.randomX = 0
        self.randomY = 0
        self.randomZ = 0

        self.XBOUND = boundX
        self.YBOUND = boundY
        self.ZBOUND = boundZ

        self.xArr = []
        self.yArr = []
        self.zArr = []

    """
        Helper method used to determine if the 
        randomX, randomY or randomZ location matches
        with the x y or z location of the snitch 
    """

    def pointReached(self):
        if (self.gSnitch.x == self.randomX):
            return True
        elif (self.gSnitch.y == self.randomY):
            return True
        elif (self.gSnitch.z == self.randomZ):
            return True
        return False

    """
    Method fly() -> Method that chooses three random
    numbers of goalX, goalY, goalZ then uses the 
    method pointReached() to continue adjusting position
    of x y z until at least one of them is equal 
    to the random number chosen 
    """

    def fly(self):
        goalX = random.randint(0, self.XBOUND)
        goalY = random.randint(0, self.YBOUND)
        goalZ = random.randint(0, self.ZBOUND)

        self.randomX = goalX
        self.randomY = goalY
        self.randomZ = goalZ

        """
        While statement that adjusts the x y z 
        position until one of them is equal to the 
        random numbers chosen.

        Adds the x y z location to the arrays that keeps
        track of each location 
        """
        while (self.pointReached() == False):
            self.gSnitch.adjustPosition(goalX, goalY, goalZ)

            self.xArr.append(self.gSnitch.x)
            self.yArr.append(self.gSnitch.y)
            self.zArr.append(self.gSnitch.z)