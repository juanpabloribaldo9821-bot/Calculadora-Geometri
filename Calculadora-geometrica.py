opcion = 0

while opcion != 11:
    print("\n--- Hola bienvenido a la Calculadora de figuras ---")
    print("1. Área de cuadrado")
    print("2. Perímetro de cuadrado")
    print("3. Área de rectángulo")
    print("4. Perímetro de rectángulo")
    print("5. Área de triángulo")
    print("6. Perímetro de triángulo")
    print("7. Área de triángulo rectángulo")
    print("8. Hipotenusa de triángulo rectángulo")
    print("9. Mostrar menú otra vez")
    print("10. Área de círculo")
    print("11. Salir")

    entrada_opc = input("\nElige una opción: ")
 
    if entrada_opc.isdigit():
        opcion = int(entrada_opc)
    else:
        print("Error: Por favor ingresa un número entero del 1 al 11.")
        opcion = 0  
        continue

    if opcion == 1:
        lado_in = input("Ingresa el lado: ")
        if lado_in.replace('.', '', 1).isdigit() and float(lado_in) >= 0:
            lado = float(lado_in)
            print("Área del cuadrado:", lado * lado)
        else:
            print("Error: El dato debe ser un número positivo.")

    elif opcion == 2:
        lado_in = input("Ingresa el lado: ")
        if lado_in.replace('.', '', 1).isdigit() and float(lado_in) >= 0:
            lado = float(lado_in)
            print("Perímetro del cuadrado:", 4 * lado)
        else:
            print("Error: El dato debe ser un número positivo.")

    elif opcion == 3:
        b_in = input("Ingresa la base: ")
        h_in = input("Ingresa la altura: ")
        if b_in.replace('.', '', 1).isdigit() and h_in.replace('.', '', 1).isdigit():
            base, altura = float(b_in), float(h_in)
            if base >= 0 and altura >= 0:
                print("Área del rectángulo:", base * altura)
            else:
                print("Error: No se permiten números negativos.")
        else:
            print("Error: Ingresa números válidos.")

    elif opcion == 4:
        b_in = input("Ingresa la base: ")
        h_in = input("Ingresa la altura: ")
        if b_in.replace('.', '', 1).isdigit() and h_in.replace('.', '', 1).isdigit():
            base, altura = float(b_in), float(h_in)
            if base >= 0 and altura >= 0:
                print("Perímetro del rectángulo:", 2 * (base + altura))
            else:
                print("Error: No se permiten números negativos.")
        else:
            print("Error: Ingresa números válidos.")

    elif opcion == 5 or opcion == 7:
        b_in = input("Ingresa la base: ")
        h_in = input("Ingresa la altura: ")
        if b_in.replace('.', '', 1).isdigit() and h_in.replace('.', '', 1).isdigit():
            base, altura = float(b_in), float(h_in)
            if base >= 0 and altura >= 0:
                print("Área:", (base * altura) / 2)
            else:
                print("Error: No se permiten números negativos.")
        else:
            print("Error: Ingresa números válidos.")

    elif opcion == 6:
        l1 = input("Lado 1: ")
        l2 = input("Lado 2: ")
        l3 = input("Lado 3: ")
        if l1.replace('.', '', 1).isdigit() and l2.replace('.', '', 1).isdigit() and l3.replace('.', '', 1).isdigit():
            a, b, c = float(l1), float(l2), float(l3)
            if a >= 0 and b >= 0 and c >= 0:
                print("Perímetro del triángulo:", a + b + c)
            else:
                print("Error: No se permiten números negativos.")
        else:
            print("Error: Ingresa números válidos.")

    elif opcion == 8:
        c1 = input("Cateto 1: ")
        c2 = input("Cateto 2: ")
        if c1.replace('.', '', 1).isdigit() and c2.replace('.', '', 1).isdigit():
            a, b = float(c1), float(c2)
            if a >= 0 and b >= 0:
                hipotenusa = (a*2 + b2)*0.5
                print("Hipotenusa:", hipotenusa)
            else:
                print("Error: Los catetos deben ser positivos.")
        else:
            print("Error: Ingresa números válidos.")

    elif opcion == 9:
        print("Cargando menú...")

    elif opcion == 10:
        r_in = input("Ingresa el radio: ")
        if r_in.replace('.', '', 1).isdigit():
            radio = float(r_in)
            if radio >= 0:
                print("Área del círculo:", 3.1416 * (radio**2))
            else:
                print("Error: El radio no puede ser negativo.")
        else:
            print("Error: Ingresa un número válido.")

    elif opcion == 11:
        print("Saliendo del programa... ¡Adiós!")

    else:
        print("Opción no válida. Intenta de nuevo.")