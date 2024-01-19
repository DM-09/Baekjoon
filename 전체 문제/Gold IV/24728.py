class PanCakeCookie:
    def __init__(self, w: int, h: int, maxC: int, u: int, d: int):
        self.__x = 0
        self.__y = 0
        self.__t = 0
        self.__score = 0
        self.__curC = maxC
        self.__u = u
        self.__d = d
        self.__maxC = maxC
        self.__w = w
        self.__h = h
        self.a = 0

    def getX(self) -> int: return self.__x
    def getY(self) -> int: return self.__y
    def getU(self) -> int: return self.__u
    def getD(self) -> int: return self.__d
    def getScore(self) -> int: return self.__score
    def getC(self) -> int: return self.__curC

    def reset(self) -> None:
        self.__x = 0
        self.__y = 0
        self.__score = 0
        self.__curC = self.__maxC
        self.a = 0
        self.__t = 0

    def setU(self, x: int) -> None:
        if 1 <= x and x <= 1000:
            self.__u = x
            self.reset()

    def setD(self, x: int) -> None:
        if 1 <= x and x <= 1000:
            self.__d = x
            self.reset()

    def setC(self, x: int) -> None:
        if 1 <= x and x <= 1000:
            self.__maxC = x
            self.reset()

    def setT(self, t: int) -> None:
        if t < 0 or t >= self.__w: return
        self.reset()
        for _ in range(t):
            self.__x += 1
            if self.__curC: self.a = 1
            if self.a == 0:
                self.__curC += 1
                self.__y -= self.__d
            else:
                self.__curC -= 1
                self.__y += self.__u
                if self.__curC == 0: self.a = 0

            if self.__y >= self.__h: self.__y = self.__h
            if self.__y <= 0: self.__y = 0

            self.__score += self.__y
