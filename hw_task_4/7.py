import numpy as np


def matrix_expression(A, S, last = False):
  B = np.random.random((S,len(A)))
  print(B)
  AB = A*B
  print(AB)
  summ=np.sum(AB, axis =1)
  print(summ)
  if last == False:
    arr = np.sin(summ)
  else:
    arr = np.maximum(summ, 0)

  return arr


#test1
X =5
S = 10
A = np.random.random(X)
print(A)
res1 = matrix_expression(A, S, last = False)
print(res1)

#test2
A = res1
S=10
print(A)
res2 = matrix_expression(A, S, last = False)
print(res2)


#test3
S=5
A = res2
print(A)
res3= matrix_expression(A, S, last = True)
print(res3)



