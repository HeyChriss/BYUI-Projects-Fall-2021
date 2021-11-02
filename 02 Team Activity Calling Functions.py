from datetime import datetime
discount = 0.10
tax = 0.06

current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

subtotal = float(input("Please enter the subtotal: "))



if subtotal >= 50 and (weekday == 1 or weekday == 2):
    Total_discount = round(subtotal * discount , 2)
    print(f"Discount amount: {Total_discount}")
    subtotal -= Total_discount

sales_tax = round(subtotal * tax, 2)
print(f"Sales tax amount: {sales_tax}")
subtotal += sales_tax


print(f"Total: {subtotal:.2f}")




#Total_discount = subtotal * discount
#print(f"Discount amount: {Total_discount:.2}")

#subtotal1 = subtotal - Total_discount











#n sub_total = float(input('Please enter the subtotal: '))
#n tax = float(input('Sales tax amount: '))
#n discount = 0
#n 
#n if day_of_week < 49:
#n     Total = sub_total + tax
#n elif day_of_week == 1 or 2 and day_of_week > 49:
#n     Total = sub_total + tax - discount
#n elif day_of_week == 0 or 3 or 4 or 5 or 6  and day_of_week > 49:
#n     Total = sub_total + tax
#n 
#n print(Total)

