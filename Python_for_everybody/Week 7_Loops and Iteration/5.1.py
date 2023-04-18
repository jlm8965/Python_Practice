 #Write a program which repeatedly reads numbers until the user enters "done." Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number. 


num = 0
total = 0.0
while True:
    snum = input("Enter number:")
    if snum == "done":
        break
    try:
        fnum = float(snum)
    except:
        print("That's not a number. Please try again.")
        continue
    num = num + 1 #count
    total = total + fnum #total
    average = (total/num) #average
    

print(num, total, average)





            
        

