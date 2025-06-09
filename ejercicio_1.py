print('Primer ejercicio de Python')
def suma(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b
def resta(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b
def multiplicacion(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b
def division(a, b):
    """Divide dos números y devuelve el resultado."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
def main():
    """Función principal que ejecuta las operaciones."""
    a = 10
    b = 5
    print(f"Suma: {suma(a, b)}")
    print(f"Resta: {resta(a, b)}")
    print(f"Multiplicación: {multiplicacion(a, b)}")
    print(f"División: {division(a, b)}")
if __name__ == "__main__":
    main()
    print("¡Ejecución completa!")
# Este es un comentario que explica el propósito del código
# Este código realiza operaciones matemáticas básicas y muestra los resultados.
