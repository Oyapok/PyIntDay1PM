class Point:
    def __init__(self, vx, vy):
        self.__x=vx   # attribute __x is defined here
        self.__y=vy   # attribute __y is defined here
        # self.z=vx+vy
        
    def __str__(self):
        return f"<{self.__x},{self.__y}>"
    
    def __add__(self, other):
        return Point(self.__x+other.__x, self.__y+other.__y)
    
    def distance(self, other):
        import math
        return math.sqrt((other.__x-self.__x)**2 + (other.__y-self.__y)**2)
    
    def clear(self):
        self.__x=self.__y=0

    def setX(self, val):
        if isinstance(val, (int, float)):
            self.__x=val
        else:
            raise Exception("Invalid value")
    def getX(self):
        return self.__x

    x=property(getX, setX)
    
    def setY(self, val):
        if isinstance(val, (int, float)):
            self.__y=val
        else:
            raise Exception("Invalid value")
    def getY(self):
        return self.__y

    y=property(getY, setY)
    
    # @property()
    # def y(self):
    #     return self.__y
    
    # @y.setter
    # def y(self.val):
    #     if isinstance(o, t)
    
    
p1=Point(10,20)
print(p1.x)
p1.x=26
print(p1)
del p1.x











