##--Code fixed and commented from previous submitted version

import csv
import sys
from pprint import pprint 

def main():
	
##-- Code below extracts data from csv called puzzle 
##-- Brings in data first as a string 
##-- Filters unwanted characters out of string
	inputpuzz = ""
	with open('puzzle.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			inputpuzz += str(row)	
	inputpuzz = inputpuzz.translate(None, "[]{}':, ")

##-- Converts string of numbers to 2D list of ints
	inputboard = [[0 for z in range(9)] for j in range(9)]
	k = 0
	for z in range(9):
		for j in range(9):
			inputboard[z][j] = int(inputpuzz[k])
			k = k + 1
	print "\nProblem"
	pprint(inputboard)

##--Calls solve algorithm for input data	
	if solve(inputboard):
		print "\n\n Solution"
		pprint(inputboard)
	else:
		print "No solution"

##--Recursive solving method		
def solve(inputboard):

##--sets Row and column values for unassigned location 
##--gives boolean of if unassinged locatons exist
	
	row, col, var = unassloc(inputboard)
	
##--If there aren't any unassigned locations board is solved	
	if not var:
		return True 
	else:	
##--Check nums 1-9 in order to see if it is a good fit for row,col	
##--If good fit is found set value to i and trigger recursion
##--If choice does not solve board set the value to 0
		for i in range(1,10):
			if goodnum(inputboard, row, col, i):
				inputboard[row][col] = i
				soln = inputboard
				if solve(soln):
					return True
				else:
					soln[row][col] = 0
		return False

##--Returns row and col of unassigned value and logic of if unassigned occurs		
def unassloc(grid):
	r = 0
	c = 0
	for r in range(9):
		for c in range(9):
			if grid[r][c] == 0:
				return (r, c, True)
	return (-1, -1, False)

##--Returns true if number occurs in row	
def inrow(inputboard, row, val):
	col = 0
	for col in range(9):
		if (inputboard[row][col] == val):
			return True
	return False

##--Returns true if number occurs in column	
def incol(inputboard, col, val):
	row = 0
	for row in range(9):
		if (inputboard[row][col] == val):
			return True 
	return False

##--Returns true if number occurs in column
def inSq(inputboard, sr, sc, val):
	row = 0
	col = 0
	for row in range(3):
		for col in range(3):
			if (inputboard[row + sr][col + sc] == val):
				return True
	return False
				
##--Checks if value provided is a valid choice
def goodnum(inputboard, row, col, val):
	if inrow(inputboard, row, val) or incol(inputboard, col, val) or inSq(inputboard, row - row%3 , col - col%3, val):
		return False
	else:
		return True


main()
