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
   return Minimum[A]



def getCoinsUsed(coinsUsed,totalVal):
   coin = TotalVal
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin
				
				
				
#  Main
def main():
	readFiles()
	length = int(totalValue.__len__())
	for idx in range(0,length):
		minCount = [0]*(totalValue[idx]+1)
		usedCount = [0]*(totalValue[idx]+1)
		#	Change these to print to file
		print totalValue[idx]
		print 'Total:',totalValue[idx],"\nChange Required:"
		#	Add timing function
		#start = time.clock() #start time
		print changedp(coinValues[idx],totalValue[idx],minCount,usedCount),"coins"
		#end = time.clock() #end time
		#sec = (end - start) #calc time
		#print("%d\t\t\t%f\t" % (i, sec))


main()