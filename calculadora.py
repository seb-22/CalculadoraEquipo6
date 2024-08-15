# Función para realizar la suma
def sum_numbers():
    a = float(input("Escribe el primer número: "))
    b = float(input("Escribe el segundo número: "))
    return a + b

# Función para realizar la resta
def subtract_numbers():
    a = float(input("Escribe el primer número: "))
    b = float(input("Escribe el segundo número: "))
    return a - b

# Función para realizar la división
def divide_numbers():
    try:
        numerator = float(input("Escribe el numerador: "))
        denominator = float(input("Escribe el denominador: "))
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: La división entre 0 no es posible."
    except ValueError:
        return "Error: Por favor ingrese solo valores numéricos."

# Función para realizar la multiplicación
def multiply_numbers():
    a = float(input("Escribe el primer número: "))
    b = float(input("Escribe el segundo número: "))
    return a * b

# Menú de operaciones
def menu():
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. División")
    print("4. Multiplicación")
    print("5. Salir")

    while True:
        choice = input("Escribe el número de la operación (1/2/3/4/5): ")

        if choice == '1':
            result = sum_numbers()
            print(f"El resultado de la suma es: {result}")
        elif choice == '2':
            result = subtract_numbers()
            print(f"El resultado de la resta es: {result}")
        elif choice == '3':
            result = divide_numbers()
            print(f"El resultado de la división es: {result}")
        elif choice == '4':
            result = multiply_numbers()
            print(f"El resultado de la multiplicación es: {result}")
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
