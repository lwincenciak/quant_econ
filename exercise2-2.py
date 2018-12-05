# polynomial p evaluated at x with coefficients
# the number of coeffs defines the highest degree n-1
# if you specify 3 coeffs then you have a quadratic equation


def p(x, coeff):
    suma = 0
    for i, a in enumerate(coeff):
        suma = suma + a * x**i
    return suma

# return sum(a * x**i for i, a in enumerate(coeff))


print(p(1, (-2, 4, 2)))
