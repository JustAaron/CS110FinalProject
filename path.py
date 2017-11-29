class Path:
    def __init__(self):
        '''
Desc: Initializes the list of tuples that represent the 2d map of the world
Param: self
Return: None
        '''
        self.paths = []
        row1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        row6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.paths.append(row1)
        self.paths.append(row2)
        self.paths.append(row3)
        self.paths.append(row4)
        self.paths.append(row5)
        self.paths.append(row6)
        self.paths.append(row7)
        self.paths.append(row8)
        self.paths.append(row9)
        self.paths.append(row10)
        self.maxPath = 1
        for i in range(len(self.paths)):
            for j in range(len(self.paths[i])):
                if(self.paths[i][j] > self.maxPath):
                    self.maxPath = self.paths[i][j]
    def __str__(self):
        '''
Desc: Return the 2d array that represents the path
Param: self
Return: List of Tuples
        '''
        return str(self.paths)
    def getNextPath(self, invader):
        '''
Desc: Given an instance of an invader, return its next path number to go to
Param: self, invader
Return: int
        '''
        if(invader.location + 1 <= self.maxPath):
            return invader.location + 1
        return -1 #if this is returned, decremenet castle health
    def getPathXY(self, pathNumber):
        '''
Desc: Given a path number to go to, return the (x,y) coordinates of the path on the grid
Param: self, int
Return: tuple
        '''
        for i in range(len(self.paths)):
            for j in range(len(self.paths[i])):
                if(pathNumber == self.paths[i][j]):
                    return (i, j)
        return (-1, -1)
