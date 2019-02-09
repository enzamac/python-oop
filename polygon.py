class Polygon:
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]
    
    def input_sides(self):
        self.sides = [float(input("Enter Side"+str(i+1)+" : ")) for i in range(self.n)]

    def display_sides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])