import wegstein_model, wegstein_solve_multi

#--- MÉTODO DE WEGSTEIN ---

print('---MÉTODO DE WEGSTEIN---')

x0 = list(map(int, input('Insira a estimativa inicial = ').split()))

xmax = list(map(int, input('Insira o limite máximo = ').split()))
xmin = list(map(int, input('Insira o limite mínimo = ').split()))

ROOT, ITER = wegstein_solve_multi.wegstein_solve_multi(wegstein_model.wegstein_model, x0, xmax, xmin)

print(f'A raiz é = [{ROOT[0]:.4f}, {ROOT[1]:.4f}]')
print(f'O número de iterações foi = {ITER}')
