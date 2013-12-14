
from Point import Point
from pypng import Png

class Dragon:
    pivot = Point()
    points = [Point()]
    
    def __init__(self, x):
        self.points = []
        for i in range(x+1):
            self.points.append(Point(i,0))
        self.pivot = Point(x,0)
        self.maximal = self.pivot.dup()
    
    def p(self, n = 8):
        counter = 0
        print 'pivot: ({0},{1})'.format(self.pivot.x,self.pivot.y)
        for p in self.points:
            print '({0},{1})'.format(p.x,p.y),
            counter += 1
            if counter == n:
                counter = 0
                print ''
        return self
    
    def iterate(self, n = 1):
        for rounds in range(n):
            for p in self.points[1:-1]:
                self.points.append(p.dup().rotate(self.pivot))
            # handle new pivot
            new_pivot = self.points[0].dup().rotate(self.pivot)
            self.pivot = new_pivot
            self.points.append(self.pivot.dup())
        return self
    
    def _normalize(self):
        #find min x and min y in points
#        print 'pre normalization:', self.p()
        minX,minY,maxX,maxY = 0,0,0,0
        for p in self.points:
            if p.x < minX:
                minX = p.x
            if p.y < minY:
                minY = p.y
#        print "\n\nfound a minimum at ({0},{1})".format(minX,minY)
        # translate all the points
        new_array = []
        for p in self.points:
            new_array.append(p.dup().translate(-minX, -minY))
        self.points = new_array
#        print '\n\npost normalization:', self.p()
        # get maximums
        for p in self.points:
            if p.x > maxX:
                maxX = p.x
            if p.y > maxY:
                maxY = p.y
        self.maximal = Point(maxX, maxY)
        return self
    
    def write(self, filename, forground = [0,0,0], background = [255,255,255]):
        self._normalize()
        width = 1 + (self.maximal.x + 1) + 1
        height = 1 + (self.maximal.y + 1) + 1
        image = Png(width,height)
#        print "image is {0}x{1} pixels".format(width, height)
        for y in range(height):
            for x in range(width):
#                print "setting background color of ({0},{1})".format(x,y)
                image.set_pixel(x,y,background)
        for p in self.points:
            image.set_pixel(1 + p.x,1 + p.y,forground)
#            print "set forground of point ({0},{1})".format(p.x,p.y),
#            print "at pixel ({0},{1})".format( 1 + p.x, 1 + p.y)
        image.write(filename)
        return self
