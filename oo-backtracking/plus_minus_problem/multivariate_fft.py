import numpy as np

def find_coeff(n, a, b, c):
    # Initialize a zero array of size (n+1)x(n+1)x(n+1)
    # coef = np.zeros((n + 1, n + 1, n + 1))

    mycoef = np.zeros((n + 1, n + 1, n + 1))


    # Set coefficients for the initial polynomials
    for i in range(1, 2):
        mycoef = np.zeros((n + 1, n + 1, n + 1))

        mycoef[i, 0, 0] = 1
        mycoef[0, i, 0] = 1
        mycoef[0, 0, i] = 1

        print(mycoef)

        # Perform n-fold 3D FFT
        fft_coef = np.fft.fftn(mycoef)

        # Compute the power of the FFT
        pow_fft = fft_coef.copy()
        pow_fft *= fft_coef

    # Perform inverse FFT to get the coefficients
    result_coef = np.fft.ifftn(pow_fft)
    array_real = np.real(result_coef)  # Convert to real numbers
    array_rounded = np.round(array_real)  # Round to the closest integer
    array_integer = array_rounded.astype(int)
    return array_integer
    # Return the requested coefficient, rounded to integer (due to possible floating-point error)
    # return int(round(result_coef[a, b, c].real))

# Example usage
n = 2
a = 15
b = 15
c = 15

arr = find_coeff(n, a, b, c)
print(arr)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            coeff = arr[i][j][k]
            if coeff != 0:
                if coeff != 1:
                    print(f" + {coeff}", end='')
                if i > 0:
                    print(f"x^{i}", end='')
                if j > 0:
                    print(f"y^{j}", end='')
                if k > 0:
                    print(f"z^{k}", end='')

print()
