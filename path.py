class Path:
    def __init__(self):
        '''
Desc: tset
        '''
        self.paths = []
        self.maxPath = 16
        row1 = (1, 2, 0, 0, 0, 14, 15, 16)
        row2 = (0, 3, 0, 0, 0, 13, 0, 0)
        row3 = (0, 4, 5, 0, 0, 12, 0, 0)
        row4 = (0, 0, 6, 0, 0, 11, 0, 0)
        row5 = (0, 0, 7, 8, 9, 10, 0, 0)
        self.paths.append(row1)
        self.paths.append(row2)
        self.paths.append(row3)
        self.paths.append(row4)
        self.paths.append(row5)
    def __str__(self):
        return str(self.paths)
    def getNextPath(self, invader):
        for i in range(1, self.maxPath + 1):
            if(i == invader.location):
                return i + 1 #should decrement castle health if this is greater than maxPath
    def getNextPathXY(self, pathNumber):
        for i in range(len(self.paths)):
            for j in range(len(self.paths[i])):
                if(pathNumber == self.paths[i][j]):
                    return (i, j)
def main():
    p = Path()
    print(p)
    print(p.paths[2][1])
    print(p.paths[2][2])
    print(p.getNextPathXY(5))
    print(p.getNextPathXY(16))
    print(p.getNextPathXY(17))
main()
