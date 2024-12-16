import random

l = int(input("Enter the security parameter: "))

X0 = random.getrandbits(l)
Y0 = random.getrandbits(l)
X1 = random.getrandbits(l)
Y1 = random.getrandbits(l)
t = random.getrandbits(l)

Z0 = (X0 & Y1) ^ t
Z1 = (X1 & Y0) ^ t

print(X0, Y0, Z0)
print(X1, Y1, Z1)
