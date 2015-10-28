# CS 325 - Project 2 - Coin Change
# Group 13
# Micheal Willard
# Stephen Heng
# Frankie Nguyen
# Robert Tang
# project2_greedy.py



import sys
import time
import datetime
import readline
sys.setrecursionlimit(2000)
coinValues = []
totalValue = []
lineIndex = 0


# Function to read in data from input file and create arrayswith data
# O'Reilly: Learning Python File I/O used for reference
def readFiles(fName):
	# Input file should contain coin values and total value (to make change for)
	global coinValues
	global totalValue
	inputFile = open(fName + '.txt', 'r')
	with open(fName + '.txt') as file:
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
				coinValues.append(line)
			# Condition for Even number File Lines
			else:
				line = int(line)
				totalValue.append(line)
			i += 1


#	
def changegreedy(V,A,Minimum):
	currentValue = A
	remainder = 0
	coinsMin = 0
	div = 0
	idx = int(V.__len__()) - 1
	tempArr = [0]*(idx+1)
	
	while currentValue > 0:
		div = currentValue / V[idx]
		rem = currentValue % V[idx]
		currentValue -= V[idx] * div
		coinsMin += div
		tempArr[idx] = div
		idx -= 1
	print coinsMin
	Minimum = coinsMin
	return tempArr



def getCoinsUsed(minArr):
	tally = 0
	for i in minArr:
		tally += i
	return tally
				

				
##  Main
def main():
	
	inputFileName = ''
	if len(sys.argv) > 1:
		inputFileName = sys.argv[1]
		print inputFileName
	else:
		print "Enter the text file name without .txt extension: "
		inputFileName = sys.stdin.readline().rstrip('\n')
		print inputFileName
	readFiles(inputFileName)
	outputFile = open(inputFileName + 'change.txt', 'w')
	outputFile.write("Algorithm 2: changegreedy Results")
	
	#  Length of the array of the total Values to make change for
	length = int(totalValue.__len__())
	#	Iterate throught the length of the total Values array
	for idx in range(0,length):
		#	Temp array to store the count of the minimum number of coins needed
		minCount = [0]*(totalValue[idx]+1)
		minCoins = 0
		#	Temp array to store the count of the coins used
		usedCount = [0]*(totalValue[idx]+1)
		print 'Total:',totalValue[idx]
		
		#	Timing to be done as a function of A
		#	A is the value for which change is being found
		#	Thus there should be one time per loop
		start = time.clock() #start time
		#	Call changedp algo, base the coin values and total Value from the input file
		usedCount[idx] = changegreedy(coinValues[idx],totalValue[idx],minCoins)
		end = time.clock() #end time
		sec = (end - start) #calc time

		print "%0.5f" % sec

		minTally = getCoinsUsed(usedCount[idx])
		#	Write the 2 lines to output file
		outputFile.write("\n" + str(usedCount[idx]))
		outputFile.write("\n" + str(minTally))

main()