# Inputs
units_consumed = int(input("Enter units consumed: "))
is_senior_citizen = input("Is senior citizen (True/False): ")
has_solar_panel = input("Has solar panel (True/False): ")
payment_mode = input("Payment mode (online/offline): ")
# Convert string to boolean
is_senior_citizen = True if is_senior_citizen == "True" else False
has_solar_panel = True if has_solar_panel == "True" else False
# 1. Calculate base bill 
bill = 0
if units_consumed <= 100:
    bill = units_consumed * 3
elif units_consumed <= 300:
    bill = (100 * 3) + ((units_consumed - 100) * 5)
else:
    bill = (100 * 3) + (200 * 5) + ((units_consumed - 300) * 8)
# 2. Senior citizen discount (10%)
if is_senior_citizen:
    bill = bill - (bill * 0.10)
# 3. Solar panel discount
if has_solar_panel:
    if units_consumed <= 250:
        bill = bill - 500
    else:
        bill = bill - 300
# 4. Offline payment surcharge
if payment_mode == "offline":
    if bill < 1000:
        bill = bill + 50
    else:
        bill = bill + 100
# 5. Minimum payable amount ■200
if bill < 200:
    bill = 200
# Final Output
print("Final Electricity Bill: ■", bill)