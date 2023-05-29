# from scipy import signal
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# y = signal.fftconvolve(a, b, mode='full')
# print('The convoluted sequence is ', y)

import numpy as np
import sys

def multiply_polynomials(a, b):
    # Find the size of the arrays that will store the coefficients of the polynomials
    n = len(a) + len(b) - 1

    # Pad the coefficient arrays with zeros to the next power of 2
    N = 1 << (n - 1).bit_length()

    # Perform the FFT on both polynomials
    fft_a = np.fft.fft(a, N)
    fft_b = np.fft.fft(b, N)

    # Multiply the FFT results element-wise
    fft_product = fft_a * fft_b

    # Inverse FFT to get the product polynomial
    product = np.fft.ifft(fft_product)

    # Round the coefficients to the nearest integer and return the result
    return np.round(product.real)[:n]


def main(n):
    # will accumulate the product in this variable:
    prod = [1]
    # Example usage
    for i in range(n+1):
        if i % 10 == 0 and i > 0:
            print()
        poly_i = [0]*(2*i + 1) # x^2 + 1
        poly_i[0] = 1
        poly_i[2*i] = 1
        # b = [1, 0, 0, 0, 1] # x^4 + 1
        product_float = multiply_polynomials(prod, poly_i)
        prod = [int(x) for x in product_float]
        # print(product1)
        print('a[{}]={},'.format(i, prod[i*(i+1)//2]), end=' ')
        # print('prod[{}] = {}; {}'.format(i, prod, i*(i+1)))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: poly1_convolve.py 99')
    else:
        n = int(sys.argv[1])
        # print('n = {}'.format(n))
        main(n)

