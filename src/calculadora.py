from operaciones import suma, resta, multiplicacion, division, potencia, division_entera

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /, **, //): ")

        if operador == '+':
            resultado = suma(a, b)
        elif operador == '-':
            resultado = resta(a, b)
        elif operador == '*':
            resultado = multiplicacion(a, b)
        elif operador == '/':
            resultado = division(a, b)
        elif operador == '**':
            resultado = potencia(a, b)
        elif operador == '//':
            resultado = division_entera(a, b)
        else:
            print("Operador inválido.")
            return

        print(f"Resultado: {resultado}")

    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
    except ValueError:
        print("Error: Entrada no numérica.")

if __name__ == "__main__":
    main()