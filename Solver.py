import tweepy
import random
from time import sleep

def matrixPrinter(a,b):
	try:
		print(matrix[a][b])
	except ValueError:
		print("Edge")

def surrounding(a,b):
	print(matrix[a][b] + "@" + str(a) + "," + str(b) + " is surrounded by :")
	matrixPrinter(a-1,b-1)		
	#print(matrix[a-1][b-1] + matrix[a][b-1] + matrix[a+1][b-1] + matrix[a-1][b] + matrix[a][b] + matrix[a+1][b] + matrix[a-1][b+1] + matrix[a][b+1] + matrix[a+1][b+1])
	return;

#creates 4X4 array
matrix = [[0 for x in range(4)] for x in range(4)]
#The tweet would need to be imported into the following:
inp = "tgrehiypugbidats"

#loop to fill array in desired order from the string letters
for x in range(4):
	for y in range(4):
		matrix[x][y] = inp[x+y]
a = random.randrange(0,4)
b = random.randrange(0,4)

letter = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
letter[1] = matrix[a][b]
print(letter[1]) 
surrounding(a,b)



