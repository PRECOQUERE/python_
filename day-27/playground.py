def add(*args) :
    total = 0
    for n in args:
        total += n
    print(total)

add(1, 2, 3, 4)

def add2(n, **kwargs) :
    n += kwargs.get("add")
    n *= kwargs["multiply"]
    return n

print(add2(5, add=7, multiply=2))

class car:
    def __init__(self, **kw) :
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = car(make="HyunDae")        
print(my_car.model)