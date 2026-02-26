
class Payment():
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")
class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")

mode = input("Enter Payment Mode (UPI / Card / Cash): ")
amount = int(input("Enter Amount: "))

if mode.lower() == "upi":
    payment = UPI()
elif mode.lower() == "card":
    payment = Card()
elif mode.lower() == "cash":
    payment = Cash()
else:
    print("Invalid Payment Mode")
    exit()

payment.pay(amount)