import csv
import sys

r = 0 
c = 0
i = 1

def main():
	
	
	inputpuzz = ""
	with open('puzzle.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			inputpuzz += str(row)	
		
	inputpuzz = inputpuzz.translate(None, "[]{}':, ")

	
	inputboard = [[0 for z in range(9)] for j in range(9)]
	k = 0
	for z in range(9):
		for j in range(9):
			inputboard[z][j] = int(inputpuzz[k])
			k = k + 1
	print inputboard

	
	if solve(inputboard):
		print "\n\n Solution"
		print inputboard
	else:
		print "No solution"
	
def solve(inputboard):
	pos = unassloc(inputboard)
	row, col, var = pos
	if not var:
		return True 
	else:	
	
		for i in range(1,10):
			if goodnum(inputboard, pos[0], pos[1], i):
				inputboard[row][col] = i
				soln = inputboard
				if solve(soln):
					
					return True
				else:
					soln[r][c] = 0
					
	
		return False

		
def unassloc(grid):
	
	r = 0
	c = 0

	for r in range(9):
		for c in range(9):
			if grid[r][c] == 0:
				
				return (r, c, True)
				
		
	return (-1, -1, False)
			
def inrow(inputboard, row, val):
	 
 
	col = 0
	for col in range(9):
		if (inputboard[row][col] == val):
			return True
		else:
			return False
			
def incol(inputboard, col, val):
	
	row = 0
	for row in range(9):
		if (inputboard[row][col] == val):
			return True 
		else:
			return False

def inSq(inputboard, sr, sc, val):
	
	row = 0
	col = 0
	for row in range(3):
		for col in range(3):
			if (inputboard[row + sr][col + sc] == val):
				return True
			else:
				return False
				

def goodnum(inputboard, row, col, val):

	if inrow(inputboard, row, val) or incol(inputboard, col, val) or inSq(inputboard, row - row%3 , col - col%3, val):
		return False
	else:
		return True


main()
