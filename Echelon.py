#	Program to Convert a Matrix to Echelon Form

import numpy as np


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
