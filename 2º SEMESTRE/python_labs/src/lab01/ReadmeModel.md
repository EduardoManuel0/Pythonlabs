```python
"""
Модель для управления спортсменами - Lab01
Вариант: Фитнес/Спорт
"""

from validate import *


class Atleta:
    """
    Classe que representa um atleta com todos os requisitos do laboratório:
    - Atributos privados
    - Propriedades (@property)
    - Validação de dados (via módulo validate.py)
    - Métodos mágicos
    - Métodos de negócio
    - Atributos de classe
    - Estado lógico
    """
    
    # Atributo de classe - Categorias de peso
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
    
    def __init__(self, имя: str, возраст: int, вес: float, рост: float, вид_спорта: str):
        """
        Construtor com validação de dados via módulo validate.
        """
        # Validação completa usando o módulo validate
        nome_val, idade_val, peso_val, altura_val, esporte_val = validate_atleta_data(
            имя, возраст, вес, рост, вид_спорта
        )
        
        # Atributos privados
        self._nome = nome_val
        self._idade = idade_val
        self._peso = peso_val
        self._altura = altura_val
        self._esporte = esporte_val
        self._ativo = True  # Estado lógico
        self._registro = f"ATL-{Atleta.всего_спортсменов + 1:04d}"
        self._nivel = "Новичок"  # Nível do atleta
        
        # Incrementa contador de atletas
        Atleta.всего_спортсменов += 1
    
    # ========== PROPRIEDADES (@property) ==========
    
    @property
    def nome(self):
        """Getter para nome"""
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        """Setter com validação via módulo validate"""
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._nome = validate_nome(novo_nome)
    
    @property
    def idade(self):
        """Getter para idade"""
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        """Setter com validação via módulo validate"""
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._idade = validate_idade(nova_idade)
    
    @property
    def peso(self):
        """Getter para peso"""
        return self._peso
    
    @peso.setter
    def peso(self, novo_peso):
        """Setter com validação via módulo validate"""
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._peso = validate_peso(novo_peso)
    
    @property
    def altura(self):
        """Getter para altura"""
        return self._altura
    
    @altura.setter
    def altura(self, nova_altura):
        """Setter com validação via módulo validate"""
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._altura = validate_altura(nova_altura)
    
    @property
    def esporte(self):
        """Getter para esporte"""
        return self._esporte
    
    @esporte.setter
    def esporte(self, novo_esporte):
        """Setter com validação via módulo validate"""
        if not self._ativo:
            raise ValueError("Невозможно изменить данные неактивного спортсмена")
        self._esporte = validate_esporte(novo_esporte)
    
    @property
    def ativo(self):
        """Getter para estado ativo"""
        return self._ativo
    
    @property
    def registro(self):
        """Getter para registro (read-only)"""
        return self._registro
    
    @property
    def nivel(self):
        """Getter para nível"""
        return self._nivel
    
    # ========== PROPRIEDADES COMPUTADAS ==========
    
    @property
    def imc(self):
        """Calcula o Índice de Massa Corporal"""
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно рассчитать ИМТ")
        return round(self._peso / (self._altura ** 2), 2)
    
    @property
    def categoria_peso(self):
        """Determina a categoria de peso do atleta"""
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно определить категорию")
        
        for categoria, (min_peso, max_peso) in Atleta.categoria_pesos.items():
            if min_peso < self._peso <= max_peso:
                return categoria.replace('_', ' ').title()
        return "Категория не определена"
    
    @property
    def imc_classificacao(self):
        """Classificação do IMC segundo OMS"""
        imc_val = self.imc
        if imc_val < 18.5:
            return "Недостаточный вес"
        elif imc_val < 25:
            return "Нормальный вес"
        elif imc_val < 30:
            return "Избыточный вес"
        elif imc_val < 35:
            return "Ожирение I степени"
        elif imc_val < 40:
            return "Ожирение II степени"
        else:
            return "Ожирение III степени"
    
    # ========== MÉTODOS DE ESTADO ==========
    
    def ativar(self):
        """Ativa o atleta"""
        self._ativo = True
        print(f"✅ Спортсмен {self._nome} успешно активирован.")
    
    def desativar(self):
        """Desativa o atleta"""
        self._ativo = False
        print(f"⏸️  Спортсмен {self._nome} успешно деактивирован.")
    
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
        """
        Calcula a energia gasta em uma atividade (método de negócio 1)
        
        Args:
            minutos_atividade: Duração em minutos
            intensidade: 'легкая', 'умеренная' ou 'интенсивная'
        
        Returns:
            float: Energia gasta em kcal
        """
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно рассчитать энергию")
        
        # Validações usando módulo validate
        minutos_val = validate_minutos_atividade(minutos_atividade)
        intensidade_val = validate_intensidade(intensidade)
        
        # Mapeamento para os fatores em russo
        mapa_intensidade = {
            'leve': 'легкая',
            'moderada': 'умеренная',
            'intensa': 'интенсивная'
        }
        
        # Cálculo: energia = peso * minutos * fator_intensidade
        fator = Atleta.коэффициенты_интенсивности[mapa_intensidade[intensidade_val]]
        energia = self._peso * minutos_val * fator
        
        return round(energia, 2)
    
    def classificar_desempenho(self, pontos: float):
        """
        Classifica o desempenho do atleta (método de negócio 2)
        
        Args:
            pontos: Pontuação obtida (0-100)
        
        Returns:
            str: Classificação do desempenho
        """
        if not self._ativo:
            raise ValueError("Спортсмен неактивен - невозможно классифицировать")
        
        pontos_val = validate_pontos(pontos)
        
        if pontos_val < 50:
            return "❌ Нужно улучшать"
        elif pontos_val < 70:
            return "👍 Средний результат"
        elif pontos_val < 90:
            return "🌟 Хороший результат"
        else:
            return "🏆 Отличный результат"
    
    def calcular_ritmo(self, distancia_km: float, tempo_minutos: float):
        """
        Calcula o ritmo médio (min/km) - método de negócio extra
        
        Args:
            distancia_km: Distância em quilômetros
            tempo_minutos: Tempo em minutos
        """
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
        estado = "🟢 Активен" if self._ativo else "🔴 Неактивен"
        
        # Mapeamento das categorias de peso para exibição em russo
        mapa_categorias = {
            'Peso Mosca': 'Наилегчайший вес',
            'Peso Galo': 'Легчайший вес',
            'Peso Pena': 'Полулегкий вес',
            'Peso Leve': 'Легкий вес',
            'Peso Medio': 'Средний вес',
            'Peso Pesado': 'Тяжелый вес',
            'Peso Super Pesado': 'Супертяжелый вес'
        }
        
        categoria_exibicao = self.categoria_peso
        for pt, ru in mapa_categorias.items():
            if pt in categoria_exibicao:
                categoria_exibicao = ru
                break
        
        return (f"\n{'='*50}\n"
                f"🏃 СПОРТСМЕН: {self._nome}\n"
                f"{'='*50}\n"
                f"📋 Регистрация: {self._registro}\n"
                f"🎯 Вид спорта:  {self._esporte.title()}\n"
                f"📊 Возраст:     {self._idade} лет\n"
                f"⚖️  Вес:         {self._peso:.1f} кг\n"
                f"📏 Рост:        {self._altura:.2f} м\n"
                f"📈 ИМТ:         {self.imc:.2f} ({self.imc_classificacao})\n"
                f"🏆 Категория:   {categoria_exibicao}\n"
                f"⭐ Уровень:     {self._nivel}\n"
                f"⚡ Состояние:   {estado}\n"
                f"{'='*50}")
    
    def __repr__(self):
        """Representação técnica do objeto"""
        return (f"Atleta(имя='{self._nome}', возраст={self._idade}, "
                f"вес={self._peso:.1f}, рост={self._altura:.2f}, "
                f"вид_спорта='{self._esporte}', активен={self._ativo})")
    
    def __eq__(self, other):
        """Comparação de igualdade entre atletas"""
        if not isinstance(other, Atleta):
            return False
        return (self._registro == other._registro)
    
    def __lt__(self, other):
        """Comparação para ordenação (por IMC)"""
        if not isinstance(other, Atleta):
            return NotImplemented
        return self.imc < other.imc
    
    def __hash__(self):
        """Hash para uso em dicionários/sets"""
        return hash(self._registro)
```