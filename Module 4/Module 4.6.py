import random
N = int(input("Number of random points you want to generate:"))
n = 0
count = 0
while count < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    count += 1
pi = 4*n/N
print(pi)
