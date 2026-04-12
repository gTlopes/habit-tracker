import json
import os

class HabitTracker:
    def __init__(self, file_path="habits.json"):
        self.file_path = file_path
        self.habits = self.load_habits()

    def load_habits(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save_habits(self):
        with open(self.file_path, "w") as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, name):
        if not name.strip():
            raise ValueError("Nome do hábito não pode ser vazio")
        self.habits[name] = False
        self.save_habits()

    def complete_habit(self, name):
        if name not in self.habits:
            raise ValueError("Hábito não encontrado")
        self.habits[name] = True
        self.save_habits()

    def remove_habit(self, name):
        if name not in self.habits:
            raise ValueError("Hábito não encontrado")
        del self.habits[name]
        self.save_habits()

    def list_habits(self):
        return self.habits