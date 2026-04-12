class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name):
        if not name.strip():
            raise ValueError("Nome do hábito não pode ser vazio")
        self.habits[name] = False

    def complete_habit(self, name):
        if name not in self.habits:
            raise ValueError("Hábito não encontrado")
        self.habits[name] = True

    def list_habits(self):
        return self.habits