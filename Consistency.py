#	Program to Check if a given Augmented Matrix is Consistent.
#comment
##	To Check if a given Augmented Matrix is Consistent.
def consistent(matrix) :

	n = len(matrix[0]) - 1		#	Number of Unknowns - System of Linear Equations
	r1, r = 0, 0				#	Rank of Augmented, Coefficient Matrices
	coeffmatrix = []			#	Coefficient Matrix
	augmatrix   = []

	for i in range(len(matrix)) :
		if [0]*(n + 1) != matrix[i] :
			augmatrix.append(matrix[i])
	r1 = len(augmatrix)			#	Rank of Augmented Matrix

	for i in range(len(matrix)) :
		if [0]*n != matrix[i][ : -1] :
			coeffmatrix.append(matrix[i][ : -1])
	r2 = len(coeffmatrix)		#	Rank of Coefficient Matrix

	if r1 == r2 == n :
		mess = "System is Consistent with a Unique Solution"
		return (augmatrix, n-r1, mess)
	if r1 == r2 :
		mess = "System is Consistent with Infinite Solutions\nSelecting "+str(n-r1)+" Variables Arbitrarily  :  Say the last "+str(n-r1)+" Variables"
		return (augmatrix, n-r1, mess)
	if r1 != r2 :
		mess = "System is Inconsistent"
		return (augmatrix,   -n, mess)
