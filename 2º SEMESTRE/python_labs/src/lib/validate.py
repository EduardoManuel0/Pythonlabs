"""
Модуль валидации для класса Atleta
Содержит все функции валидации, отделенные от бизнес-логики
"""

import re

class ValidationError(Exception):
    """Исключение для ошибок валидации"""
    pass

# ========== VALIDAÇÕES DE TIPO ==========

def validate_type(value, expected_type, field_name):
    """
    Valida se o valor é do tipo esperado
    
    Args:
        value: Valor a ser validado
        expected_type: Tipo esperado (type ou tuple de tipos)
        field_name: Nome do campo para mensagem de erro
    
    Raises:
        ValidationError: Se o tipo não corresponder
    """
    if not isinstance(value, expected_type):
        raise ValidationError(
            f"{field_name} должен быть типа {expected_type.__name__}, "
            f"получен {type(value).__name__}"
        )

# ========== VALIDAÇÕES ESPECÍFICAS ==========

def validate_nome(nome):
    """
    Valida o nome do atleta
    
    Regras:
    - Deve ser string
    - Não pode ser vazio
    - Mínimo 3 caracteres
    - Apenas letras e espaços
    """
    validate_type(nome, str, "name")
    
    nome_stripped = nome.strip()
    
    if not nome_stripped:
        raise ValidationError("Имя не может быть пустым")
    
    if len(nome_stripped) < 3:
        raise ValidationError("Имя должно содержать минимум 3 символа")
    
    # Permite letras, espaços, apóstrofos e hífens para nomes compostos
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]+$", nome_stripped):
        raise ValidationError(
            "Имя должно содержать только буквы, пробелы, апострофы или дефисы"
        )
    
    return nome_stripped


def validate_idade(idade):
    """
    Valida a idade do atleta
    
    Regras:
    - Deve ser inteiro
    - Entre 1 e 120 anos
    """
    validate_type(idade, int, "age")
    
    if idade <= 0:
        raise ValidationError("Возраст должен быть больше нуля")
    
    if idade > 120:
        raise ValidationError("Возраст не может быть больше 120 лет")
    
    return idade


def validate_peso(peso):
    """
    Valida o peso do atleta
    
    Regras:
    - Deve ser número (int ou float)
    - Maior que zero
    - Máximo 300kg
    """
    validate_type(peso, (int, float), "Вес")
    
    if peso <= 0:
        raise ValidationError("Вес должен быть больше нуля")
    
    if peso > 300:
        raise ValidationError("Вес не может быть больше 300 кг")
    
    # Arredonda para 2 casas decimais se for float
    return round(peso, 2) if isinstance(peso, float) else float(peso)


def validate_altura(altura):
    """
    Valida a altura do atleta
    
    Regras:
    - Deve ser número (int ou float)
    - Entre 0.5 e 2.5 metros
    """
    validate_type(altura, (int, float), "Рост")
    
    if altura <= 0:
        raise ValidationError("Рост должен быть больше нуля")
    
    if altura < 0.5:
        raise ValidationError("Рост не может быть меньше 0.5 м")
    
    if altura > 2.5:
        raise ValidationError("Рост не может быть больше 2.5 м")
    
    return round(altura, 2)


def validate_esporte(tipo_desporto):
    """
    Valida o esporte do atleta
    
    Regras:
    - Deve ser string
    - Não pode ser vazio
    - Deve estar na lista de esportes permitidos
    """
    validate_type(tipo_desporto, str, "Вид спорта")
    
    esporte_stripped = tipo_desporto.strip().lower()
    
    if not esporte_stripped:
        raise ValidationError("Вид спорта не может быть пустым")
    
    esportes_validos = [
        'natacao', 'atletismo', 'ginastica', 'futebol', 
        'basquete', 'volei', 'tenis', 'judô', 'jiu-jitsu',
        'boxe', 'ciclismo', 'surf', 'skate'
    ]
    
    # Remove duplicata de 'natacao' se houver
    esportes_validos = sorted(list(set(esportes_validos)))
    
    if esporte_stripped not in esportes_validos:
        raise ValidationError(
            f"Вид спорта должен быть одним из: {', '.join(esportes_validos)}"
        )
    
    return esporte_stripped


def validate_minutos_atividade(minutos):
    """
    Valida os minutos de atividade
    
    Regras:
    - Deve ser número
    - Maior que zero
    """
    validate_type(minutos, (int, float), "Минуты активности")
    
    if minutos <= 0:
        raise ValidationError("Минуты активности должны быть больше нуля")
    
    return float(minutos)


def validate_intensidade(intensidade):
    """
    Valida a intensidade do treino
    
    Regras:
    - Deve ser string
    - Deve ser 'leve', 'moderada' ou 'intensa'
    """
    validate_type(intensidade, str, "Интенсивность")
    
    intensidade_lower = intensidade.lower()
    intensidades_validas = ['leve', 'moderada', 'intensa']
    
    if intensidade_lower not in intensidades_validas:
        raise ValidationError(
            f"Интенсивность должна быть одной из: {', '.join(intensidades_validas)}"
        )
    
    return intensidade_lower


def validate_pontos(pontuacao):
    """
    Valida pontuação de desempenho
    
    Regras:
    - Deve ser número
    - Não pode ser negativo
    """
    validate_type(pontuacao, (int, float), "Очки")
    
    if pontuacao < 0:
        raise ValidationError("Очки не могут быть отрицательными")
    
    return float(pontuacao)


def validate_distancia(dist):
    """
    Valida distância em km
    
    Regras:
    - Deve ser número
    - Maior que zero
    """
    validate_type(dist, (int, float), "Расстояние")
    
    if dist <= 0:
        raise ValidationError("Расстояние должно быть больше нуля")
    
    return float(dist)


def validate_tempo(tmp):
    """
    Valida tempo em minutos
    
    Regras:
    - Deve ser número
    - Maior que zero
    """
    validate_type(tmp, (int, float), "Время")
    
    if tmp <= 0:
        raise ValidationError("Время должно быть больше нуля")
    
    return float(tmp)


# ========== VALIDAÇÕES COMBINADAS ==========

def validate_atleta_data(nome, idade, peso, altura, tipo_desporto):
    """
    Valida todos os dados do atleta de uma vez
    
    Returns:
        tuple: Dados validados e normalizados
    """
    nome_validado = validate_nome(nome)
    idade_validada = validate_idade(idade)
    peso_validado = validate_peso(peso)
    altura_validada = validate_altura(altura)
    esporte_validado = validate_esporte(tipo_desporto)
    
    return (nome_validado, idade_validada, peso_validado, 
            altura_validada, esporte_validado)


def validate_treino_data(minutos, intensidade):
    """
    Valida dados de treino
    
    Returns:
        tuple: Dados validados
    """
    minutos_validados = validate_minutos_atividade(minutos)
    intensidade_validada = validate_intensidade(intensidade)
    
    return (minutos_validados, intensidade_validada)


def validate_desempenho_data(pontuacao):
    """
    Valida dados de desempenho
    
    Returns:
        float: Pontos validados
    """
    return validate_pontos(pontuacao)


def validate_ritmo_data(dist, tmp):
    """
    Valida dados para cálculo de ritmo
    
    Returns:
        tuple: Distância e tempo validados
    """
    distancia_validada = validate_distancia(dist)
    tempo_validado = validate_tempo(tmp)
    
    return (distancia_validada, tempo_validado)