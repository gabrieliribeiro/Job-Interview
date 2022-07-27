number = int(input("Informe um número: "))

first, second = 0, 1

if number < 0:
   print("Digite um número válido!")
   print("Sequência de Fibonacci não possui número negativo!")
else:
    while first < number:
        first, second = second, first + second

if first == number:
    print("Esse número pertence a sequência de Fibonacci.")
else:
    print("Esse número não pertence a sequência de Fibonacci.")

