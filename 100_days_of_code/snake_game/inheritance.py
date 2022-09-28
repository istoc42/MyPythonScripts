class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal): # Add class to inherit from in aprenthesis after class name
    def __init__(self):
        super().__init__() # This line inits the inherited class within the new class            
            
    def breathe(self):
        super().breathe() # Inherit a method from the super class
        print("Breathing underwater.")
    
    def swim(self):
        print("Moving in water.")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)