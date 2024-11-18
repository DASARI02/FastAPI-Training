class Rect:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    def area(self):
        area = self.length * self.breath
        return area
    def perimeter(self):
        perimeter = 2 * (self.length + self.breath)
        return perimeter
r = Rect(4,5)
r1 = Rect(5,6)
print(r.area())
print(r1.area())