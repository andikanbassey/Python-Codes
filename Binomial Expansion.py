#binomial Expansion
from math import factorial

def bistr(coff, a, n, r, b):
    """ display the binomial expression
    """
    s = ''
    if int(coff) != 1:
        s = s + coff + ' * '

    if n-r != 0:
        s = s + a
        if n-r != 1:
            s = s + '^' + str(n-r)

    if r != 0:
        if int(coff) != 1:
            s = s  + ' * '
        s = s + b
        if r != 1:
            s = s + '^' + str(r)

    if n != 1:
        s = '(' + s + ')'
    return s

def biexpand(a, b, n):
    """(a + b)^n = from r=0 to n compute c(n,r) * a^(n-r) * b^r
    """
    # calculate cofficient c(n,r)
    cnr = lambda n, r: factorial(n) / (factorial(r) * factorial(n-r))

    # print binomial expansion
    for r in range(n+1):
        coff = str(cnr(n, r))
        biexp = bistr(coff, a, n, r, b)
        # biexp = "(%s * %s^(%d-%d) * %s^%d)" % (coff, a, n, r, b, r)
        print (biexp)
        if r != n:
            print ('+'),

if __name__ == '__main__':
    a = 'a' # a = str(raw_input('Enter a : '))
    b = 'b' # b = str(raw_input('Enter b : '))

    print ('+a+' + '+b+'),
    n = int(raw_input('raise to power : '))

    biexpand(a, b, n)
