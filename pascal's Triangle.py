import math

# pascals_tri_formula = [] # don't collect in a global variable.
a = int(input("Enter the size of the triangle desired: "))

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascals_triangle(rows):
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result

for row in pascals_triangle(a):
    print(row)
