import os
import random
import unicodedata

# === CORES E ESTILOS ===
RESET = "\033[0m"
VERDE = "\033[42;30m"
AMARELO = "\033[43;30m"
VERMELHO = "\033[41;97m"
ROXO = "\033[45;97m"

# === CONFIGURAÇÃO ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICIO_PATH = os.path.join(BASE_DIR, "resources", "dicionario.txt")
MAX_TENTATIVAS = 7  # Jogo "5ETE"

def carregar_palavras():
    if not os.path.exists(DICIO_PATH):
        print(f"ERRO: Dicionário não encontrado em {DICIO_PATH}")
        print("Rode 'python3 tools/build_dict.py' primeiro.")
        exit(1)
    
    with open(DICIO_PATH, "r", encoding="utf-8") as f:
        # Lê, remove quebras de linha e normaliza
        return [linha.strip().upper() for linha in f if len(linha.strip()) == 5]

# Carrega no início (Cache)
PALAVRAS_VALIDAS = carregar_palavras()

def remover_acentos(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn").upper()

# Lista normalizada para validação rápida (Set é O(1))
PALAVRAS_NORM = set(remover_acentos(p) for p in PALAVRAS_VALIDAS)

def pintar(letra, estilo):
    return f"{estilo}[ {letra} ]{RESET}"

def main():
    os.system("clear")
    print(f"{ROXO}=== 5ETE (Termo SRE) ==={RESET}\n")
    
    # Escolhe segredo
    SEGREDO_RAW = random.choice(PALAVRAS_VALIDAS)
    SEGREDO = remover_acentos(SEGREDO_RAW)
    
    tentativas = 0
    
    while tentativas < MAX_TENTATIVAS:
        print(f"Tentativa {tentativas + 1} de {MAX_TENTATIVAS}")
        try:
            entrada = input("Digite: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo...")
            break

        tentativa_norm = remover_acentos(entrada)
        
        # Validações
        if len(tentativa_norm) != 5:
            print(">>> 5 letras, por favor.")
            continue
            
        if tentativa_norm not in PALAVRAS_NORM:
            print(">>> Palavra desconhecida!")
            continue
            
        # Lógica de 3 Passadas (Preservada da v1.0)
        t_chars = list(tentativa_norm)
        s_chars = list(SEGREDO)
        s_copia = list(SEGREDO)
        cores = [None] * 5
        
        # 1. Verdes
        for i in range(5):
            if t_chars[i] == s_chars[i]:
                cores[i] = VERDE
                s_copia[i] = None
        
        # 2. Amarelos
        for i in range(5):
            if cores[i] is None:
                letra = t_chars[i]
                if letra in s_copia:
                    cores[i] = AMARELO
                    idx = s_copia.index(letra)
                    s_copia[idx] = None
        
        # 3. Vermelhos
        for i in range(5):
            if cores[i] is None:
                cores[i] = VERMELHO
                
        # Renderiza
        linha_visual = ""
        for i in range(5):
            linha_visual += pintar(t_chars[i], cores[i]) + " "
            
        print(f"\n{linha_visual}\n")
        
        if tentativa_norm == SEGREDO:
            print(f"{VERDE} VICTORY! A palavra era {SEGREDO_RAW} {RESET}")
            break
            
        tentativas += 1

    if tentativas == MAX_TENTATIVAS:
        print(f"{VERMELHO} GAME OVER. Era: {SEGREDO_RAW} {RESET}")

if __name__ == "__main__":
    main()