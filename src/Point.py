
#from const import cw
#from const import ccw
cw,ccw = 1,-1

class Point:
    x = 0
    y = 0
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def translate(self, x, y):
        self.x += x
        self.y += y
        return self
    
    def dup(self):
        return Point(self.x, self.y)
    
#    def _rotcw(self):
#        x,y = self.x,self.y
#        self.x, self.y = y, -x
#        return self
#    
#    def _rotccw(self):
#        x,y = self.x,self.y
#        self.x,self.y = -y, x
#        return self
    
    def rotate(self, pivot, cdir = cw):
        x = self.x
        y = self.y
        if cdir == cw:
            self.x = y - pivot.y + pivot.x
            self.y = pivot.x - x + pivot.y
            return self
#            return (self - pivot)._rotcw() + pivot
        else:
            self.x = pivot.y - y + pivot.x
            self.y = x - pivot.x + pivot.y
#            return (self - pivot)._rotccw() + pivot
    
