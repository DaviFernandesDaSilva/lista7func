import random as r
import math
q = True
def menu():
    print("0 - Sair")
    print("1 - Valor em Dobro")
    print("2 - Data")
    print("3 - Positivo ou Negativo")
    print("4 - Quadrado Perfeito")
    print("5 - Hipotenusa")
    print("6 - Maior número")
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
def Q7():
    a = 0
def Q8():
    a = 0
def Q9():
    a = 0
def Q10():
    a = 0
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
        Q7()
    elif q == 8:
        Q8()
    else:
        print("Erro")