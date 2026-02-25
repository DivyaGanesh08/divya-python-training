#Order Amount Calculation using Class
class Order:
    def __init__(self):
        self.total = 0

    def add_items(self):
        n = int(input("Enter number of items: "))
        for i in range(n): # loop
            price = float(input(f"Enter price of item {i+1}: "))
            qty = int(input("Enter quantity: "))
            amount = price * qty # operator
            self.total += amount

    def discount(self):
        if self.total >= 1000: # conditional
            print("10% discount applied")
            self.total = self.total - (self.total * 0.10)
        elif self.total >= 500:
            print("5% discount applied")
            self.total = self.total - (self.total * 0.05)
        else:
            print("No discount")

    def display(self):
        print("Final Order Amount =", self.total)
# main program
obj = Order()
obj.add_items()
obj.discount()
obj.display()