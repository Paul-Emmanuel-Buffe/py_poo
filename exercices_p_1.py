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
print(instance_rectangle.color)

instance_rectangle.color = "blue"
instance_rectangle.height = 5
instance_rectangle.width = 8

print(instance_rectangle.color)
print(instance_rectangle.width)
aire_rectangle = instance_rectangle.calcul_area()
print(aire_rectangle)


