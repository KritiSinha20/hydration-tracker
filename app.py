import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Hydration Tracker", layout="centered")

st.title("💧 Kriti's Daily Hydration Tracker")

# Set daily goal
weight_kg = 45
hydration_goal_liters = round(weight_kg * 0.04, 2)  # approx 40ml per kg

st.subheader(f"Today's Goal: {hydration_goal_liters} L")

# Initialize session state
if "water_intake" not in st.session_state:
    st.session_state.water_intake = 0.0

# Add water intake
add_amount = st.number_input("Add water (in L)", min_value=0.1, max_value=1.0, step=0.1)
if st.button("+ Add"):
    st.session_state.water_intake += add_amount

# Display progress
progress = min(st.session_state.water_intake / hydration_goal_liters, 1.0)
st.progress(progress, text=f"You've had {st.session_state.water_intake:.2f} / {hydration_goal_liters} L")

# Log entry
st.write("---")
st.caption(f"Updated at: {datetime.now().strftime('%I:%M %p %d %b %Y')}")

if st.button("Reset"):
    st.session_state.water_intake = 0.0

"Added hydration tracker Streamlit app"
