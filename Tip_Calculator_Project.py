print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage would you like to give? 10 12 15"))
people = int(input("how many people to split the bill?"))
tip_to_percentage = (tip/100)
total_tip_amount = (bill * tip_to_percentage)
total_bill = (bill + total_tip_amount)
bill_per_person = (total_bill / people)
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")


