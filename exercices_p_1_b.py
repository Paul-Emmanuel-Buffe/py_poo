class ToolsBox : 
    
    def __init__ (self):
        self.tool = []
    
    def add_tools (self):
        """"ajoute des outils"""
        pass

    def remove_tools (self):
        """"retire des outils"""
        pass
       
    
class Hammer :

    def __init__(self, color = "red"):
     """"initialise la couleur"""
     self.color = color
     pass
    
    def paint_hammer(self,color) :
        """change la couleur"""
        pass

    def hammer_in( self, nail):
        "planter"
        pass
    
    def remove (self, nail):
        """retirer"""
        pass

class Screwdriver :
    
    def __init__(self, size):
        """initialise la taille"""
        self.size = size
        pass

    def tighten (self,scew) :
        """visser"""
        pass

    def loosen (self,screw):
        """dévisser"""
        pass
        
