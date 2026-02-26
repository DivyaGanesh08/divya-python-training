
class Vehicle():
    def calculate_rent(self, days):
        pass
class Car(Vehicle):
    def calculate_rent(self, days):
        return days * 1000  

class Bike(Vehicle):
    def calculate_rent(self, days):
        return days * 500

vehicle_type = input("Enter Vehicle (Car / Bike): ")
days = int(input("Enter Number of Days: "))

if vehicle_type.lower() == "car":
    vehicle = Car()
elif vehicle_type.lower() == "bike":
    vehicle = Bike()
else:
    print("Invalid Vehicle Type")
    exit()

total_rent = vehicle.calculate_rent(days)
print("Total Rent:", total_rent)