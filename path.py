class Path:
    def __init__(self):
        '''
        Desc: Initializes the list of tuples that represent the 2d map of the world
        Param: self
        Return: None
        '''
        
        self.paths = []
        row1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row2 = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        row3 = [0, 0, 0, 5, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23]
        row4 = [0, 0, 0, 6, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0]
        row5 = [0, 0, 0, 7, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0]
        row6 = [0, 0, 0, 8, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0]
        row7 = [0, 0, 0, 9, 10, 11, 12, 0, 0, 0, 0, 0, 0, 0]
        row8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.paths.append(row1)
        self.paths.append(row2)
        self.paths.append(row3)
        self.paths.append(row4)
        self.paths.append(row5)
        self.paths.append(row6)
        self.paths.append(row7)
        self.paths.append(row8)

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
    
    
    def getPathXY(self, pathNumber):
        '''
        Desc: Given a path number to go to, return the (x,y) coordinates of the path on the grid
        Param: self
                pathNum is an int
        Return: tuple
        '''
        
        for i in range(len(self.paths)):
            for j in range(len(self.paths[i])):
                if(pathNumber == self.paths[i][j]):
                    return (j * 50, i * 50)
        return (-1, -1)

    def isGrass(self,towerobj):
        """
        Descr: isGrass defines area on map that is not path
        Param: self
                mousePosition is a tuple containing position of mouse
        Return: bool expression(True/False) """
        
        pos = (towerobj.rect.centerx,towerobj.rect.centery)
        for i in range(len(self.paths)):
            for j in range(len(self.paths[i])):
                rule1 = self.paths[i][j] == 0
                rule2 = int(pos[0] /50)
                rule3 = int(pos[1] / 50)
                if (self.paths[rule3][rule2])!=0:
                    return False
        return True

