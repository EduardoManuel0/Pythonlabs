import pytest

# Importa as funções do seu arquivo text_tools.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.lib.text import normalize, tokenize, count_freq, top_n


# --- Testes para a função normalize ---
@pytest.mark.parametrize(
    "text_in, expected_out, casefold_val, yo2e_val",
    [
        # Caso básico: espaços, quebras de linha e casefold padrão
        ("Olá Mundo\nEste é um teste.  ", "olá mundo este é um teste.", True, True),
        # Caso sem casefold
        ("Olá Mundo", "Olá Mundo", False, True),
        # Caso russo com substituição de 'ё' (padrão)
        ("Пётр Чайковский", "петр чайковский", True, True),
        # Caso russo sem substituição de 'ё'
        ("Пётр Чайковский", "пётр чайковский", True, False),
        # Caso misto complexo
        (
            "  TESTE\tCom\nEspaços\rEspeciais ",
            "teste com espaços especiais",
            True,
            True,
        ),
    ],
)
def test_normalize(text_in, expected_out, casefold_val, yo2e_val):
    """Testa a função normalize com vários parâmetros de entrada."""
    result = normalize(text_in, casefold=casefold_val, yo2e=yo2e_val)
    assert result == expected_out


# --- Testes para a função tokenize ---
@pytest.mark.parametrize(
    "text_in, expected_out",
    [
        # Caso básico: palavras, números e hífens
        (
            "Aqui estão 2 exemplos: teste-hifenizado e mais um.",
            ["aqui", "estão", "2", "exemplos", "teste-hifenizado", "e", "mais", "um"],
        ),
        # Ignorando pontuação
        (
            "O quê? Isso é um teste, certo!",
            ["o", "quê", "isso", "é", "um", "teste", "certo"],
        ),
        # Texto com apenas números e símbolos
        ("123, 456. abc!", ["123", "456", "abc"]),
    ],
)
def test_tokenize(text_in, expected_out):
    """Testa a função tokenize para extração correta de tokens."""
    assert tokenize(text_in) == expected_out


# --- Testes para a função count_freq ---
@pytest.mark.parametrize(
    "tokens_in, expected_out",
    [
        # Caso simples com repetições
        (
            ["gato", "cão", "gato", "peixe", "cão", "gato"],
            {"gato": 3, "cão": 2, "peixe": 1},
        ),
        # Caso sem repetições
        (["a", "b", "c"], {"a": 1, "b": 1, "c": 1}),
        # Caso com lista vazia
        ([], {}),
    ],
)
def test_count_freq(tokens_in, expected_out):
    """Testa a contagem de frequência de diferentes listas de tokens."""
    assert count_freq(tokens_in) == expected_out


# --- Testes para a função top_n ---
@pytest.mark.parametrize(
    "freq_in, n_val, expected_out",
    [
        # Teste padrão (n=5 por default, mas explicitado aqui)
        (
            {"a": 10, "b": 20, "c": 5, "d": 50, "e": 1, "f": 15},
            5,
            [("d", 50), ("b", 20), ("f", 15), ("a", 10), ("c", 5)],
        ),
        # Teste com limite n=2
        (
            {"banana": 5, "maçã": 3, "laranja": 8, "uva": 1},
            2,
            [("laranja", 8), ("banana", 5)],
        ),
        # Teste de desempate (tie-breaking) por ordem alfabética
        (
            {"zebra": 5, "abacate": 5, "bola": 5},
            3,
            [("abacate", 5), ("bola", 5), ("zebra", 5)],
        ),
        # Teste onde n é maior que o número de itens
        ({"um": 1, "dois": 2}, 10, [("dois", 2), ("um", 1)]),
    ],
)
def test_top_n(freq_in, n_val, expected_out):
    """Testa a ordenação e o limite da função top_n."""
    # Nota: A função top_n no seu código original espera o 'n' como argumento posicional agora,
    # então a chamada aqui é top_n(freq_in, n_val).
    assert top_n(freq_in, n=n_val) == expected_out
