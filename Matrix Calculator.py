
#A python Program to multiply two matrices
#
f = int(input("Enter the size of rows for the first: "))
g = int(input("Enter the size of columns for the first: "))

q = int(input("Enter the size of rows for the second: "))
w = int(input("Enter the size of columns for the second: "))




#Function to Multiply Two Matrices
def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 :
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

matrixa = []
rowa = f
cola = g
while len(matrixa) < rowa:
    item = int(input("Enter your row Numbers For the 1st Matrix: "))
    matrixa.append(item)

while len(matrixa) < cola:
    item = int(input("Enter your column Numbers For the 1st Matrix: "))
    matrixa.append(item)
    print matrixa
print "That's your 1st Matrix"






matrixb = []
lengthb = g
while len(matrixb) < lengthb:
    ite = int(input("Enter your Numbers For the 2nd Matrix: "))
    matrixb.append(ite)
    print matrixb
print "That's your 2nd Matrix"
print matrixb


Matrix=matmult(matrixa,matrixb)
print("The product of the matrices is ",Matrix )

    #Function to find the Determinant of a Matrix
v = int(input("Enter the size of rows: "))
n = int(input("Enter the size of columns: "))
def det(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * det(m, sign * matrix[0][i])
        return total

matrix = [[1,3],[3,5]]
print("The Determinant of the matrix is:",det(matrix, 1))