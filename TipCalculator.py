"""Tip Calculator Program in python
where this will take an amount entered with a
add tax and calculate the tip from the total. """

#Oscar Taracena
#TipCalculator.py - Ver. 1.0
#03.16.2014

#variables 

tax = 0.009 #tax that will be charged for the meal
tip = 0.15 #tip that will be added to the bill

print "Hello and please enter the total you spend on dinner: "
totalCostofMeal = raw_input()

mealWithTax = totalCostofMeal * tax

print mealWithTax