from math import *
first_num = raw_input("Write a numbere:")
second_num = raw_input("Choose a second number:")
if first_num == float(first_num) or int(second_num):
	print first_num
else:
	print "Please submit a number"

if second_num == float(second_num) or int(second_num):
	print first_num
else:
	print "Please submit a number"
operation = raw_input("Please type your operation: add, subtract, multiply or divide.")
if operation = raw_input("add"):
	print first_num + second_num
elif operation = raw_input("subtract"):
	print first_num - second_num
elif operation = raw_input("multiply"):
	print first_num * second_num
elif operation = raw_input("divide"):
	print first_num / second_num
else:
	print "Please choose one of the options."