
import turtle

class Feature:
    def __init__(self, width, height, origin, offset, type, sides=4):
        self.width = width
        self.height = height
        self.origin = origin
        self.offset = offset
        self.type = type
        self.sides = sides//2

    def draw(self):
        for i in range(self.sides):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)

    def transform(self):
        pointA = f'[{self.origin[0]-self.width/2 -self.offset }, {self.origin[1]-self.height/2 - self.offset}]'
        pointB = f'[{self.origin[0]+self.width/2 +self.offset }, {self.origin[1]-self.height/2 - self.offset}]'
        pointC = f'[{self.origin[0]+self.width/2 +self.offset }, {self.origin[1]+self.height/2 + self.offset}]'
        pointD = f'[{self.origin[0]-self.width/2 -self.offset }, {self.origin[1]+self.height/2 +self.offset}]'

        print(
            f'the bottom left "{self.type}" feature is transformed into coordinates of {pointA}')
        print(
            f'the bottom right "{self.type}" feature is transformed into coordinates of {pointB}')
        print(
            f'the top right "{self.type}" feature is transformed into coordinates of {pointC}')
        print(
            f'the top left "{self.type}" feature is transformed into coordinates of {pointD}')

        for i in range(self.sides):
            turtle.forward(self.width+self.offset)
            turtle.right(90)
            turtle.forward(self.height+self.offset)
            turtle.right(90)

myWidth = int(input('Enter a width: '))
myHeight = int(input('Enter a height: '))
pointA = int(input('Enter the x value of origin: '))
pointB = int(input('Enter the y value of origin: '))
myOffset = int(input('Enter the offsetValue: '))

round = Feature(myWidth, myHeight, [pointA, pointB], myOffset, 'Round')
round.draw()
round.transform()
