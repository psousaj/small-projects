import sys
from utils import clear_screen

"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência.
"""


def is_in_fibonacci(number):
    if number == 0 or number == 1:
        return True

    fibonacci = [0, 1]

    # Enquanto o ultimo é menor ou igual ao numero
    while fibonacci[-1] <= number:
        # Adiciona a soma dos dois anteriores no array
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

    # Verifica se o número está no array
    return number in fibonacci


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Digite um número: "))
            print(is_in_fibonacci(n))
        except (TypeError, ValueError) as e:
            clear_screen()
            print("informe um número válido! \n")
            continue
        except KeyboardInterrupt:
            clear_screen()
            exit(1)
