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
	
	# Input File has data stored, Output File holds temporary arrays and final output of Algorithms
	inputFile = open('Amount.txt', 'r')
	outputFile = open('Amountchange.txt', 'w')
	
	string = inputFile.read()
	string = string.translate(None, '[],')
	outputFile.write(string)
	outputFile.seek(0)
	
	# sub procedure to create the arrays of values
	# 1st, 3rd, etc line is a coinValues. 2nd, 4th, etc line is a totalValue
	with open('Amountchange.txt') as file: # double check whihc file to have here change
		i = 0
		for line in file:
			# Condition for Odd number File Lines
			# i = 0,2,4, etc
			if i % 2 == 0:
				line = line.split()
				line = [int(j) for j in line]
				print line
				coinValues.append(line)
			# Condition for Even number File Lines
			else:
				line = int(line)
				totalValue.append(line)
			i += 1
			print line
	outputFile.truncate(0)
	outputFile.close()
	


	
	
#def changedp()
				
				
				
#  Main
def main():
	tempidx = 0

	readFiles()
	print "Coin Values: "
	for x in xrange(len(coinValues)):
		print("Results for problem " + str(tempidx) + "\nCoins: " + str(coinValues[tempidx]) + "\n")
		print("Amount: " + str(totalValue[tempidx]) + "\n") 
		#print coinValues
	print "Total Amount: "
	print totalValue
	#outputFile = open('Amountchange.txt')
	tempidx += 1
	print "Manual Extraction: "
	print (coinValues[0][0] + coinValues[0][1])
	print coinValues[1][0]
	print totalValue[0]
	print totalValue[1]
	
main()

