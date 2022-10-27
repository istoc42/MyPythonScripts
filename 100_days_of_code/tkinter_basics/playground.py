def add(*args): # Unlimited arguments
    result = 0
    for n in args:
        result += n
    
    print(result)
    
add(1, 2, 3, 4, 5)
add(1, 24, 389, 4346, 511235, 820985,  823, 2398752)

def calculate(n, **kwargs): # Unlimited keyword arguments
    print(kwargs)
    print(kwargs["add"])
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="BMW")
print(my_car.model)

