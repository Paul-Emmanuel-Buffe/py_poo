class Car :

    def __init__(self, model, year, color= "grey"):
        self.model = model
        self.year = year
        self.color = color

    def control (self):
        if self.year > 1950:
                result = "Ce véhicule peut rouler"
        else:
            result = "Ce véhicule doit être détruit" 

        return result
    

instance_car = Car("berline", 1780, "Bleue")

conformite= instance_car.control()

print(conformite)
print(instance_car.model)

instance_car.color = "Rose"
instance_car.year = 1987

print(instance_car.color)
conformite= instance_car.control()
print(conformite)

            
class Bird : 
     
    names = ("mouette", "perdreau", "moineau", "pie")
    positions = {}

    def __init__(self, name):
          
         self.name = name
         self.position = (1,2)

         self.positions[self.position] = self.name

    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée."""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"
        return "On a rien trouvé..." 
    

Bird.names
Bird.positions

print(Bird.find_bird((1,3)))

bird = Bird("mouette")

print(Bird.find_bird((1,2)))
