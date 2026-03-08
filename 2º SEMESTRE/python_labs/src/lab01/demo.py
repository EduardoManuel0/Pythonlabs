"""
Демонстрация класса Atleta - Lab01
С импортами с использованием структуры пакетов
"""

from model import *
import sys
import os


def cabecalho(titulo):
    """Imprime um cabeçalho formatado"""
    print("\n" + "="*70)
    print(f" {titulo}")
    print("="*70)


def demonstrar_criacao_objetos():
    """Demonstra a criação de objetos Atleta"""
    cabecalho("ДЕМОНСТРАЦИЯ 1: СОЗДАНИЕ ОБЪЕКТОВ")
    
    try:
        # Criação válida
        atleta1 = Atleta("João Silva", 25, 75.5, 1.80, "natacao")
        atleta2 = Atleta("Maria Santos", 22, 62.3, 1.68, "atletismo")
        
        print("✅ Спортсмены успешно созданы!")
        print(atleta1)
        print(atleta2)
        
        # Demonstração de __repr__
        print("\n🔍 Техническое представление (__repr__):")
        print(repr(atleta1))
        
    except ValidationError as e:
        print(f"❌ Ошибка валидации: {e}")
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")


def demonstrar_validacoes():
    """Demonstra as validações do módulo validate.py"""
    cabecalho("ДЕМОНСТРАЦИЯ 2: ВАЛИДАЦИИ (validate.py)")
    
    casos_teste = [
        ("Пустое имя", "имя", "", 25, 75.5, 1.80, "natacao"),
        ("Короткое имя", "имя", "Jo", 25, 75.5, 1.80, "natacao"),
        ("Имя с цифрами", "имя", "João123", 25, 75.5, 1.80, "natacao"),
        ("Отрицательный возраст", "возраст", "João", -5, 75.5, 1.80, "natacao"),
        ("Возраст > 120", "возраст", "João", 150, 75.5, 1.80, "natacao"),
        ("Нулевой вес", "вес", "João", 25, 0, 1.80, "natacao"),
        ("Вес > 300", "вес", "João", 25, 350, 1.80, "natacao"),
        ("Рост < 0.5", "рост", "João", 25, 75.5, 0.3, "natacao"),
        ("Рост > 2.5", "рост", "João", 25, 75.5, 3.0, "natacao"),
        ("Неверный вид спорта", "вид спорта", "João", 25, 75.5, 1.80, "xadrez"),
    ]
    
    for desc, campo, nome, idade, peso, altura, esporte in casos_teste:
        try:
            print(f"\n▶️  Тестирование: {desc}")
            Atleta(nome, idade, peso, altura, esporte)
            print(f"  ❌ ОШИБКА: {campo} должно было быть отклонено!")
        except ValidationError as e:
            print(f"  ✅ Валидация верна: {e}")
        except Exception as e:
            print(f"  ❌ Неожиданная ошибка: {e}")


def demonstrar_propriedades_setters():
    """Demonstra propriedades e setters com validação"""
    cabecalho("ДЕМОНСТРАЦИЯ 3: СВОЙСТВА И СЕТТЕРЫ")
    
    atleta = Atleta("João Silva", 25, 75.5, 1.80, "natacao")
    print("📝 Начальный спортсмен:")
    print(atleta)
    
    print("\n🔄 Изменение свойств через сеттеры:")
    
    try:
        atleta.peso = 78.3
        atleta.altura = 1.82
        atleta.esporte = "futebol"
        
        print("✅ Изменения успешно выполнены!")
        print(f"  Новый вес: {atleta.peso} кг")
        print(f"  Новый рост: {atleta.altura} м")
        print(f"  Новый вид спорта: {atleta.esporte}")
        
        # Teste de validação no setter
        print("\n🔒 Тестирование сеттера с неверным значением:")
        atleta.peso = -10
    except ValidationError as e:
        print(f"  ✅ Сеттер верно отклонил: {e}")
    except ValueError as e:
        print(f"  ✅ Ошибка состояния: {e}")


def demonstrar_atributos_classe():
    """Demonstra atributos de classe"""
    cabecalho("ДЕМОНСТРАЦИЯ 4: АТРИБУТЫ КЛАССА")
    
    print(f"📊 Всего спортсменов: {Atleta.всего_спортсменов}")
    
    # Criar mais alguns atletas
    atleta1 = Atleta("João", 25, 75.5, 1.80, "natacao")
    atleta2 = Atleta("Maria", 22, 62.3, 1.68, "atletismo")
    atleta3 = Atleta("Pedro", 28, 85.0, 1.85, "basquete")
    
    print(f"📊 После создания 3 спортсменов: {Atleta.всего_спортсменов}")
    
    print("\n🏋️  Доступные весовые категории:")
    # Tradução das categorias para exibição
    mapa_categorias_ru = {
        'наилегчайший_вес': 'Наилегчайший вес',
        'легчайший_вес': 'Легчайший вес',
        'полулегкий_вес': 'Полулегкий вес',
        'легкий_вес': 'Легкий вес',
        'средний_вес': 'Средний вес',
        'тяжелый_вес': 'Тяжелый вес',
        'супертяжелый_вес': 'Супертяжелый вес'
    }
    
    for categoria, (min_peso, max_peso) in Atleta.categoria_pesos.items():
        categoria_ru = mapa_categorias_ru.get(categoria, categoria.replace('_', ' ').title())
        print(f"  - {categoria_ru}: "
              f"{min_peso}кг - {max_peso if max_peso != float('inf') else '∞'}кг")
    
    print("\n🔥 Коэффициенты интенсивности:")
    for intensidade, fator in Atleta.коэффициенты_интенсивности.items():
        print(f"  - {intensidade.title()}: {fator}")


