from Consistency import consistent
from Solution import soln
from Echelon import echelon
from fractions import Fraction

##	__Main__
def main(matrix) :

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

	echelon(matrix)

	m = [[Fraction(str(j)).limit_denominator(100) for j in i] for i in matrix]
	m, flag, mess = consistent(m)
	print('*'*80)

	soln(m, flag)
	print(f"{'<'*80}\n")


if __name__ == "__main__" :
    from Inputs import OBJ
    for key in OBJ :
        main(OBJ[key])