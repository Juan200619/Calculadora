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


      if opcion == "1":
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
      elif opcion == "2":
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")


      
      if opcion == "3":
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
      if opcion == "4":
            if num2 != 0:
                  resultado = num1 / num2
                  print(f"El resultado de la división es: {resultado}")
            else:
                  print("Error: División por cero no permitida.")

      
      if opcion == "5":
            if num1 >= 0:
                  resultado = math.sqrt(num1)
                  print(f"La raíz cuadrada de {num1} es: {resultado}")
            else:
                  print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
      if opcion == "6":
            resultado = math.pow(num1, num2)
            print(f"{num1} elevado a la potencia de {num2} es: {resultado}")
      else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