def demonstrar_metodos_negocio():
    """Demonstra os métodos de negócio"""
    cabecalho("ДЕМОНСТРАЦИЯ 5: БИЗНЕС-МЕТОДЫ")
    
    atleta = Atleta("João Silva", 25, 75.5, 1.80, "natacao")
    
    print("📊 Расчет затраченной энергии (30 минут):")
    # Mapa para tradução das intensidades
    mapa_intensidade = {
        'leve': 'легкая',
        'moderada': 'умеренная',
        'intensa': 'интенсивная'
    }
    
    for intensidade in ['leve', 'moderada', 'intensa']:
        energia = atleta.calcular_energia_gasta(30, intensidade)
        intensidade_ru = mapa_intensidade[intensidade]
        print(f"  - {intensidade_ru.title()}: {energia} ккал")
    
    print("\n🏆 Классификация производительности:")
    pontuacoes = [45, 65, 85, 95]
    for pontos in pontuacoes:
        classificacao = atleta.classificar_desempenho(pontos)
        print(f"  - {pontos} очков: {classificacao}")
    
    print("\n⏱️  Расчет темпа:")
    ritmo = atleta.calcular_ritmo(10, 50)  # 10km em 50min
    print(f"  - 10 км за 50 мин: {ritmo} мин/км")


def demonstrar_estado_logico():
    """Demonstra comportamento dependente de estado"""
    cabecalho("ДЕМОНСТРАЦИЯ 6: ЛОГИЧЕСКОЕ СОСТОЯНИЕ")
    
    atleta = Atleta("João Silva", 25, 75.5, 1.80, "natacao")
    
    print("🟢 Начальное состояние (активен):")
    print(f"  ИМТ: {atleta.imc}")
    print(f"  Категория: {atleta.categoria_peso}")
    
    print("\n⏸️  Деактивация спортсмена...")
    atleta.desativar()
    
    print("\n🔴 Попытка операций с неактивным спортсменом:")
    try:
        imc = atleta.imc
    except ValueError as e:
        print(f"  ✅ ИМТ заблокирован: {e}")
    
    try:
        atleta.calcular_energia_gasta(30, 'moderada')
    except ValueError as e:
        print(f"  ✅ Расчет энергии заблокирован: {e}")
    
    try:
        atleta.peso = 80.0
    except ValueError as e:
        print(f"  ✅ Изменение веса заблокировано: {e}")
    
    print("\n🔄 Реактивация спортсмена...")
    atleta.ativar()
    print(f"  ИМТ после реактивации: {atleta.imc}")


def demonstrar_fluxos_trabalho():
    """Demonstra fluxos de trabalho completos"""
    cabecalho("ДЕМОНСТРАЦИЯ 7: РАБОЧИЕ ПРОЦЕССЫ")
    
    # FLUXO 1: Atleta em preparação para competição
    print("🏁 ПРОЦЕСС 1: Подготовка к соревнованиям")
    print("-" * 50)
    
    atleta1 = Atleta("João Silva", 25, 78.5, 1.80, "natacao")
    print(f"Спортсмен: {atleta1.nome}")
    print(f"Начальный вес: {atleta1.peso} кг")
    print(f"Категория: {atleta1.categoria_peso}")
    
    # Treinamento intenso
    print("\n📅 Недели 1-4: Интенсивные тренировки")
    for semana in range(1, 5):
        # Perde 0.5kg por semana
        atleta1.peso = atleta1.peso - 0.5
        energia = atleta1.calcular_energia_gasta(60 * 5, 'intensa')  # 5h/semana
        print(f"  Неделя {semana}: {atleta1.peso} кг, Энергия: {energia} ккал")
    
    print(f"\n✅ Итоговая категория: {atleta1.categoria_peso}")
    
    # FLUXO 2: Mudança de modalidade com validações
    print("\n\n🔄 ПРОЦЕСС 2: Смена вида спорта")
    print("-" * 50)
    
    atleta2 = Atleta("Maria Santos", 22, 62.3, 1.68, "atletismo")
    print(f"Текущий вид спорта: {atleta2.esporte}")
    
    try:
        print("\nПопытка сменить на плавание...")
        atleta2.esporte = "natacao"
        print(f"✅ Новый вид спорта: {atleta2.esporte}")
        
        print("\nПопытка сменить на неверный вид спорта...")
        atleta2.esporte = "xadrez"
    except ValidationError as e:
        print(f"❌ {e}")
    
    # FLUXO 3: Evolução de nível
    print("\n\n📈 ПРОЦЕСС 3: Эволюция уровня")
    print("-" * 50)
    
    atleta3 = Atleta("Pedro Costa", 20, 70.0, 1.75, "jiu-jitsu")
    print(f"Начальный уровень: {atleta3.nivel}")
    
    pontuacoes = [45, 80, 150, 250]
    for i, pontos in enumerate(pontuacoes, 1):
        novo_nivel = atleta3.atualizar_nivel(pontos)
        print(f"  Турнир {i} ({pontos} очков): {novo_nivel}")


def main():
    """Função principal"""
    print("="*70)
    print(" LAB01 - КЛАСС ATLETA (ФИТНЕС/СПОРТ)")
    print("="*70)
    print("\n📁 Структура с отдельным модулем validate.py")
    print("\nВыполнение всех демонстраций...\n")
    
    demonstrar_criacao_objetos()
    demonstrar_validacoes()
    demonstrar_propriedades_setters()
    demonstrar_atributos_classe()
    demonstrar_metodos_negocio()
    demonstrar_estado_logico()
    demonstrar_fluxos_trabalho()
    
    print("\n" + "="*70)
    print("✅ КОНЕЦ ДЕМОНСТРАЦИИ")
    print("="*70)


if __name__ == "__main__":
    main()