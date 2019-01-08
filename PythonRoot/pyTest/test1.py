import numpy as np 

a = [str(X) + str(Y) + str(Z) for X in range(1,5) for Y in range(1,5) for Z in range(1,5) if X != Y and X != Z and Y != Z ]

print(a)