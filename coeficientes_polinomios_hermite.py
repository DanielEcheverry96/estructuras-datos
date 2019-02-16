def coeficientePolinomioHermite(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    return 2 * x * coeficientePolinomioHermite(n - 1, x) - 2 * (n - 1) * coeficientePolinomioHermite(n - 2, x)  


print(coeficientePolinomioHermite(2, 3))
