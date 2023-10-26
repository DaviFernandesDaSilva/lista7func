import random as r
import math
q = True
def menu():

    print("\033[91m0 - Sair\033[0m")
    print("\033[93m1 - Valor em Dobro\033[0m")
    print("\033[94m2 - Data\033[0m")
    print("\033[91m3 - Positivo ou Negativo\033[0m")
    print("\033[93m4 - Quadrado Perfeito\033[0m")
    print("\033[95m5 - Hipotenusa\033[0m")
    print("\033[94m6 - Maior número\033[0m")
    print("\033[93m7 - Soma dos Algarismos de um Número\033[0m")
    print("\033[91m8 - Desenha Linha\033[0m")
    print("\033[96m9 - Soma dos Números Inteiros entre Dois Números\033[0m")
    print("\033[95m10 - Cálculo Manual de Potência\033[0m")
    print("\033[92m11 - Maior Fator Primo\033[0m")
    print("\033[94m12 - Quantidade de Números Primos Abaixo de N\033[0m")
    print("\033[93m13 - Padrão de Exclamações\033[0m")
    print("\033[91m14 - Triângulo Lateral\033[0m")
    print("\033[96m15 - Soma dos Algarismos de N!\033[0m")
    print("\033[95m16 - Triângulo\033[0m")
    print("\033[92m17 - Cosseno usando Série de Taylor\033[0m")
    print("\033[94m18 - Fatorial Duplo\033[0m")
    print("\033[93m19 - Operações com Vetores\033[0m")
    print("\033[91m20 - Valores Maiores que 10 numa Matriz 4x4\033[0m")
    print("\033[96m21 - Verificar Matriz Identidade (13x13)\033[0m")
    print("\033[95m22 - Soma de uma Coluna numa Matriz (32x23)\033[0m")



    
    print("Qual questão deseja executar?")

def Q1():
    def func(x):
        return x*2

    a = r.randint(-10,10)

    print(f"{a} em dobro é {func(a)}")

def Q2(dia,mes,ano):
    if 1<=mes<=12 or 1<=dia<=31:
        if mes == 1:
            mes = 'janeiro'
        elif mes == 2:
            mes = 'fevereiro'
        elif mes == 3:
            mes = 'março'
        elif mes == 4:
            mes = 'abril'
        elif mes == 5:
            mes = 'maio'
        elif mes == 6:
            mes = 'junho'
        elif mes == 7:
            mes = 'julho'
        elif mes == 8:
            mes = 'agosto'
        elif mes == 9:
            mes = 'setembro'
        elif mes == 10:
            mes = 'outubro'
        elif mes == 11:
            mes = 'novembro'
        elif mes == 12:
            mes = 'dezembro'
    else:
        return print("Inválido")
    
    return print(f"{dia} de {mes} de {ano}")
    
def Q3(num):
    if num>0:
        return 1
    elif num<0:
        return -1
    else:
        return 0
    
def Q4(num):
    if num < 0:
        return False
    else:
        raiz = int(num ** 0.5)
        if raiz*raiz == num:
            return True
def Q5(a,b):
    h = math.sqrt( ( (a**2) + (b**2) ) )
    return h
def Q6(n1,n2):
    if n1>n2:
        return print(f"{n1} maior que {n2}")
    if n1<n2:
        return print(f"{n2} maior que {n1}")
    if n1==n2:
        return print(f"{n1} igual a {n2}")
def Q7(num):
    if num>0:
        numS = str(num)
        soma = 0

        for x in numS:
            soma += int(x)

        return print(soma)
    else:
        print("Número Inválido")

def Q8(num):
    return print(num*"=")

def Q9(num1,num2):
    if num1>0 and num2>0:
        soma = 0
        for x in range(num1, num2+1):
            soma += x
        return print(soma)
    else:
        print("Ambos devem ser números inteiros positivos")

def Q10(x,y):
    return print(x**y)
def Q11():
    a = 0
def Q12():
    a = 0
def Q13():
    a = 0
def Q14():
    a = 0
def Q15():
    a = 0
def Q16():
    a = 0
def Q17():
    a = 0
def Q18():
    a = 0
def Q19():
    a = 0
def Q20():
    a = 0
def Q21():
    a = 0
def Q22():
    a = 0
    

while q:
    print(" ")
    menu()
    q = int(input(": "))
    if q == 0:
        q = False
        print("Fim")
        break
    elif q == 1:
        Q1()
    elif q == 2:
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        ano = int(input("Ano: "))
        Q2(dia,mes,ano)
    elif q == 3:
        num = int(input("Digite um número: "))
        print(Q3(num))
    elif q == 4:
        num = int(input("Digite um número: "))
        eoun = Q4(num)
        if eoun:
            print(f"{num} é um quadrado perfeito")
        else:
            print(f"{num} não é um quadrado perfeito")
    elif q == 5:
        a = int(input("Digite o cateto A: "))
        b = int(input("Digite o cateto B: "))
        print(f"Hipotenusa: {Q5(a,b):.2f}")
    elif q == 6:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        Q6(num1,num2)
    elif q == 7:
        num = int(input("N>0: "))
        Q7(num)
    elif q == 8:
        num = int(input("Desenha Linha: "))
        Q8(num)
    elif q == 9:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        Q9(num1,num2)
    elif q == 10:
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        Q10(x,y)
    elif q == 11:

        Q11()
    elif q == 12:
        Q12()
    elif q == 13:
        Q13()
    elif q == 14:
        Q14()
    elif q == 15:
        Q15()
    elif q == 16:
        Q16()
    elif q == 17:
        Q17()
    elif q == 18:
        Q18()
    elif q == 19:
        Q19()
    elif q == 20:
        Q20()
    elif q == 21:
        Q21()
    elif q == 22:
        Q22()
    else:
        print("Erro")