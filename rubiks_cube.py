class RubiksCube:
    def __init__(self):
        self.redCenter = Face("R")
        self.orangeCenter = Face("O")
        self.yellowCenter = Face("Y")
        self.greenCenter = Face("G")
        self.blueCenter = Face("B")
        self.whiteCenter = Face("W")

    def fPrime(self):
        whiteRowTwo = self.whiteCenter.getRowTwo()
        orangeColumnTwo = self.orangeCenter.shiftColumnTwo(whiteRowTwo)
        yellowRowOne = self.yellowCenter.shiftRowOne(orangeColumnTwo)
        redColumnOne = self.redCenter.shiftColumnOne(yellowRowOne)
        self.whiteCenter.shiftRowTwo(redColumnOne)
        self.greenCenter.rotate()

    def f(self):
        whiteRowTwo = self.whiteCenter.getRowTwo()
        redColumnOne = self.redCenter.shiftColumnOne(whiteRowTwo)
        yellowRowOne = self.yellowCenter.shiftRowOne(redColumnOne)
        orangeColumnTwo = self.orangeCenter.shiftColumnTwo(yellowRowOne)
        self.whiteCenter.shiftRowTwo(orangeColumnTwo)
        self.greenCenter.rotate()

    def u(self):
        whiteRowOne = self.whiteCenter.getRowOne()

    def __str__(self):
        result = str(self.whiteCenter)+"\n" + str(self.orangeCenter)+"\n" + str(self.greenCenter) + \
            "\n" + str(self.redCenter)+"\n" + str(self.blueCenter) + \
            "\n" + str(self.yellowCenter)+"\n"
        return result


class Face:
    def __init__(self, color):
        self.face = [color, color, color, color, color, color, color, color]

    def rotate(self, clockwise=True):
        if clockwise:
            zero = self.face[0]
            one = self.face[1]
            self.face[0] = self.face[6]
            self.face[1] = self.face[7]
            self.face[2] = zero
            self.face[3] = one
            self.face[4] = self.face[2]
            self.face[5] = self.face[3]
            self.face[6] = self.face[4]
            self.face[7] = self.face[5]
        else:
            zero = self.face[0]
            one = self.face[1]
            self.face[0] = self.face[2]
            self.face[1] = self.face[3]
            self.face[2] = self.face[4]
            self.face[3] = self.face[5]
            self.face[4] = self.face[6]
            self.face[5] = self.face[7]
            self.face[6] = zero
            self.face[7] = one

    def __str__(self):
        result = f"{self.face[0]} {self.face[1]} {self.face[2]}\n{self.face[7]}   {self.face[3]}\n{self.face[6]} {self.face[5]} {self.face[4]}"
        return(result)

    def getRowOne(self):
        return self.face[0], self.face[1], self.face[2]

    def getRowTwo(self):
        return self.face[4], self.face[5], self.face[6]

    def getColumnOne(self):
        return self.face[6], self.face[7], self.face[0]

    def getColumnTwo(self):
        return self.face[2], self.face[3], self.face[4]

    def shiftRowOne(self, new):
        old = self.getRowOne()
        self.face[0], self.face[1], self.face[2] = new
        return old

    def shiftRowTwo(self, new):
        old = self.getRowOne()
        self.face[4], self.face[5], self.face[6] = new
        return old

    def shiftColumnOne(self, new):
        old = self.getRowOne()
        self.face[6], self.face[7], self.face[0] = new
        return old

    def shiftColumnTwo(self, new):
        old = self.getRowOne()
        self.face[2], self.face[3], self.face[4] = new
        return old


cube = RubiksCube()
print(cube)
cube.f()
print("after f")
print(cube)
