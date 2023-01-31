from sympy import zeros, BlockMatrix, Matrix, symbols, eye, cos, det, sin, diff, pprint, simplify, pi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
theta1, theta2, l1, l2, m1, m2, m, g = symbols('theta1, theta2, l1, l2, m1, m2, m, g')
A = Matrix([[0,1,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,0,0,1],
            [0,0,-m1*g/m,0,-m2*g/m,0],
            [0,0,-((m1+m)*g/(m*l1)),0,((-m2*g)/(m*l1)),0,0,0],
            [0,((-m2*g)/(m*l2)),-((m1+m)*g/(m*l2)),0,0,0]])
print("state space matrix A is")
pprint(A)
A2 = A*A
# pprint(A2)
A3 = A2*A
A4 = A3*A
A5 = A4*A
A6 = A5*A
B = Matrix([0,0,0,1/m,1/(m*l1),1/(m*l2)])
print("control input matrix B is")
B1 = A*B
B2 = A2*B
B3 = A3*B
B4 = A4*B
B5 = A5*B
pprint(B)
ControllabilityMatrix = [B, B1, B2, B3, B4, B5]
print("controllability matrix C is")
pprint(ControllabilityMatrix)

A = A.evalf(subs={m:1000, m1:100, m2:100, l1:20, l2:10, g:9.8})
B = B.evalf(subs={m:1000, m1:100, m2:100, l1:20, l2:10, g:9.8})
C = Matrix([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0]])

pprint(A)
pprint(B)
pprint(C)
# C.det()
# C = C.evalf(subs={m:1000, m1:100, m2:100, l1:20, l2:10, g:9.8})
