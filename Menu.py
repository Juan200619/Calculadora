import math
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while True:    
      
      print("""
      Indique la operación a realizar:
      
      1. Resta 
      2. Suma
      3. Multiplicación
      4. División
      5. raiz cuadrada
      6. potencia

            """)
      opcion = input("Ingrese la opción deseada (1-6): ")
      
      if opcion == "3":
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
      if opcion == "4":
            if num2 != 0:
                  resultado = num1 / num2
                  print(f"El resultado de la división es: {resultado}")
            else:
                  print("Error: División por cero no permitida.")
