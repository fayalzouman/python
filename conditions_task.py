from math import *
first_num = raw_input("Write a number from 1-10")
if first_num == float(first_num) or int(second_num):
	print first_num
else:
	print "Please submit a number"
second_num = raw_input("Write a number from 11-20")
if second_num == float(second_num) or int(second_num):
	print first_num
else:
	print "Please submit a number"
operation = raw_input("Choose an operation: add, subtract, multiply or divide.")
if operation == +:
	print first_num + second_num
elif operation == -:
	print first_num - second_num
elif operation == *:
	print first_num * second_num
elif operation == /:
	print first_num / second_num
else:
	print "Please choose one of the options."