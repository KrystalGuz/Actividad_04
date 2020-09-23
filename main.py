from funciones import Funciones

a = Funciones()

while True:
    print('1) Areas')
    print('2) Zodiaco')
    print('3) Calcular e')
    print('0) Salir')
    op = input()

    if op == "1":
        while True:
            print('1) Cuadrado')
            print('2) triangulo')
            print('3) Circulo')
            print('0) Salir')
            opc = input()

            if opc == "1":
                a.cuadrado()
            elif opc == "2":
                a.triangulo()
            elif opc == "3":
                a.circulo()
            elif opc == "0":
                break
            
    elif op == "2":
        a.zodiaco()
    elif op == "3":
        limite = int(input("Cual es el limite? "))
        n = 0
        e = 0
        while n < limite:
            e += 1 / a.factorial(n)
            n +=1
        print(e)
        
    elif op == "0":
        break