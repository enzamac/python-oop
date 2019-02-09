from polygon import Polygon

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def calculate_area(self):
        a,b,c = self.sides
        #get the semi-perimeter
        s = (a+b+c)/2
        #K = sqrt[ s(s - a)(s - b)(s - c) ] s**0.5
        Area = (s*(s-a)*(s-b)*(s-c))**0.5

        print("The area of the  the triangle is", Area)
    
if __name__ == "__main__":
    triangle = Triangle()         
