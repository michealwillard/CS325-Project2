# CS 325 - Project 2 - Coin Change
# Group 13
# Micheal Willard
# Stephen Heng
# Frankie Nguyen
# Robert Tang
# project2_changeDP.py



import sys
import time
sys.setrecursionlimit(2000)
coinValues = []
totalValue = []
lineIndex = 0
#inputFileName = 'Amount'
#inputFileName = 'q4'
#inputFileName = 'q5a'
#inputFileName = 'q5b'
inputFileName = 'q5c'
#inputFileName = 'q5d'

# Function to read in data from input file and create arrayswith data
# O'Reilly: Learning Python File I/O used for reference
def readFiles():
	# Input file should contain coin values and total value (to make change for)
	global coinValues
	global totalValue
	# if statement to change inputFileName goes here
	inputFile = open(inputFileName + '.txt', 'r')
	with open(inputFileName + '.txt') as file:
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

# Change Dynamic Programming Function
# Inputs: 
#	Array V where V[i] is the value of the coin of the ith denomination
#	Value A which is the amount of change being asked to make
#	Array Minimum which counts the minimum number of coins used
#	Array Used which is the full Dynamic Programming counting array
	
def changedp(V,A,Minimum,Used):
	for cents in range(A+1):
		coinCount = cents
		newCoin = 1
		# j starting at 0 going to c, for list compression
		for j in [c for c in V if c <= cents]:
			# Check if current coinCount > Minimum at index cents - j
			if Minimum[cents-j] + 1 < coinCount:
				coinCount = Minimum[cents-j]+1
				# Reset the new coin value to j (value of coin from coin values in V)
				newCoin = j
		Minimum[cents] = coinCount
		Used[cents] = newCoin
		# Minimum at last index
	return Minimum[A]



def getCoinsUsed(coinsUsed,totalVal,coinVal):
	coin = totalVal
	tempCount = []
	tallyArr = []
	# Put the number of coins used in tempCount
	while coin > 0:
		thisCoin = coinsUsed[coin]
		coin = coin - thisCoin
		tempCount.append(thisCoin)
	t = 0
	# Count the number of occurences of each coin in tempCount, append tally to tallyArr
	for coin in coinVal:
		tallyArr.append(tempCount.count(coin))
		t += 1
	# need to return new array that compares the values of V, ie:
	# tempCount = [1,7,7,7], V = [1,3,7,26] => newArr = [1,0,3,0]
	return tallyArr
				
				
				
#  Main
def main():
	readFiles()
	outputFile = open(inputFileName + 'change.txt', 'w')
	outputFile.write("Algorithm 3: changedp Results")
	#  Length of the array of the total Values to make change for
	length = int(totalValue.__len__())
	#	Iterate throught the length of the total Values array
	for idx in range(0,length):
		#	Temp array to store the count of the minimum number of coins needed
		minCount = [0]*(totalValue[idx]+1)
		#	Temp array to store the count of the coins used
		usedCount = [0]*(totalValue[idx]+1)
		print 'Total:',totalValue[idx]
		
		#	Timing to be done as a function of A
		#	A is the value for which change is being found
		#	Thus there should be one time per loop
		start = time.clock() #start time
		#	Call changedp algo, base the coin values and total Value from the input file
		minOutput = changedp(coinValues[idx],totalValue[idx],minCount,usedCount)
		end = time.clock() #end time
		sec = (end - start) #calc time
		print "Time for A =",totalValue[idx],":",sec, "seconds"
		
		minArray = getCoinsUsed(usedCount,totalValue[idx],coinValues[idx])
		#	Write the 2 lines to output file
		outputFile.write("\n" + str(minArray))
		outputFile.write("\n" + str(minOutput))

main()