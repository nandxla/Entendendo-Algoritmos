def regressiva(n):
    print(n)
    
    if n <= 1:
        # caso-base
        return 
    else:
        # caso recursivo
        regressiva(n - 1)

regressiva(10)