# TASK 2
# calculate the final bill for a food order based on
# 1. order amt
# 2. customer type
# 3. delivery distance
# 4. payment method
# discount
# >=1000 - 10%
# >=500 - 5%
# customer type
# prime- order value >=500 extra 5%
# delivery charge based on distance
# <=5km -40rs
# >5km - 70rs
# payment method
# cash on delivery <500 - extra 25rs
#PROGRAM

order_amt = float(input("Enter order amount: "))
customer_type = input("Enter customer type (prime/regular): ")
distance = float(input("Enter delivery distance (in km): "))
payment_method = input("Enter payment method (cod/online): ")
discount = 0
# Order amount discount
if order_amt >= 1000:
    discount = order_amt * 0.10
elif order_amt >= 500:
    discount = order_amt * 0.05
# Prime customer extra discount
if customer_type.lower() == "prime" and order_amt >= 500:
    discount += order_amt * 0.05
    amount_after_discount = order_amt - discount
# Delivery charge
if distance <= 5:
    delivery_charge = 40
else:
    delivery_charge = 70
# Cash on delivery extra charge
cod_charge = 0
if payment_method.lower() == "cod" and order_amt < 500:
    cod_charge = 25
# Final bill
final_bill = amount_after_discount + delivery_charge + cod_charge
print("Discount:", discount)
print("Delivery Charge:", delivery_charge)
print("COD Charge:", cod_charge)
print("Final Bill Amount:", final_bill)