"""
x + y = 5
2x - y = 1

| 1 1 | | x | = | 5 |
| 2 -1| | y |   | 1 |

A*u = b
u = inv(A)*b #x = 2; y = 3
"""
import numpy as np
from numpy.linalg import inv

A = np.matrix([[1,1],[2,-1]]) # 2x2 matrix
b = np.matrix([[5],[1]]) # 2x1 vector
u = inv(A)*b
print(u)

"""
x + y + z = 3
x - y - z = -1
2x + 3y + 4z = 9
"""
A = np.matrix([[1,1,1],[1,-1,-1],[2,3,4]])
b = np.matrix([[3],[-1],[9]])
u = inv(A)*b
print(u)

"""
-3x -y + z = 2
-5x -2y + z = 0
-7x + z = 0
"""
A = np.matrix([[-3,-1,1],[-5,-2,1],[-7,0,1]])
b = np.matrix([[2],[0],[0]])
u = inv(A)*b
print(u)
print(A*u)

A = np.matrix([[1,2],[3,4]])
b = np.matrix([[1],[2]])
u = inv(A)*b
print(u)