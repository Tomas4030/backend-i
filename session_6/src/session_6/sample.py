def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

