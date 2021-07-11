import sys

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

try:
    n = int(input('Enter an integer: '))
except:
    print("That's not an integer")
    sys.exit(1)

i = 0
while n != 1:
    n = collatz(n)
    i += 1
    print(n)

print('finished in', i, 'iterations')

