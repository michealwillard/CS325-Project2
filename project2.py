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
	string = string.translate(None, '[], ')
	outputFile.write(string)
	outputFile.seek(0)
	
	# sub procedure to create the arrays of values
	# 1st, 3rd, etc line is a coinValues. 2nd, 4th, etc line is a totalValue
	with open('Amountchange.txt') as file: # double check whihc file to have here
		i = 0
		for line in file:
			# Condition for Odd number File Lines
			# i = 0,2,4, etc
			if i % 2 == 0:
				line = line.split()
				line = [int(j) for j in line]
				coinValues.append(line)
			# Condition for Even number File Lines
			else:
				line = int(line)
				totalValue.append(line)
			i += 1
	outputFile.truncate(0)
	outputFile.close()
	
#	
#	def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
#	   for cents in range(change+1):
#	      coinCount = cents
#	      newCoin = 1
#	      for j in [c for c in coinValueList if c <= cents]:
#	            if minCoins[cents-j] + 1 < coinCount:
#	               coinCount = minCoins[cents-j]+1
#	               newCoin = j
#	      minCoins[cents] = coinCount
#	      coinsUsed[cents] = newCoin
#	   return minCoins[change]
#
#	def printCoins(coinsUsed,change):
#	   coin = change
#	   while coin > 0:
#	      thisCoin = coinsUsed[coin]
#	      print(thisCoin)
#	      coin = coin - thisCoin
#
#	def main():
#	    amnt = 63
#	    clist = [1,5,10,21,25]
#	    coinsUsed = [0]*(amnt+1)
#	    coinCount = [0]*(amnt+1)
	
	
#def changedp()
				
				
				
#  Main

readFiles()
print "Coin Values: "
print coinValues
print "Total Amount: "
print totalValue
#outputFile = open('Amountchange.txt')

