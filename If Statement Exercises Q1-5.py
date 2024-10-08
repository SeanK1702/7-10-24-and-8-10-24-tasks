#Sean Kenneally
#8/10/24
#If Statement Exercises Q1-5

#Q1
#name = input("Enter your name: ")
#print(len(name))

#if len(name) <7:
    #print("Your name is short")
#elif len(name) >=7 <=10:
    #print("Your name is long")
#else:
    #print("Your name is very long")

#Q2
#print("Menu: \n 1. Music \n 2. History \n 3. Design and Technology \n 4. Exit")
#choice = input("Please enter your choice: ")

#if choice == "1":
    #print("You chose Music")
#elif choice == "2":
    #print("You chose History")
#elif choice == "3":
    #print("You chose Design and Technology")
#elif choice == "4":
    #print("Goodbye")
    
#Q3
import random
#dice1 = random.randint(1, 6)
#dice2 = random.randint(1, 6)

#if dice1 == dice2:
    #print("You rolled a double")
    #print(dice1*dice2)
#else:
    #print(dice1+dice2)

#Q4
#price = int(input("Input value of good: "))

#if price >=200:
    #price1 = price/10
    #print("You owe", price-price1)
#elif price >=100 <=199:
    #price2 = price/5
    #print("You owe", price-price2)
#else:
    #print("You owe", price)

#Q5
#A
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

#D
if num1 >  num2:
    out = num1 - num2
#C
else:
    out = num2 - num1
    
print("The difference is", out)

