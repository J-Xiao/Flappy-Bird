from random import *
# bird 20*20 pipehole 50 pipewidth 40


class Birdandpipe:
    def __init__(self):
        self.bypos = 150
        self.bxpos = 60
        self.t = 0.1
        self.listh = []   # the random list of height
        self.listxr = []  # real list of xpos
        self.v0 = -18
        self.score = 0

    def initlisth(self):
        for i in range(100):
            self.listh += [randint(50, 200)]  # initialize height

    def initlistx(self):
        for i in range(100):
            self.listxr += [180+130*i]  # init originally 180 + 100 * i
            #self.listxv += [180+120*i]  # init

    def updatebird(self, v0, a, i):
        dy = self.v0 * self.t + a * self.t ** i  # the new ypos of kotori
        self.v0 = self.v0 + a * self.t
        self.bypos += dy
        return dy

    def updatepipe(self):
        for i in range(100): # new xpos of pipe
            self.listxr[i] -= 1
            #self.listxv[i] -= 1

    def flag1(self):
        if self.bypos >= 300 or self.bypos <= 0:
            return False
        elif 10 < self.listxr[0] < 65 and (self.bypos - self.listh[0] < 20 or self.bypos - self.listh[0] > 70):
            return False
        else:
            if self.listxr[0] < 25:
                del self.listxr[0]
                del self.listh[0]
                self.score += 1
                self.listxr += [0]
            return True

    def bgetX(self):
        return self.bxpos

    def bgetY(self):
        return self.bypos

    def pgetXlist(self, m):
        return self.listxr[m]

    def pgetHlist(self, n):
        return self.listh[n]

    def getSpeed(self):
        return self.v0

    def updateSpeed(self):
        self.v0 = -18
        return self.v0
    

