import sys
import os
# Add the path to the project root folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

def stats(tableMode: bool = False):
    print("Enter text (to finish, press Ctrl+Z on a new line): ")
    text = sys.stdin.read()    # Reading all input from stdin
    if not text.strip():
        print("You have not entered any text!!!") #No text entered.
        return
    normalized_text = normalize(text) # Normalizing the text.
    tokens = tokenize(normalized_text) # Tokenizing the text.
    # Calculating statistics
    total_words = len(tokens)  # Calculate the total words.
    unique_words = len(set(tokens)) #Get the total of words without repetitions.
    # Frequencies and Top 5
    freq = count_freq(tokens)
    top_words = top_n(freq)
    if not tableMode:        
        # Вывод результатов
        print(f"Total of words: {total_words}")
        print(f"Total of Unique words: {unique_words}")
        print("Top-5:")
        for word, count in top_words:
            print(f"{word}:{count}")
    else:       
       max_word_len = max(len(word) for word, _ in top_words)
       print(f'{"Word":<{max_word_len}} | Frequency')
       print("-" * (max_word_len + 14))
       for word, count in top_words:
            print(f"{word:<{max_word_len}} | {count}")

if __name__ == "__main__":
    stats()