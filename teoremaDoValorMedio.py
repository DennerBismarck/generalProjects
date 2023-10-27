import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def calculador_derivadas(funcao, variavel, ponto):
    x = sp.symbols(variavel)
    f_x = sp.sympify(funcao)
    derivada = sp.diff(f_x, x)
    funcao_python = sp.lambdify(x, f_x, 'numpy')
    derivada_python = sp.lambdify(x, derivada, 'numpy')
    x_vals = np.linspace(ponto - 5, ponto + 5, 400)
    y_vals = funcao_python(x_vals)
    derivada_vals = derivada_python(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'{funcao}', color='blue')
    plt.plot(x_vals, derivada_vals, label=f'Derivada de {funcao}', color='red')
    plt.xlabel(variavel)
    plt.ylabel('f(x)')
    plt.axvline(x=ponto, color='green', linestyle='--', label=f'Ponto: {ponto}')
    plt.legend()
    plt.grid(True)
    plt.title('Gráfico da Função e sua Derivada')
    plt.show()

def calculador_teorema_valor_medio(ponto, funcao):
    x = sp.symbols('x')
    a = ponto - 5
    b = ponto + 5
    
    funcao_python = sp.lambdify(x,funcao,'numpy')

    fa = funcao_python(a)
    fb = funcao_python(b)

    valor_medio = (fb-fa)/(b-a)

    return valor_medio

funcao = ("(x**3 + 2*x)**2")
variavel = "x"
ponto = 0

calculador_derivadas(funcao, variavel, ponto)
print(calculador_teorema_valor_medio(ponto, funcao))
