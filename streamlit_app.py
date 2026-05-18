import streamlit as st

from src.habits import HabitTracker
from src.weather import get_weather


tracker = HabitTracker()


st.title("🧠 Habit Tracker")

st.write("Acompanhe seus hábitos diários de forma simples.")


# Clima
try:
    temperature = get_weather()

    st.info(
        f"🌤️ Temperatura atual: {temperature}°C\n\n"
        "💧 Lembre-se de se hidratar hoje!"
    )

except Exception:
    st.warning("Não foi possível obter dados do clima.")


# Adicionar hábito
new_habit = st.text_input("Novo hábito")

if st.button("Adicionar hábito"):
    try:
        tracker.add_habit(new_habit)
        st.success("Hábito adicionado!")

    except ValueError as error:
        st.error(str(error))


# Listar hábitos
st.subheader("📋 Seus hábitos")

habits = tracker.list_habits()

if not habits:
    st.write("Nenhum hábito cadastrado.")

else:
    for habit, done in habits.items():
        status = "✔" if done else "✘"

        st.write(f"{habit}: {status}")