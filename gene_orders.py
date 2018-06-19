# Given: A positive integer n
# Return: The total number of permutations of length n, followed by a list of all such permutations.


n = int(raw_input("Enter the integer: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n - 1))
        
def permutations(n, r):
    return (factorial(n))/(factorial(n-r))

num_of_perms = permutations(n, n)
print num_of_perms

seq = ''
for i in range(1,n+1):
    seq += str(i)

# MODIFY THIS FUNCTION TO RETURN A VALUE. WORKS FOR NOW

def all_permutations(head, tail = ''):
        if len(head) == 0:
                print tail
        else:
                for i in range(len(head)):
                        all_permutations(head[:i] + head[i + 1:], tail + head[i])

print all_permutations(seq)