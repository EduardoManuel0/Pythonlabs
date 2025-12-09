import string
import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    s = text
    if casefold:
        s = s.casefold()
    if yo2e:
        s = s.replace("ё", "е").replace("Ё", "Е")
    s = s.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    s = s.strip()
    while "  " in s:
        s = s.replace("  ", " ")
    return s


def tokenize(text: str) -> list[str]:
    # A expressão regular encontra (e coloca-a na variável "default"):
    # 1. Palavras que contêm um hífen (\w+-\w+)
    # 2. Números (\d+)
    # 3. Palavras com padrão de letras/números/sublinhados (\w+)
    default = r"\w+-\w+|\d+|\w+"
    # Encontre todos os caracteres de padrão no texto e devolva apenas estes.
    return re.findall(default, text.lower())


def count_freq(tokens: list[str]) -> dict[str, int]:
    d = {}
    tokens_set = set(tokens)
    for key in tokens_set:
        d[key] = tokens.count(key)
    return d


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    d = freq
    d = sorted(d.items(), key=lambda para: (-para[1], para[0]))
    return d[:n]
