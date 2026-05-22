from app import FitnessApp
from models import Athlete, Workout
from exceptions import DuplicateItemError, ItemNotFoundError

class CLI:
    def __init__(self, app):
        self.app = app

    def _add_athlete(self):
        try:
            print("\n--- Cadastro de novo atleta ---")
            
            athlete_id = int(input("ID do atleta: "))
            name = input("Nome do atleta: ")
            weight = float(input("Peso (kg): "))
            record = float(input("Recorde: "))

            # Cria o objeto temporário para visualização
            athlete = Athlete(athlete_id, name, weight, record)

            # Mostra os dados digitados (como no JSON)
            print("\n--- Dados a serem adicionados ---")
            print(f"ID: {athlete_id}")
            print(f"Nome: {name}")
            print(f"Peso: {weight} kg")
            print(f"Recorde: {record}")
            print("---")

            # Pergunta de confirmação
            confirm = input("Deseja adicionar este atleta? (s/n): ").strip().lower()

            if confirm == 's':
                self.app.add_athlete(athlete)
                print("Atleta adicionado com sucesso!\n")
            elif confirm == 'n':
                print("Operação cancelada. Atleta não foi adicionado.\n")
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.\n")

        except ValueError:
            print("Erro: Por favor, digite números válidos.\n")
        except DuplicateItemError as e:
            print(f"Erro: {e}\n")

    def _show_all_athletes(self):
        athletes = self.app.get_all_athletes()
        if athletes:
            for athlete in athletes:
                print(athlete)
        else:
            print("Nenhum atleta cadastrado.\n")

    def _find_athlete(self):
        try:
            athlete_id = int(input("ID do atleta a ser procurado: "))
            athlete = self.app.find_athlete(athlete_id)
            print(f"\n{athlete}\n")
        except ValueError:
            print("Erro: ID deve ser um número.\n")
        except ItemNotFoundError as e:
            print(f"Erro: {e}\n")

    def _delete_athlete(self):
        try:
            athlete_id = int(input("ID do atleta a ser removido: "))
            
            # Busca e exibe o atleta antes de deletar (para confirmação)
            athlete = self.app.find_athlete(athlete_id)
            print(f"\nAtleta encontrado:\n{athlete}")
            
            # Pergunta de confirmação
            confirm = input("Deseja remover este atleta? (s/n): ").strip().lower()
            
            if confirm == 's':
                self.app.delete_athlete(athlete_id)
                print("Atleta removido com sucesso!\n")
            elif confirm == 'n':
                print("Operação cancelada. Atleta não foi removido.\n")
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.\n")
                
        except ValueError:
            print("Erro: ID deve ser um número.\n")
        except ItemNotFoundError as e:
            print(f"Erro: {e}\n")

    def _filter_athletes(self):
        try:
            record_threshold = float(input("Recorde mínimo para filtrar: "))
            filtered = self.app.filter_athletes_by_record(record_threshold)
            if filtered:
                for athlete in filtered:
                    print(athlete)
            else:
                print("Nenhum atleta encontrado com recorde superior.\n")
        except ValueError:
            print("Erro: Por favor, digite um número válido.\n")

    def _sort_athletes(self):
        print("Escolha o critério de ordenação:")
        print("1. Por nome")
        print("2. Por peso")
        print("3. Por recorde")
        
        choice = input("Opção: ")
        sorted_athletes = []

        if choice == '1':
            sorted_athletes = self.app.sort_athletes('name')
        elif choice == '2':
            sorted_athletes = self.app.sort_athletes('weight')
        elif choice == '3':
            sorted_athletes = self.app.sort_athletes('record')
        else:
            print("Opção inválida.\n")
            return

        if sorted_athletes:
            for athlete in sorted_athletes:
                print(athlete)
        else:
            print("Nenhum atleta para ordenar.\n")

    def run(self):
        while True:
            print("\n=== GERENCIADOR DE ATHLETES ===")
            print("1. Adicionar atleta")
            print("2. Exibir todos os atletas")
            print("3. Procurar atleta por ID")
            print("4. Remover atleta")
            print("5. Filtrar atletas por recorde")
            print("6. Ordenar atletas")
            print("0. Sair")

            choice = input("\nEscolha uma opção: ").strip()

            if choice == '1':
                self._add_athlete()
            elif choice == '2':
                self._show_all_athletes()
            elif choice == '3':
                self._find_athlete()
            elif choice == '4':
                self._delete_athlete()
            elif choice == '5':
                self._filter_athletes()
            elif choice == '6':
                self._sort_athletes()
            elif choice == '0':
                print("Encerrando o programa. Até logo!\n")
                break
            else:
                print("Opção inválida. Tente novamente.\n")
