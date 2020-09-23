class Funciones:
    def cuadrado(self):
        a = float(input("Cuanto mide el lado del cuadrado? "))
        print("El area del cuadrado es: ", a * a)

    def triangulo(self):
        a = float(input("Cuanto mide la base del triangulo? "))
        b = float(input("Cuanto mide la altura del triangulo? "))
        print("El area del triangulo es:", (a * b)/2)

    def circulo(self):
        a = float(input("Cuanto mide el radio del circulo? "))
        print("El area del circulo es: ", 3.14 * (a * a))

    def zodiaco(self):
        dia = int(input("Cual es tu dia de nacimiento? "))
        mes = int(input("Cual es tu mes de nacimiento? "))

        if (dia>=21 and mes==3) or (dia<=20 and mes==4):
            print ('Aries')
        elif (dia>=24 and mes==9) or (dia<=23 and mes==10):
            print ('Libra')
        elif (dia>=21 and mes==4) or (dia<=21 and mes==5):
            print ('Tauro')
        elif (dia>=24 and mes==10) or (dia<=22 and mes==11):
            print ('Escorpio')
        elif (dia>=22 and mes==5) or (dia<=21 and mes==6):
            print ('G\u00E9minis')
        elif (dia>=23 and mes==11) or (dia<=21 and mes==12):
            print ('Sagitario')
        elif (dia>=21 and mes==6) or (dia<=23 and mes==7):
            print ('C\u00E1ncer')
        elif (dia>=22 and mes==12) or (dia<=20 and mes==1):
            print ('Capricornio')
        elif (dia>=24 and mes==7) or (dia<=23 and mes==8):
            print ('Leo')
        elif (dia>=21 and mes==1) or (dia<=19 and mes==2):
            print ('Acuario')
        elif (dia>=24 and mes==8) or (dia<=23 and mes==9):
            print ('Virgo')
        elif (dia>=20 and mes==2) or (dia<=20 and mes==3):
            print ('Piscis')

    def factorial(self, n):
        f = 1
        i = 1
        while i <= n:
            f *= n
            i += 1
        return f
	
    # def numero(self):
    #     limite = int(input("Cual es el limite? "))
    #     n = 0
    #     e = 0
    #     while n < limite:
    #         e += 1 / a.factorial(n)
    #         n +=1
    #     print(e)
    #     return 0