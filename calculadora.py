def Menu():
    """Funcion que se encarga de mostrar el menu principal"""
    print ("""
---------Calculadora------------
---------Menu Principal---------
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Verificación de número primo
6) Verificación de número palíndromo
7) Salir 
-------------------------------
""")

def es_primo(numero):
    """Funcion que se encarga de definir si un número es primo"""
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

def es_palindromo(numero):
    """Funcion que se encarga de definir si un número es palíndromo"""
    if str(numero) == str(numero)[::-1] :
        print("Si es un número palíndromo") 
    else: 
        print("No es un número palíndromo") 

def Calculadora():
    """Funcion principal que muestra menu y llama a las otras funciones"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <7):
        """Si se va a realizar una operacion, se piden 2 numeros, si se va a verificar se pide 1 """
        if opc <5:
             primer_numero = int(input("Ingrese un número\n"))
             segundo_numero = int(input("Ingrese otro número\n"))
        else:
            NumeroAVerificar = int(input("Ingrese número a verificar\n"))
        """Opciones disponibles """
        if (opc==1):
            print ("La Suma es:", primer_numero+segundo_numero)
            Menu()
            opc = int(input("Selecione Opcion\n"))
            
        elif(opc==2):
            print ("La Resta es:",primer_numero-segundo_numero)
            Menu()
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",primer_numero*segundo_numero)
            Menu()
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print ("La Division es:", primer_numero/segundo_numero)
              Menu()
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              Menu()
              opc = int(input("Selecione Opcion\n"))
        elif(opc==5):          
            es_primo(NumeroAVerificar)
            Menu()
            opc = int(input("Selecione Opcion\n"))
        elif(opc==6):
            es_palindromo(NumeroAVerificar)
            Menu()
            opc = int(input("Selecione Opcion\n"))
              
Calculadora()