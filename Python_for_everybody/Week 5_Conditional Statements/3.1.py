#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#asking user for hours
hrs = input("Enter hours:")

try:
    hrs = float(hrs)
except:
    hrs = 0
    if hrs == 0:
        print("That's not a number. Please enter a number in number format.")

#asking user for rate
rate = input("Enter rate:")
try:
    rate = float(rate)
except:
    rate = 0
    if rate == 0:
        print("That's not a number. Please enter a number in number format")

#calculating gross pay 
if 40 == hrs > 0:
    gpay = hrs * rate
elif 40 <= hrs > 0:
    othrs = hrs - 40
    otpay = othrs * (rate * 1.5)
    spay = 40 * rate
    gpay = spay + otpay
print(gpay)