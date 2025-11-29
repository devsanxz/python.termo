import os
import random
import unicodedata

# === CORES E ESTILOS ===
RESET = "\033[0m"
VERDE = "\033[42;30m"
AMARELO = "\033[43;30m"
VERMELHO = "\033[41;97m"
ROXO = "\033[45;97m"

# === DADOS (MVP) ===
# Dicionário pequeno hardcoded
PALAVRAS_RAW = ["TERMO", "MORTE", "ONTEM", "METRO", "AUREO", "FESTA", "PORTA", "LIVRO", "SAGAZ"]

def remover_acentos(texto):
    # Normaliza para NFD (separa letra do acento) e filtra não-espaçados
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn").upper()

# Lista normalizada para validação
PALAVRAS_VALIDAS = [remover_acentos(p) for p in PALAVRAS_RAW]

def pintar(letra, estilo):
    return f"{estilo}[ {letra} ]{RESET}"

def main():
    os.system("clear")
    print(f"{ROXO}=== TERMO v2.0 (Logic Edition) ==={RESET}\n")
    
    # Escolhe uma palavra secreta aleatória
    SEGREDO_RAW = random.choice(PALAVRAS_RAW)
    SEGREDO = remover_acentos(SEGREDO_RAW)
    
    tentativas_restantes = 6
    
    while tentativas_restantes > 0:
        print(f"Tentativas restantes: {tentativas_restantes}")
        entrada = input("Digite 5 letras: ").strip().upper()
        tentativa_norm = remover_acentos(entrada)
        
        # 1. Validação de Tamanho
        if len(tentativa_norm) != 5:
            print(">>> Digite exatamente 5 letras!")
            continue
            
        # 2. Validação de Existência (Dicionário)
        if tentativa_norm not in PALAVRAS_VALIDAS:
            print(">>> Palavra desconhecida!")
            continue
            
        # === O ALGORITMO DE 3 PASSADAS ===
        
        # Listas mutáveis para processamento
        t_chars = list(tentativa_norm)
        s_chars = list(SEGREDO)
        s_copia = list(SEGREDO) # A vítima para depenar
        cores = [None] * 5      # Array de resultados
        
        # Passada 1: VERDES (Prioridade Máxima)
        for i in range(5):
            if t_chars[i] == s_chars[i]:
                cores[i] = VERDE
                s_copia[i] = None # Consome a letra exata da cópia
        
        # Passada 2: AMARELOS (O que sobrou)
        for i in range(5):
            if cores[i] is None: # Se ainda não foi resolvido
                letra = t_chars[i]
                if letra in s_copia:
                    cores[i] = AMARELO
                    # Encontra a primeira ocorrência e remove (depena)
                    idx = s_copia.index(letra)
                    s_copia[idx] = None 
        
        # Passada 3: VERMELHOS (Resto)
        for i in range(5):
            if cores[i] is None:
                cores[i] = VERMELHO
                
        # === RENDERIZAÇÃO ===
        linha_visual = ""
        for i in range(5):
            linha_visual += pintar(t_chars[i], cores[i]) + " "
            
        print(f"\n{linha_visual}\n")
        
        if tentativa_norm == SEGREDO:
            print(f"{VERDE} PARABÉNS! VOCÊ ACERTOU! {RESET}")
            break
            
        tentativas_restantes -= 1

    if tentativas_restantes == 0:
        print(f"{VERMELHO} PERDEU! A palavra era: {SEGREDO_RAW} {RESET}")

if __name__ == "__main__":
    main()
