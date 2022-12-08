""" MÉTODO DE WEGSTEIN """
def wegstein_solve(func, x0:float, xmax:float, xmin:float, tolerance:float=1e-10, max_iterations:int=100):
    for i in range(max_iterations):
        xi = func(x0) 
        xm = func(xi)

        slope = (xm - xi) / (xi - x0)
        teta = 1 / (1 - slope)
        
        if teta > xmax:
            teta = xmax
        elif teta < xmin:
          teta = xmin

        x0 = (1 - teta) * xi + teta * xm

        if abs(x0 - xi) <= (tolerance) * (abs(x0)): break
    return x0, i

def wegstein_model(x) -> float:
    nc8h10a = 100
    nc8h8a = 0
    nh2a = 0 
    nh2oa = 3000         
    nc8h10r = x 
    nc8h8r = 1.00469113
    nh2r = 0
    nh2or = 0
    nc8h10ri = nc8h10a + nc8h10r
    nc8h8ri = nc8h8a + nc8h8r
    nh2ri = nh2a + nh2r
    nh2ori = nh2oa + nh2or
    nc8h10ro = nc8h10ri - (0.65 * nc8h10ri)
    nc8h8ro = nc8h8ri + (0.65 * nc8h10ri)
    nh2ro = nh2ri + (0.65 * nc8h10ri)
    nh2oro = nh2ori
    nh2ow = nh2oro * 1
    nh2v = nh2ro * 1
    nc8h10oo = nc8h10ro * 1
    nc8h8oo = nc8h8ro * 1
    nc8h10p = nc8h10oo * 0.01
    nc8h8p = nc8h8oo * 0.99
    f = nc8h10a * 106.167 + nh2oa * 18.01 - nh2ow * 18.01 - nh2v * 2.016 - nc8h10p * 106.167 - nc8h8p * 104.15

    return f

print('---MÉTODO DE WEGSTEIN---')

x0 = float(input('Insira a estimativa inicial = '))

xmax = float(input('Insira o limite máximo = '))
xmin = float(input('Insira o limite mínimo = '))

root, iterations = wegstein_solve(wegstein_model, x0, xmax, xmin)

print(f'A raiz é = {root:.4f}')
print(f'O número de iterações foi = {iterations}')


print()