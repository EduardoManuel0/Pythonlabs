import sys
import os
# Добавляем путь к корневой папке проекта
# Add the path to the project root folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib import text


example_normalize = "  двойные   пробелы  "
example_tokenize = "emoji 😀 не слово"
example_count_freq = ["bb","aa","bb","aa","cc"]

res_normalise = text.normalize(example_normalize)
res_tokenize = text.tokenize(example_tokenize)
res_count_freq = text.count_freq(example_count_freq)
res_count_top_n = text.top_n(res_count_freq)

print(res_normalise)    
print(res_tokenize)
print(res_count_freq)
print(res_count_top_n)