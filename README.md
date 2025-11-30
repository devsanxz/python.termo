# Termo CLI (Python MVP)

Um clone robusto e eficiente do jogo Termo/Wordle, rodando inteiramente no terminal.

## 🐍 Engenharia & Algoritmo

Diferente de implementações ingênuas, este projeto foca na **correção lógica** das regras de coloração do Termo (lidando com letras repetidas e prioridades de feedback).

### O Algoritmo de 3 Passadas
Para garantir que as dicas (Verde/Amarelo/Vermelho) sejam 100% fiéis ao jogo original, implementamos uma lógica de três estágios com "depenação" (consumo) da palavra secreta:

1.  **Passada Verde (Prioridade Máxima):** Identifica e trava matches exatos (posição correta). Remove a letra correspondente da "cópia de trabalho" do segredo.
2.  **Passada Amarela (Descoberta):** Busca as letras restantes na "cópia de trabalho" (que já teve os verdes removidos). Isso evita falsos positivos (ex: marcar uma letra repetida como amarela se ela só existe uma vez na palavra e já foi encontrada).
3.  **Passada Vermelha (Fallback):** Tudo que não foi classificado acima é marcado como erro.

### Features Técnicas
*   **Normalização Unicode:** Utiliza `unicodedata` para sanitizar inputs. O usuário pode digitar `ÁUREO`, e o sistema processa `AUREO` transparentemente.
*   **Visualização ANSI:** Renderização de blocos coloridos no terminal para imitar a interface do jogo web.
*   **Validação de Dicionário:** Verifica se a palavra existe antes de gastar uma tentativa.

## 🚀 Como Rodar

1.  Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  Execute o jogo:
    ```bash
    python3 termo.py
    ```

---
*Codado para ser lido, mantido e expandido. Estilo SRE.*