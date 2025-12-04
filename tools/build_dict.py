import os

INPUT_FILE = "../resources/br-utf8.txt"
OUTPUT_FILE = "../resources/dicionario.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f_in, \
    open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
    for linha in f_in:
        palavra = linha.strip()
        if len(palavra) == 5:
            f_out.write(palavra + "\n")
    print("Concluído!")
