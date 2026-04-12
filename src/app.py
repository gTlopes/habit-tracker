from habits import HabitTracker

tracker = HabitTracker()

def menu():
    while True:
        print("\n===== HABIT TRACKER =====")
        print("1 - Adicionar hábito")
        print("2 - Concluir hábito")
        print("3 - Listar hábitos")
        print("4 - Remover hábito")
        print("5 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Digite o nome do hábito: ")
            try:
                tracker.add_habit(name)
                print("Hábito adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif choice == "2":
            name = input("Qual hábito deseja concluir: ")
            try:
                tracker.complete_habit(name)
                print("Hábito concluído!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif choice == "3":
            habits = tracker.list_habits()
            if not habits:
                print("Nenhum hábito cadastrado.")
            else:
                print("\nSeus hábitos:")
                for habit, done in habits.items():
                    status = "✔" if done else "✘"
                    print(f"- {habit}: {status}")

        elif choice == "4":
            name = input("Qual hábito deseja remover: ")
            try:
                tracker.remove_habit(name)
                print("Hábito removido!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif choice == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()