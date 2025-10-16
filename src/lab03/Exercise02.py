import sys
import os
# Add the path to the project root folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

def stats(tableMode: bool = False):
    print("Introduza o texto (para finalizar, prima Ctrl+Z numa nova linha): ")
    text = sys.stdin.read()    # Leitura de todas as entradas do stdin
    if not text.strip():
        print("Não digitou nenhum texto!!!") #No text entered.
        return
    normalized_text = normalize(text) # Normalizando o texto.
    tokens = tokenize(normalized_text) # Tokenizando o texto.
    # Calculating statistics
    total_words = len(tokens)  # Calcule o total de palavras.
    unique_words = len(set(tokens)) #Obtenha o total de palavras sem repetições.
    # Frequências e Top 5
    freq = count_freq(tokens)
    top_words = top_n(freq)
    if not tableMode:        
        #Os seus resultados
        print(f"Total de palavras: {total_words}")
        print(f"Total of Unique words: {unique_words}")
        print("Top 5:")
        for word, count in top_words:
            print(f"{word}:{count}")
    else:       
       max_word_len = max(len(word) for word, _ in top_words)
       print(f'{"Word":<{max_word_len}} | Frequência')
       print("-" * (max_word_len + 14))
       for word, count in top_words:
            print(f"{word:<{max_word_len}} | {count}")

if __name__ == "__principal__":
    stats()