#part one
h=[1,12,123,1234,12345]
for y in h:
    print(y)

#part 2
import math
print(math.factorial(5))


#part 3

a = 3
b = 4
c=(a+b)
print(c)

#part 4
class User:
    def __init__(self, car, brand, year):
        self.car = car
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"car: {self.car}")
        print(f"brand: {self.brand}")
        print(f"year: {self.year}")

#part 5
user1 = User("rangerover", "edition5", "2023")
user1.display_info()
print()



