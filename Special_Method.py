class Point:
    style="fun"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # __repr__ is a special method used to show representation of object.
    def __repr__(self):
        return f"<Point x={self.x} y={self.y}>"

p1 = Point(10, 10)
p2 = Point(100, 100)
for p in [p1, p2]:
    print(f"Object {p}")
    
# Output:
Object <Point x=10 y=10>
Object <Point x=100 y=100>
