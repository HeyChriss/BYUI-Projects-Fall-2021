import math
from datetime import datetime

current_date = datetime.now()
model = input ('Enter the car model:  ')
w = float(input ('Enter the width of the tire in mm (ex 205): '))
a = float(input ('Enter the aspect ratio of the tire (ex 60): '))
d = float(input ('Enter the diameter of the wheel in inches (ex 15): ')) 

volume = ((math.pi *(w**2)* a) * (w*a + (2540 * d))) / 10000000000

print(f' The approximate volume is: {volume:.2f} liters')

buy = input('Would you like to buy the tires? (yes or no): ').capitalize()

if buy == 'Yes':
    Phone = input ('What is your phone number')
    with open("volumes.txt", "at") as volumes_file:
        print(current_date, model, file=volumes_file)
        print(f"width: {w},ratio: {a},diameter: {d},volume: {volume:.2f} ", file=volumes_file)
        print(f'Phone number is: {Phone}',file=volumes_file)
    print('Thank you, your information has been recorded.')    
elif buy == 'No': 
    with open("volumes.txt", "at") as volumes_file:
        print(current_date, model, file=volumes_file)
        print(f"width: {w},ratio: {a},diameter: {d},volume: {volume:.2f} ", file=volumes_file)
    print('Thank you, We hope we see you soon! ')
else:
    print ('You chose the incorrect option, your information has not been saved.')
    print ('Please enter the correct answer again. ')


    