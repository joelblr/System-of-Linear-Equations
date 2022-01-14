#	Program to Convert a Matrix to Echelon Form

from fractions import Fraction
import numpy as np

from Consistency import consistent
from Solution import soln

##	To divide two Numbers with Exception
def div(x, y) :
	if y == 0	:	return (0)
	return (x/y)

##	To Perform Row Transformations
def rowReplace(matrix, i):

	for j in range(len(matrix)-1, 0, -1) :
		if matrix[j][i] != 0 :
			matrix[i], matrix[j] = matrix[j], matrix[i]
			break

##	To Simplify a Matrix using Gaussian elimination method
def echelon(matrix) :

	for i in range(len(matrix)) :	matrix[i] = list(map(float, matrix[i]))
	for i in range(len(matrix)-1) :

		##	Row Inversion  			Ri ⟷ Rj  ##
		if matrix[i][i] == 0 :
			rowReplace(matrix, i)

		##	Row Transformation	Ri → xRi + yRj ##
		for j in range(i+1, len(matrix)) :
			factor = div(matrix[j][i], matrix[i][i])
			matrix[j] = list(np.subtract(matrix[j], [k*factor for k in matrix[i]]))
##	__Main__
def main() :

	superscript_map	=	{
	"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
	"7": "⁷", "8": "⁸", "9": "⁹"}
	subscript_map	=	{
	"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
	"7": "₇", "8": "₈", "9": "₉"}

	print(f"\n{'>'*80}")
	for i in range(len(matrix[0]) -1):
		print(f"\tx{subscript_map[str(i+1)]}", end = "\t")
	print("\n")

	for i in matrix :
		for j in range(len(i)) :
			if j == len(i) -1	:	print(f"=\t{i[j]}")
			else				:	print(f"\t{i[j]}", end = "\t")
	# print(f"{'*'*80}\nEchelon Matrix  :  {len(matrix[0]) -1} Variables\n{'*'*80}")
	echelon(matrix)
	m = [[Fraction(str(j)).limit_denominator(100) for j in i] for i in matrix]
	m, flag, mess = consistent(m)
	# for k in m	:
	# 	for l in k :
	# 		print(l, end = '\t')
	# 	print()
	# print(f"{'*'*80}\n{mess}")
	print('*'*80)

	soln(m, flag)
	print(f"{'<'*80}\n")


###################################################################################
## Trivial

matrix = [	[1, 2, 3, 0],
			[2, 3,  1, 0],
			[4, 5,  4, 0],
			[1, 1, -2, 0]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 1, 3, 0],
			[4, 3, 12, 0],
			[2, 1, 2, 0]	]		#	x, y = -1, 2	System of Linear Equations
main()

###################################################################################
## Infinite

matrix = [	[1, 1, 1, 6],
			[1, 2, 3, 10],
			[1, 2, 3, 10]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 1, 3, 0],
			[4, 3, 8, 0],
			[2, 1, 2, 0]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 2, 3, 14],
			[4, 5, 7, 35],
			[3, 3, 4, 21]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[ 1, -2,  1, -1,  0],
			[ 1,  1, -2,  3,  0],
			[ 4,  1, -5,  8,  0],
			[ 5, -7,  2, -1,  0]	]		#	x, y = -1, 2	System of Linear Equations
main()

####################################################################################
## No Soln

matrix = [	[0, 2, 3],
			[0, 0, 6],
			[0, 8, 9]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 1, 1, 6],
			[1, 2, 3, 10],
			[1, 2, 3, 5]	]		#	x, y = -1, 2	System of Linear Equations
main()

####################################################################################
## Unique

matrix = [	[1, 1, 1, 6],
			[1, 2, 3, 10],
			[1, 2, 5, 10]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 1, 1, 6],
			[1, 2, 3, 10],
			[1, 2, 5, 4]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 1, 1],
			[2, 1, 1],
			[3, 1, 1]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]	]		#	x, y = -1, 2	System of Linear Equations
main()

matrix = [	[1, 1, 1],
			[1, 2, 3],
			[2, 1, 0]	]		#	x, y = -1, 2	System of Linear Equations
main()


matrix = [	[1,  5, 6,  8],
			[4, -5, 1,  5],
			[5,  1, 6, 11]	]		#	x, y = -1, 2	System of Linear Equations
main()

####################################################################################
