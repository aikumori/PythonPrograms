"""
Author: Abraheem Irheem
Time converter
"""

time = input("Enter time in seconds: ")

seconds = time

hours = seconds/(60*60)
seconds = seconds%(60*60)

minutes = seconds/60
seconds = seconds%60

print "%d seconds = " % time + "%d hours, " % hours + "%d minutes, " % minutes + "and %d seconds" % seconds
