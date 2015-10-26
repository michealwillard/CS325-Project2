# CS 325 - Project 2 - Coin Change
# Group 13
# Micheal Willard
# Joshua Johnson
# Robert Tang
# project2.py



import sys
import time
sys.setrecursionlimit(2000)
coinValues = []
totalValue = []
lineIndex = 0

# Function to read in data from input file and create arrayswith data
# O'Reilly: Learning Python File I/O used for reference
def readFiles():
	# Input file should contain coin values and total value (to make change for)
	global coinValues
	global totalValue
#	coinValues = []
#	totalValue = []
	inputFile = open('Amount.txt', 'r')
	with open("Amount.txt") as file:
		i = 0
		## sub procedure to create the arrays of values
		## 1st, 3rd, etc line is a coinValues. 2nd, 4th, etc line is a totalValue
		for line in inputFile:
			line = line.replace('[', '').replace(']', '')
			#		# Condition for Odd number File Lines
			#		# i = 0,2,4, etc
			if i % 2 == 0:
				line = line.rstrip().split(',')
				line = [int(j) for j in line]
#				print line
				coinValues.append(line)
			# Condition for Even number File Lines
			else:
				line = int(line)
				totalValue.append(line)
			i += 1




	
	
#def changedp()
				
				
				
#  Main
def main():
	tempidx = 0

	readFiles()
	#	Array output check
	print("Coin Values:")
	print coinValues[0]
	print coinValues[1]
	print coinValues[0][0]
	print coinValues[0][1]
	print coinValues[0][2]
	print coinValues[1][0]
	print coinValues[1][1]
	print coinValues[1][2]
	print coinValues[1][3]
	print("Total Value:")
	print totalValue[0]
	print totalValue[1]
	
main()

