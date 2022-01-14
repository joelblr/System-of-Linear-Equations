#	Program to Find Solutions for a System of Linear Equations

import numpy as np
from fractions import Fraction

superscript_map	=	{
"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
"7": "⁷", "8": "⁸", "9": "⁹"}
subscript_map	=	{
"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
"7": "₇", "8": "₈", "9": "₉"}

##	To Find Solutions for a System of Linear Equations
def soln(augmatrix, flag) :

	if   flag < 0 :		#  Return [ϕ]				## For No Solutions

		U1 = ['ϕ'] * (len(augmatrix[0]) -1)

	elif flag == 0 :	#  Return [x1,x2,..,xn]		## For Unique Solutions

		U1 = [1 for i in augmatrix[0][:-1]]	+ [0]
		for i in range(len(augmatrix) -1, -1, -1) :
			m = augmatrix[i]
			U1[i] = (m[-1] -1*sum(list(np.multiply(U1[i+1:], m[i+1:]))))/(U1[i]*m[i-len(augmatrix)-1])
		U1.pop()
		U1 = list(map(str, U1))

	elif flag > 0 :		#  Return [x1,x2,..,xn]		## For Infinite Solutions

		U1 = [[0] + [0]*flag]*(len(augmatrix[0])-flag-1)
		U2 = [""] + ['k'+subscript_map[str(i+1)] for i in range(flag)]

		for i in range(flag):
			U1 += [[0] + [0]*flag]
			U1[-1][i+1] = 1

		for i in range( len(augmatrix) -1, -1, -1) :
			m = augmatrix[i]
			a = list([m[-1]/m[i]]) + list([0]*flag 	)
			b = [0]*(flag+1)
			for k,l in zip(U1[i+1:],m[i+1:-1]) :
				b = list(np.add(b, list(np.array(k)*l/-m[i])))
			U1[i] = list(np.add(a, b))

		for i in range(len(U1)) :
			U1[i], ch = list(map(str, U1[i])), ''
			for j,k in zip(U1[i], U2) :
				if   j == '0'				:	continue
				elif j == '1'				:	ch += k + ' + '
				elif U1[i].index(j) == 0	:	ch += j + ' + '
				else						:	ch += '(' + j + ')' + k + ' + '
			U1[i] = ch[:-3]

	print("\tSolutions")
	for i in range(len(U1)) :
		print(f"\t\tx{subscript_map[str(i+1)]} = {U1[i]}")
	if flag > 0 :
		print("\t\t\twhere kₙ ∊ Ɍ")
	return
