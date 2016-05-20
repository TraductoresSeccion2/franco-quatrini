from prueba1 import ValidarCaracter
from prueba2 import ValidaNum

letra =  input("Ingresar palabra: ")
num = input("Ingresar números: ")
if ValidarCaracter(letra) == True and ValidaNum(num) == True:
    print ("Ingreso de palabras y numeros exitoso....por favor espera para entrar al sistema")
else:
    print ("Ingreso no exitoso... falla de sistema... reniciando")