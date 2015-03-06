# Author: Abraheem Irheem
"""
Coin Dispenser
"""

print "Welcome to the dollar store!"
price = input("Enter the price of the item: ")

totalChange = 100 - price
change = totalChange # 'change' is used for calculation
print "Returning %d cents as" % change 

quarters = change/25 #Gets number of quarters
change = change%25   #Gets the remainder

dim = change/10      #Gets number of dimes
change = change%10   #Gets the remainder

nic = change/5       #Gets number of nickels
change = change%5    #Gets the remainder

pen = change         #What remains of 'change' is the number of pennies 

#Prints results
print "%d of quarter = " % quarters + "%2d cents" %(quarters*25)
print "%d of dimes   = " % dim + "%2d cents" %(dim*10)
print "%d of nickels = " % nic + "%2d cents" %(nic*5) 
print "%d of pennies = " % pen + "%2d cents" %(pen)
print "total change = %2d cents" % totalChange

x = raw_input("Press Enter to exit the program")
