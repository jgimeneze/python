# coding:utf-8
"""Sumamos operando1 (entero) y operando2 (entero)
Devolvemos el resultado (entero)
"""
def sumar(operando1,operando2):
    return operando1+operando2


#############################################################################
if __name__ == "__main__":
    num1=0
    num2=0


    num1=int(input("Introduce número1: "))
    num2=int(input("Introduce número2: "))

    total=sumar(num1,num2)

    print("La suma de " , num1, " y " , num2, "es igual a ",
