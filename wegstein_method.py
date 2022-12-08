# 3.3.3 Single-Variable Wegstein Method

def calculating_q(func, initial_value:float):
  """Auxiliar function to calculate q - necessary variable to wegstein method"""
  MAX_ITERATIONS = 2
  x = initial_value

  y_x = [x]
  for i in range(MAX_ITERATIONS):
    y_x.append(func(x))

    if y_x[-1] == 0: break

    x = y_x[-1]
  
  if len(y_x) == 3:
    a = (y_x[2] - y_x[1]) / (y_x[1] - y_x[0])
    q = a / (a - 1)
    return q, a


def wegstein_method(func, initial_value:float, tolerance:float=5e-8, max_iterations:int=200):
  """Implementing Wegstein method"""
  counter, error, x = 0, 1, initial_value

  # Calculating q
  q, a = calculating_q(func, initial_value)

  while tolerance < error and counter < max_iterations:
    y_x = q * x + (1 - q) * func(x)

    if y_x == 0:
      break

    error = np.abs((y_x - x) / y_x)
    x = y_x

    counter += 1
  print(f"iterations: {counter}\n      root: {x}")

x_squared_minus_x_minus_one = lambda x: x ** 2 - x - 1
one_plus_one_divide_x = lambda x: 1 + 1 / x
x_squared_minus_one = lambda x: x ** 2 - 1

wegstein_method(one_plus_one_divide_x, 2)

wegstein_method(x_squared_minus_one, 2)