import unicodedata
from utils import clear_screen

"""
Escreva um programa que verifique, em uma string, 
a existência da letra ‘a’, seja maiúscula ou minúscula, 
além de informar a quantidade de vezes em que ela ocorre.
"""


def char_a_ocorrunce_in_string(string: str):
    mapping = {}

    for char in string:
        # Normaliza o caractere para remover acentos e converte para minúsculas
        char = (
            unicodedata.normalize("NFD", char)
            .encode("ascii", "ignore")
            .decode("utf-8")
            .lower()
        )

        if char.isalpha():
            if char in mapping:
                mapping[char] += 1
            else:
                mapping[char] = 1

    return mapping.get("a", 0)


if __name__ == "__main__":
    while True:
        try:
            string = str(input("Digite uma string: "))
            print(
                "'A' aparece:",
                char_a_ocorrunce_in_string(string),
                "vezes na string",
                f"'{string}'\n",
            )
        except (TypeError, ValueError):
            clear_screen()
            print("informe uma string válido! \n")
            continue
        except KeyboardInterrupt:
            clear_screen()
            exit(1)
