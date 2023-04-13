
while True:
    estado = input("¿Desea realizar una operación? Y/N ")
    if estado == "N":
        print("Muchas gracias por haber usado la calculadora")
        break
    elif estado == "Y":
            seleccionOperacion = int(input("Elija la operación que desea realizar: \n1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Potenciación \n6. Raíz cuadrada \n7. Factorial \n8. Volver al inicio \n"))
            if seleccionOperacion > 0 and seleccionOperacion < 6:
                primerNumero =int(input("ingrese el primer número: "))
                segundoNumero =int(input("ingrese el segundo número: "))
                if seleccionOperacion == 1:
                    suma =primerNumero +segundoNumero
                    print("La Suma es:", suma)
                elif seleccionOperacion == 2:
                    resta =primerNumero -segundoNumero
                    print("La Resta es:", resta)
                elif seleccionOperacion == 3:
                    multiplicacion =primerNumero *segundoNumero
                    print("La Multiplicación es:", multiplicacion)
                elif seleccionOperacion == 4:
                    if segundoNumero != 0:
                        division =primerNumero /segundoNumero
                        print("La División es:", division)
                    else:
                        print("Error, no se puede dividir por 0")
                elif seleccionOperacion == 5:
                    potencia = int(primerNumero)**int(segundoNumero)
                    print("La potencia es: ", potencia)
            elif seleccionOperacion == 6:
                numeroRaiz = int(input("número para sacarle la raíz cuadrada: "))
                if numeroRaiz > 0:
                    print(numeroRaiz**0.5)
                else:
                    print("Sólo se puede calcular la raíz cuadrada de un número positivo")
            elif seleccionOperacion == 7:
                numeroFactorial = int(input("digite el número para generar el factorial: "))
                factorial = numeroFactorial
                for i in range(1, factorial, 1):
                    factorial = factorial*i
                print("El factorial de ",numeroFactorial, " es ", factorial)
            elif seleccionOperacion == 8:
                print("Volviendo al inicio")
                continue
            else:
                print("Error, eliga un número del 1 al 8 según el menú")
    else:
        print("digite la letra Y si quiere continuar o la N si desea salir")
        continue
