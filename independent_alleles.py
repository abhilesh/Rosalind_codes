# Given : Two positive integers k and N (N<2**k). Tom, in the 0th generation has genotype AaBb. 
# Tom has two children in the first generation, each of whom have two children and so on. Each oragnism always mates with an AaBb organism
# Return : The probability that atleast N AaBb organisms will belong to the kth generation of Tom's family tree.

k = int(raw_input("Enter k: "))
N = int(raw_input("Enter N: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n - 1))

def combinations(n, r):
    return (factorial(n)/((factorial(r))*(factorial(n - r))))

x = 2**k
probability = 0.0

for i in range(N,(x) + 1):
    p = combinations(x, i) * ((0.25)**i)*((0.75)**((x)-i))
    probability += p

print probability