#!/usr/bin/pythonC:\Python27

def calculate():
	calculation = raw_input("Enter Your Calculation")
	calculation = calculation.split(" ")

	num1 = float(calculation[0])
	type = calculation[1]
	num2 = float(calculation[2])

	print num1

calculate()
