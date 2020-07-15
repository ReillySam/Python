 # ================================================== MATRIX ==================================================
'''
    Matrices (sometimes called 2D or multidimensional arrays) are containers for many values. For example, 
    a tic tac toe board is a 2D matrix of 3 rows and 3 columns, each holding a character
    (usually 'x', 'o', and ' '). Matrixes have all the same properties as Arrays and are indexed in the same 
    manner, just using multiple "indexes", one for each row, column, etc.
 '''

# ========================================= Working with Matrices ================================================

import numpy as np

# Creating a matrix
m = np.array([[1, 2, 4, 6], [2, 4, 3, 5], [0, 1, 1, 7]])
print('Matrix 1: \n', m,'\n')

# Generate matrix
m2 = np.arange(1,10)

print('Matrix 2: \n', m2,'\n')
print('Matrix 2 reshaped: \n',(m2.reshape(3,3)),'\n')

# Transpose
m3 = np.array([[1, 2, 4, 6], [2, 4, 3, 5]])
m_transpose = m3.transpose()
print('Transposing matrix 3: \n', m_transpose, '\n')

# Multiply matrices using dot()
m4 = np.arange(1, 10).reshape(3, 3)
m5 = np.arange(5, 14).reshape(3, 3)
print('Matrix 4: \n', m4, '\n')
print('Matrix 5: \n', m5, '\n')

m6 = m4.dot(m5)
print('Matrix 4 x Matrix 5: \n', m6, '\n')

 # ============================================ Matrix Exercises ================================================
