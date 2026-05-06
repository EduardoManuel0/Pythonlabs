import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Поднимаем уровень на одну папку вверх
from lib.validate import *
class Atleta:
    """
    Classe que representa um atleta com requisitos básicos:
    - Atributos privados
    - Propriedades (@property)
    - Validação de dados (via módulo validate.py)
    - Métodos mágicos
    - Métodos de negócio
    - Atributos de classe
    - Estado lógico
    """

    # Atributo de classe - Categorias de peso (mantido para possível uso futuro)
    categoria_pesos = {
        'наилегчайший_вес': (0, 52),
        'легчайший_вес': (52, 57),
        'полулегкий_вес': (57, 62),
        'легкий_вес': (62, 70),
        'средний_вес': (70, 85),
        'тяжелый_вес': (85, 105),
        'супертяжелый_вес': (105, float('inf'))
    }

    # Atributo de classe para contador de instâncias
    всего_спортсменов = 0

    # Atributo de classe - Fatores de intensidade para cálculo de energia
    коэффициенты_интенсивности = {
        'легкая': 0.05,
        'умеренная': 0.08,
        'интенсивная': 0.12
    }

    def __init__(self, nome: str, idade: int, peso: float, altura: float, tipo_desporto: str):
        """Construtor com validação de dados via módulo validate."""
        nome_val, idade_val, peso_val, altura_val, esporte_val = validate_atleta_data(
            nome, idade, peso, altura, tipo_desporto
        )

        # Atributos privados
        self._nome = nome_val
        self._idade = idade_val
        self._peso = peso_val
        self._altura = altura_val
        self._esporte = esporte_val
        self._ativo = True  # Состояние активности
        self._registro = f"ATL-{Atleta.всего_спортсменов + 1:04d}"
        self._nivel = "Новичок"  # Уровень спортсмена

        # Увеличиваем счётчик спортсменов
        Atleta.всего_спортсменов += 1

    # ========== PROPRIEDADES (@property) ==========

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._nome = validate_nome(novo_nome)

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._idade = validate_idade(nova_idade)

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, novo_peso):
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._peso = validate_peso(novo_peso)

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, nova_altura):
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._altura = validate_altura(nova_altura)

    @property
    def esporte(self):
        return self._esporte

    @esporte.setter
    def esporte(self, novo_esporte):
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._esporte = validate_esporte(novo_esporte)

    @property
    def ativo(self):
        return self._ativo

    @property
    def registro(self):
        return self._registro

    @property
    def nivel(self):
        return self._nivel

    # ========== MÉTODOS DE ESTADO ==========

    def ativar(self):
        """Ativa o atleta"""
        self._ativo = True
        print(f"Спортсмен {self._nome} успешно активирован.")

    def desativar(self):
        """Desativa o atleta"""
        self._ativo = False
        print(f"Спортсмен {self._nome} успешно деактивирован.")

    def atualizar_nivel(self, pontuacao):
        """Atualiza o nível do atleta baseado na pontuação"""
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно обновить уровень")

        pontuacao_val = validate_pontos(pontuacao)

        if pontuacao_val < 50:
            self._nivel = "Новичок"
        elif pontuacao_val < 100:
            self._nivel = "Средний уровень"
        elif pontuacao_val < 200:
            self._nivel = "Продвинутый"
        else:
            self._nivel = "Элита"

        return self._nivel

    # ========== MÉTODOS DE NEGÓCIO ==========

    def calcular_energia_gasta(self, minutos_atividade: int, intensidade: str = 'умеренная'):
        """Calcula a energia gasta em uma atividade."""
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно рассчитать энергию")

        minutos_val = validate_minutos_atividade(minutos_atividade)
        intensidade_val = validate_intensidade(intensidade)

        mapa_intensidade = {
            'leve': 'легкая',
            'moderada': 'умеренная',
            'intensa': 'интенсивная'
        }

        fator = Atleta.коэффициенты_интенсивности[mapa_intensidade[intensidade_val]]
        energia = self._peso * minutos_val * fator

        return round(energia, 2)

    def classificar_desempenho(self, pontos: float):
        """Classifica o desempenho do atleta."""
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно классифицировать")

        pontos_val = validate_pontos(pontos)

        if pontos_val < 50:
            return "Нужно улучшать"
        elif pontos_val < 70:
            return "Средний результат"
        elif pontos_val < 90:
            return "Хороший результат"
        else:
            return "Отличный результат"

    def calcular_ritmo(self, distancia_km: float, tempo_minutos: float):
        """Calcula o ritmo médio (min/km)."""
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно рассчитать темп")

        if distancia_km <= 0:
            raise ValueError("Расстояние должно быть больше нуля")
        if tempo_minutos <= 0:
            raise ValueError("Время должно быть больше нуля")

        ritmo = tempo_minutos / distancia_km
        return round(ritmo, 2)

    # ========== MÉTODOS MÁGICOS ==========

    def __str__(self):
        """Representação amigável do objeto"""
        estado = "Активен" if self._ativo else "Неактивен"

        return (f"\n{'='*50}\n"
                "СПОРТСМЕН: {self._nome}\n"
                "{'='*50}\n"
                "Регистрация: {self._registro}\n"
                "Вид спорта:  {self._esporte.title()}\n"
                "Возраст:     {self._idade} лет\n"
                "Вес:         {self._peso:.1f} кг\n"
                "Рост:        {self._altura:.2f} м\n"
                )