from app import FitnessApp
from cli import CLI

def main():
    # Cria a instância do aplicativo (que lida com os dados)
    app = FitnessApp()
    
    # Cria a instância da interface CLI, passando o app como parâmetro
    cli = CLI(app)
    
    # Executa o loop do menu (chama o método run() do CLI)
    cli.run()

if __name__ == "__main__":
    main()
