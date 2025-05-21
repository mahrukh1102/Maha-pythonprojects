#Web App Title: Habit Tracker

import streamlit as st
from datetime import date

#  Initialization 
if "habits" not in st.session_state:
    st.session_state.habits = []
if "completed_today" not in st.session_state:
    st.session_state.completed_today = {}
if "last_reset" not in st.session_state:
    st.session_state.last_reset = date.today()
if "mood_today" not in st.session_state:
    st.session_state.mood_today = None

# Daily Reset 
if st.session_state.last_reset != date.today():
    st.session_state.completed_today = {}
    st.session_state.mood_today = None
    st.session_state.last_reset = date.today()

# Page Title
st.title("🧠 Habit + Mood Tracker")

# Sidebar: Add Habit
st.sidebar.header("➕ Add Habit")
new_habit = st.sidebar.text_input("Habit (e.g., Exercise, Meditate)")
if st.sidebar.button("Add Habit"):
    if new_habit.strip():
        if new_habit not in [h["name"] for h in st.session_state.habits]:
            st.session_state.habits.append({"name": new_habit})
            st.success(f"Habit '{new_habit}' added.")
        else:
            st.warning("Habit already exists.")
    else:
        st.warning("Habit name cannot be empty.")

# Sidebar: Select Mood 
st.sidebar.header("🙂 How Are You Feeling Today?")
mood = st.sidebar.radio("Select your mood:", ["😊 Happy", "😐 Neutral", "😞 Sad", "😡 Angry", "😴 Tired"])

if st.sidebar.button("Save Mood"):
    st.session_state.mood_today = mood
    st.sidebar.success("Mood saved for today!")

# Today's Summary 
st.subheader(f"📅 {date.today().strftime('%A, %B %d, %Y')}")
if st.session_state.mood_today:
    st.info(f"🧠 **Today's Mood:** {st.session_state.mood_today}")
else:
    st.warning("Mood not set yet!")

#Habit Checklist 
st.subheader("📋 Daily Habits")

if not st.session_state.habits:
    st.info("No habits yet. Add some in the sidebar.")
else:
    for i, habit in enumerate(st.session_state.habits):
        col1, col2 = st.columns([0.8, 0.2])

        habit_name = habit["name"]
        completed = st.session_state.completed_today.get(habit_name, False)
        col1.checkbox(habit_name, value=completed, key=f"check_{i}",
                      on_change=lambda h=habit_name: st.session_state.completed_today.update({h: not completed}))

        if col2.button("❌", key=f"delete_{i}"):
            st.session_state.habits.pop(i)
            st.session_state.completed_today.pop(habit_name, None)
            st.rerun()


total = len(st.session_state.habits)
done = sum(st.session_state.completed_today.get(h["name"], False) for h in st.session_state.habits)
st.success(f"✅ You completed {done}/{total} habits today.")

#Reset 
if st.button("🔄 Reset Today"):
    st.session_state.completed_today = {}
    st.session_state.mood_today = None
    st.success("Progress and mood reset for today.")


st.markdown("---")
st.caption("🧘‍♀️ Stay consistent, and take care of your mind and body!")
