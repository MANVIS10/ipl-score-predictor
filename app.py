import streamlit as st
import pickle
import numpy as np

# ── Page config ──────────────────────────────────────────
st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="centered"
)

#  Load saved model and encoder
# This is pickle.load() - opposite of pickle.dump()
# We're loading the trained model from disk back into RAM
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('batting_encoder.pkl', 'rb') as f:
    le_batting = pickle.load(f)

with open('bowling_encoder.pkl', 'rb') as f:
    le_bowling = pickle.load(f)

# ── Team list ─────────────────────────────────────────────
teams = sorted([
    'Sunrisers Hyderabad', 'Kolkata Knight Riders',
    'Royal Challengers Bangalore', 'Kings XI Punjab',
    'Mumbai Indians', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
])

# ── UI ────────────────────────────────────────────────────
st.title("🏏 IPL Score Predictor")
st.markdown("Predict the **final score** of an IPL innings based on current match situation")
st.divider()

# Two columns side by side - this is how you do layouts in Streamlit
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("🏏 Batting Team", teams)

with col2:
    bowling_team = st.selectbox("🎯 Bowling Team", teams)

st.divider()

col3, col4, col5 = st.columns(3)

with col3:
    # slider(label, min, max, default)
    current_over = st.slider("Current Over", 6, 19, 10)

with col4:
    current_runs = st.number_input("Runs Scored", min_value=0, max_value=300, value=80)

with col5:
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=2)

st.divider()

# Predict button 
if st.button("🔮 Predict Final Score", use_container_width=True):

    # Validate - batting and bowling team can't be same
    if batting_team == bowling_team:
        st.error("Batting and Bowling team can't be the same!")
    
    else:
        # Calculate the same features we used during training
        current_run_rate = current_runs / current_over
        remaining_overs = 20 - current_over
        runs_per_wicket = current_runs / (wickets + 1)

        # Encode team names to numbers using saved encoders
        batting_encoded = le_batting.transform([batting_team])[0]
        bowling_encoded = le_bowling.transform([bowling_team])[0]

        # Create input array for model - same order as training features
        input_features = np.array([[
            batting_encoded,
            bowling_encoded,
            current_over,
            current_runs,
            wickets,
            current_run_rate,
            remaining_overs,
            runs_per_wicket
        ]])

        # Make prediction
        predicted_score = model.predict(input_features)[0]

        # Show result
        st.success(f"🏏 Predicted Final Score: **{round(predicted_score)} runs**")

        # Show a range (because no prediction is exact)
        low = round(predicted_score) - 10
        high = round(predicted_score) + 10
        st.info(f"📊 Expected range: **{low} - {high} runs**")

        # Your own addition
        if wickets >= 7:
            st.warning("⚠️ Too many wickets lost! Batting collapse likely.")
        if current_run_rate > 12:
         st.warning("🔥 Scoring at a blazing rate!")
        if remaining_overs <= 4 and current_runs < 100:
            st.error("😬 Very low score with few overs left!")

        # Show match summary
        st.markdown("### 📋 Match Situation")
        c1, c2, c3 = st.columns(3)
        c1.metric("Run Rate", f"{current_run_rate:.2f}")
        c2.metric("Remaining Overs", remaining_overs)
        c3.metric("Runs/Wicket", f"{runs_per_wicket:.1f}")