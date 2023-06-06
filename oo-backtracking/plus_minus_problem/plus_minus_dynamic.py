import sys

# Aplūkojam algoritmisku uzdevumu: Izrakstīti visi naturāli skaitļi no 1 līdz n augošā secībā. 
# Cik dažādos veidos var pirms katra no šiem skaitļiem ierakstīt "+" un "-" zīmes tā, 
# lai visu skaitļu summa būtu 0. 

def nice_output(P, n): 
    HALF = n*(n+1)//2
    for i in range(0, n+1):
        for j in range(-HALF, HALF + 1):
            print(P[i][j+HALF], end=' ')
        print()

# Compute the 
def plus_minus(n):
    HALF = n*(n+1)//2
    P = [ [0]*(2*HALF + 1) for i in range(n+1)]
    P[0][HALF] = 1
    for i in range(1, n+1):
        for j in range(-HALF, HALF+1):
            P[i][j+HALF] += P[i-1][j-i+HALF]
            if j+i+HALF <= 2*HALF:
                P[i][j+HALF] += P[i-1][j+i+HALF]
    result = [P[i][HALF] for i in range(0,n+1)]
    nice_output(P,n)
    return result

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python plus_minus_problem.py <n>')
        exit(0)
    n = int(sys.argv[1])
    aa = plus_minus(n)
    print(aa)
    # pairs = [(i,aa[i] % 4) for i in range(len(aa))]
    # for pair in pairs:
    #     if pair[1] == 2:
    #         print(pair)


