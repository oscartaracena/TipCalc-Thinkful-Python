"""Tip Calculator Program in python
where this will take an amount entered with a
add tax and calculate the tip from the total. """

#Oscar Taracena
#TipCalculator.py - Ver. 2.0
#03.16.2014

#variables 

tax = 0.09 #tax that will be charged for the meal
tip = 0.15 #tip that will be added to the bill
print "\n\n\n"

#input of the amount of the meal
print "Hello and please enter the total you spend on dinner: "
totalCostofMeal = float(raw_input())

print "\n\n"
#print "$" + str(totalCostofMeal) 

print("$" + "%.2f" % totalCostofMeal + " Is the cost of the meal")

#The math and calculations 
mealWithTax = (totalCostofMeal * tax)

total = mealWithTax + totalCostofMeal 
total1 = total * tip
#print str(total) + " Cost of dinner and tax" 
print("$" + "%.2f" % total + " Cost of Dinner and Tax")
print("$" + "%.2f" % total1 + " Is the tip!!")
print "\n"
print "$" +str(total + total1) + " Is the total cost of meal with tax and tip."
print "\n"