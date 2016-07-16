from collections import namedtuple
import graphicAssets
import json

#todo add color
Pixel = namedtuple("pixel", ['y', 'x', 'char'])

class gameEntity():
    def __init__(self, graphicAsset, y, x):
        self.graphic = graphicAsset
        self.y = y
        self.x = x

    #methods to be used by server game side

    #can be used to make a json of an array of these entities
    def __repr__(self):
        return str({"graphicAsset":self.graphic.name, "x":self.x, "y":self.y}).replace("\'","\"")

    def setYX(self, y, x):
        self.y = y
        self.x = x

    #methods used by client/render side
    def getYX(self):
        return self.y, self.x

    #todo add color
    #todo choose drawing index by animation sequence
    def getDrawing(self):
        return [Pixel(y + self.y, x + self.x, ord(self.graphic.drawings[0][y][x]))
                for y in range(self.graphic.height)
                for x in range(self.graphic.width)
                if self.graphic.drawings[0][y][x] != " "]


#for testing
if __name__ == '__main__':
    import random
    import cursesIO
    import log

    assets = graphicAssets.getAllAssets()
    entities = []
    for k in [random.choice(assets.keys()) for _ in range(6)]:
        y,x = random.randint(0, 20 - assets[k].height - 1), random.randint(0, 80 - assets[k].width - 1)
        entities.append(gameEntity(assets[k], y, x))

    log.log(str(entities) + '\n')

    cursesEntities = cursesIO.createScreenArray(str(entities), assets)
    cursesScreen = cursesIO.startCurses()
    cursesIO.renderEntities(cursesScreen,cursesEntities)

    while 1:
        char_in = cursesScreen.getch()
        if char_in == ord('q'): break

    cursesIO.exitCurses(cursesScreen)

