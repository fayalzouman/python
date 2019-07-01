from math import *

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, /, *)")

if num1.isdigit() and num2.isdigit():
	if operation == "+":
		print(int(num1) + int(num2))
	elif operation == "-":
		print(int(num1) - int(num2))
	elif operation == "/":
		print (int(num1) / int(num2))
	elif operation == "*":
		print(int(num1) * int(num2))
	else: 
		print("Please print a valid operation")
else: 
	print("Please input a valid number")










