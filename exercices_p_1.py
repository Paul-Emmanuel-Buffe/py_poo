class Rectangle:
        def __init__(self, height, width, color="red"):
                self.height = height
                self.width = width
                self.color = color

        def calcul_area(self):
             return self.width * self.height
    
instance_rectangle = Rectangle(4, 3)

aire_rectangle = instance_rectangle.calcul_area()

print(aire_rectangle)


