# Python program to demonstrate
# super function
 
 
class Animals:
     
    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
     
    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")
     
    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")
     
class Dogs(Animals):
    def __init__(self):
        super().__init__()
 
    def isMammal(self):
        super().isMammal()
 
class Horses(Animals):
    def __init__(self):
        super().__init__()
 
    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")
 
# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()