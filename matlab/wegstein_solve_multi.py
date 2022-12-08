import numpy as np

def wegstein_solve_multi(func, x0, xmax, xmin) -> tuple:
  x0, xmin, xmax = np.array(x0), np.array(xmin), np.array(xmax)

  iteration = 0

  while iteration < 100:
    iteration = iteration + 1
          
    x1 = np.array(func(x0))
    x2 = np.array(func(x1))
    fx2 = np.array(func(x2))

    a, b, slope, teta = np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2)
    for i in range(0, len(x1)):
      a[i] = x2[i] - x1[i]
      if a[i] == 0:
        slope[i] = 0
      else:
        slope[i] = (fx2[i] - x2[i]) / (x2[i] - x1[i])

      b[i] = 1 - slope[i]
      if b[i] == 1:
        teta[i] = 1
      else:
        teta[i] = 1/(1 - slope[i])

    if all(np.greater(teta, xmax)):
      teta = xmax  
    elif all(np.less(teta, xmin)):
      teta = xmin

    x0 = (1 - teta) * x2 + teta * fx2

    if abs(x0 - x1).all() <= (1e-6) * (abs(x0).all()): break

  return x0, iteration
