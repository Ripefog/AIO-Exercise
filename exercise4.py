def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def approx_sin(x, n):
    result = 0
    for i in range(n):
        temp = ((-1)**i)*(x**(2*i))/factorial(2*i+1)
        result += temp
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result
