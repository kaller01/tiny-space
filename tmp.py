from opensimplex import OpenSimplex
from Planet import Planet
opensimplex = OpenSimplex()

def generatePlanets():
        xAmount = 40
        yAmount = 40
        factor = 2
        for x in range(-xAmount,xAmount):
            for y in range(-yAmount,yAmount):
                print(x,y)
                value = (opensimplex.noise2d(x,y)+1)/2
                value **= 2
                if value > 0.5:
                    pass

generatePlanets()