import wegstein_model, gauss_jacobi_solve

A = [[2.0,1.0], [5.0,7.0]]
b = [11.0, 13.0]

solution = gauss_jacobi_solve.gauss_jacobi_solve(A, b, wegstein_model.wegstein_model)
print(solution)