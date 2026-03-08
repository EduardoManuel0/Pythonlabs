```python
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

def validate_nome(имя):
    """
    Valida o nome do atleta
    
    Regras:
    - Deve ser string
    - Não pode ser vazio
    - Mínimo 3 caracteres
    - Apenas letras e espaços
    """
    validate_type(имя, str, "Имя")
    
    nome_stripped = имя.strip()
    
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


def validate_idade(возраст):
    """
    Valida a idade do atleta
    
    Regras:
    - Deve ser inteiro
    - Entre 1 e 120 anos
    """
    validate_type(возраст, int, "Возраст")
    
    if возраст <= 0:
        raise ValidationError("Возраст должен быть больше нуля")
    
    if возраст > 120:
        raise ValidationError("Возраст не может быть больше 120 лет")
    
    return возраст


def validate_peso(вес):
    """
    Valida o peso do atleta
    
    Regras:
    - Deve ser número (int ou float)
    - Maior que zero
    - Máximo 300kg
    """
    validate_type(вес, (int, float), "Вес")
    
    if вес <= 0:
        raise ValidationError("Вес должен быть больше нуля")
    
    if вес > 300:
        raise ValidationError("Вес не может быть больше 300 кг")
    
    # Arredonda para 2 casas decimais se for float
    return round(вес, 2) if isinstance(вес, float) else float(вес)


def validate_altura(рост):
    """
    Valida a altura do atleta
    
    Regras:
    - Deve ser número (int ou float)
    - Entre 0.5 e 2.5 metros
    """
    validate_type(рост, (int, float), "Рост")
    
    if рост <= 0:
        raise ValidationError("Рост должен быть больше нуля")
    
    if рост < 0.5:
        raise ValidationError("Рост не может быть меньше 0.5 м")
    
    if рост > 2.5:
        raise ValidationError("Рост не может быть больше 2.5 м")
    
    return round(рост, 2)


def validate_esporte(вид_спорта):
    """
    Valida o esporte do atleta
    
    Regras:
    - Deve ser string
    - Não pode ser vazio
    - Deve estar na lista de esportes permitidos
    """
    validate_type(вид_спорта, str, "Вид спорта")
    
    esporte_stripped = вид_спорта.strip().lower()
    
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


def validate_minutos_atividade(минуты):
    """
    Valida os minutos de atividade
    
    Regras:
    - Deve ser número
    - Maior que zero
    """
    validate_type(минуты, (int, float), "Минуты активности")
    
    if минуты <= 0:
        raise ValidationError("Минуты активности должны быть больше нуля")
    
    return float(минуты)


def validate_intensidade(интенсивность):
    """
    Valida a intensidade do treino
    
    Regras:
    - Deve ser string
    - Deve ser 'leve', 'moderada' ou 'intensa'
    """
    validate_type(интенсивность, str, "Интенсивность")
    
    intensidade_lower = интенсивность.lower()
    intensidades_validas = ['leve', 'moderada', 'intensa']
    
    if intensidade_lower not in intensidades_validas:
        raise ValidationError(
            f"Интенсивность должна быть одной из: {', '.join(intensidades_validas)}"
        )
    
    return intensidade_lower


def validate_pontos(очки):
    """
    Valida pontuação de desempenho
    
    Regras:
    - Deve ser número
    - Não pode ser negativo
    """
    validate_type(очки, (int, float), "Очки")
    
    if очки < 0:
        raise ValidationError("Очки не могут быть отрицательными")
    
    return float(очки)


def validate_distancia(расстояние):
    """
    Valida distância em km
    
    Regras:
    - Deve ser número
    - Maior que zero
    """
    validate_type(расстояние, (int, float), "Расстояние")
    
    if расстояние <= 0:
        raise ValidationError("Расстояние должно быть больше нуля")
    
    return float(расстояние)


def validate_tempo(время):
    """
    Valida tempo em minutos
    
    Regras:
    - Deve ser número
    - Maior que zero
    """
    validate_type(время, (int, float), "Время")
    
    if время <= 0:
        raise ValidationError("Время должно быть больше нуля")
    
    return float(время)


# ========== VALIDAÇÕES COMBINADAS ==========

def validate_atleta_data(имя, возраст, вес, рост, вид_спорта):
    """
    Valida todos os dados do atleta de uma vez
    
    Returns:
        tuple: Dados validados e normalizados
    """
    nome_validado = validate_nome(имя)
    idade_validada = validate_idade(возраст)
    peso_validado = validate_peso(вес)
    altura_validada = validate_altura(рост)
    esporte_validado = validate_esporte(вид_спорта)
    
    return (nome_validado, idade_validada, peso_validado, 
            altura_validada, esporte_validado)


def validate_treino_data(минуты, интенсивность):
    """
    Valida dados de treino
    
    Returns:
        tuple: Dados validados
    """
    minutos_validados = validate_minutos_atividade(минуты)
    intensidade_validada = validate_intensidade(интенсивность)
    
    return (minutos_validados, intensidade_validada)


def validate_desempenho_data(очки):
    """
    Valida dados de desempenho
    
    Returns:
        float: Pontos validados
    """
    return validate_pontos(очки)


def validate_ritmo_data(расстояние, время):
    """
    Valida dados para cálculo de ritmo
    
    Returns:
        tuple: Distância e tempo validados
    """
    distancia_validada = validate_distancia(расстояние)
    tempo_validado = validate_tempo(время)
    
    return (distancia_validada, tempo_validado)
```