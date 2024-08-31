import sys
from utils import clear_screen

"""
Escreva um programa que inverta os caracteres de um string.
"""


def reverse_string(string):
    chars = [c for c in string]
    # Dois ponteiros indicando início e fim do array
    x, y = 0, len(chars) - 1
    while x < y:
        first_original_number = chars[x]
        chars[x] = chars[y]
        chars[y] = first_original_number
        #
        x += 1
        y -= 1

    return "".join(chars)


if __name__ == "__main__":
    while True:
        try:
            string = str(input("Digite uma string: "))
            print(reverse_string(string))
        except (TypeError, ValueError):
            clear_screen()
            print("informe uma string válido! \n")
            continue
        except KeyboardInterrupt:
            clear_screen()
            sys.exit(1)
