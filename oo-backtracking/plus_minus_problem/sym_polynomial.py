from sympy import symbols, expand

def get_coefficient(polynomial, a, b, c):

    x, y, z = symbols('x y z')

    # Extract the coefficient from the polynomial
    #coefficient = polynomial.coeff(x**a*y**b*z**c)
    coefficient = polynomial.coeff_monomial(x**15*y**15*z**15)

    return coefficient


def polynomial_product(n):
    x, y, z = symbols('x y z')
    product = 1

    for i in range(1, n+1):
        term = x**i + y**i + z**i
        product *= term
    return product



def main():
    # Create sympy.core.mul.Mul object:
    product = polynomial_product(9)
    # Convert into sympy.core.add.Add object:
    expanded_product = expand(product)
    print(expanded_product)
    # Convert into sympy.polys.polytools.Poly object:
    poly_product = product.as_poly()
    coeff_central = get_coefficient(poly_product, 15, 15, 15)
    print(coeff_central)



if __name__ == '__main__':
    main()