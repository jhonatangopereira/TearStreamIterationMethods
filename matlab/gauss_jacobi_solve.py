import numpy as np

def gauss_jacobi_solve(mx_a, b, func, iterations=25):
  mx_a = np.array(mx_a)
  l, c = mx_a.shape
  B = np.zeros((l, c))
  g = np.zeros(c)

  for i in range(l):
    B[i,:] = func(mx_a[i,:]) / mx_a[i, i]
    g[i] = b[i] / mx_a[i, i]
    B[i, i] = 0
  B = -B

  x = np.zeros(c)
  for j in range(iterations):
    x = np.dot(B, x) + g
  print(f"iterations: {j}\n      root: {x}")