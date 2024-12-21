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


class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]

 

class Screwdriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size
    
    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()
    
    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color
    
    def paint(self, color):
        """Paint le marteau."""
        self.color = color
    
    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()
    
    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screw:
    """Vis."""
     
    MAX_TIGHTNESS = 5
    
    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0
    
    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1
    
    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""
    
    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False
    
    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True
    
    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."

outils_in_box = ToolBox()

tournevis = Screwdriver()

marteau = Hammer()

outils_in_box.add_tool(tournevis)
outils_in_box.add_tool(marteau)

print(outils_in_box.tools)

vis = Screw()
print(vis)

vis.tighten()
print(vis)

clou = Nail()

print(clou)

clou.nail_in()
print(clou)

outils_in_box = ToolBox()
marteau2 = Hammer()
marteau2.paint('blue')
outils_in_box.add_tool(marteau2)
print(outils_in_box.tools)

