#  The time in seconds that a pendulum takes to swing
#  back and forth once is given by this formula:
#               ____
#              / n
#      t = 2π / ----
#            √  9.81
#  
#  where t is the time in seconds,
#  π is PI the ratio of the circumference divided by
#      the diameter of a circle (use math.pi), and
#  n is the length of the pendulum in meters.
#  
#  Write a program that prompts a user to enter the length of a
#  pendulum in meters and then computes and prints the time in
#  seconds that it takes for that pendulum to swing back and forth.

import math
Lenght = float(input('Length of pendulum (meters): '))

#This is the formula 
Time = 2.0 * math.pi * math.sqrt (Lenght/9.81)
print (f'Time (seconds): {Time:.2f}')
