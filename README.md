# 🏏 IPL Score Predictor

🚀 **Live Demo:** https://ipl-score-predictor-mwzfkvcke36kk87jwjkqyy.streamlit.app
<div align="center">

![IPL Score Predictor Banner](https://img.shields.io/badge/IPL-Score%20Predictor-blue?style=for-the-badge&logo=cricket&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Predict the final score of an IPL innings in real time using Machine Learning** 🎯

</div>

---

## 📌 About The Project

Ever wondered what the final score will be when your team is batting at over 12 with 110 runs and 3 wickets down? This app answers exactly that!

**IPL Score Predictor** uses a **Random Forest Regressor** trained on real IPL ball-by-ball data from 2008–2019 to predict the final innings score based on the current match situation.

---

## ✨ Features

- 🏏 Select any current IPL team as batting or bowling side
- 📊 Input current over, runs scored, and wickets fallen
- 🔮 Get instant final score prediction with a confidence range
- ⚡ Real-time run rate, remaining overs, and runs-per-wicket display
- ⚠️ Smart warnings for batting collapses and low-scoring situations

---

## 🖥️ App Preview

> Select teams → Enter match situation → Click Predict → Get your score!

```
Batting Team:  Mumbai Indians       Bowling Team: Chennai Super Kings
Current Over:  12                   Runs Scored:  95
Wickets Fallen: 3

🔮 Predicted Final Score: 162 runs
📊 Expected Range: 152 - 172 runs

Run Rate: 7.92    Remaining Overs: 8    Runs/Wicket: 23.8
```

---

## 🧠 How It Works

```
📦 Raw IPL Data (1,79,078 ball-by-ball records)
          ↓
🧹 Data Cleaning
   • Keep only 1st innings
   • Remove super overs
   • Remove defunct teams (Deccan Chargers, Kochi Tuskers etc.)
          ↓
⚙️ Feature Engineering
   • Cumulative runs & wickets per over
   • Current run rate
   • Remaining overs
   • Runs per wicket
          ↓
🤖 Model Training
   • Algorithm: Random Forest Regressor (200 trees)
   • Split: 80% train / 20% test (split by match ID)
   • MAE: ~15 runs
          ↓
🌐 Streamlit Web App
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core language |
| 🐼 Pandas | Data manipulation |
| 🔢 NumPy | Numerical operations |
| 🤖 Scikit-learn | ML model (Random Forest) |
| 🌐 Streamlit | Web app interface |
| 💾 Pickle | Model serialization |

---

## 📁 Project Structure

```
ipl-score-predictor/
│
├── 📓 Untitled-1.ipynb      # Data exploration & model training notebook
├── 🌐 app.py                # Streamlit web application
├── 📋 requirements.txt      # Required libraries
├── 🚫 .gitignore            # Files excluded from Git
└── 📖 README.md             # You are here!
```

> ⚠️ Note: `model.pkl`, `deliveries.csv`, and `matches.csv` are not included due to file size limits. See setup instructions below.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/MANVIS10/ipl-score-predictor.git
cd ipl-score-predictor
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download the dataset
Download `matches.csv` and `deliveries.csv` from:
👉 [IPL Dataset on Kaggle](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set)

Place both files in the project root folder.

### 4️⃣ Train the model
Open `Untitled-1.ipynb` in VS Code or Jupyter and run all cells.
This will generate `model.pkl`, `batting_encoder.pkl`, and `bowling_encoder.pkl`.

### 5️⃣ Run the app
```bash
streamlit run app.py
```

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Random Forest Regressor |
| Trees | 200 estimators |
| R² Score | 0.62 |
| Mean Absolute Error | ~15 runs |
| Training Data | Overs 6–20 only |

> The model predicts from over 6 onwards since early overs have too little information for accurate predictions.

---

## 🏆 Teams Supported

| | | | |
|---|---|---|---|
| 🟠 Sunrisers Hyderabad | 💜 Kolkata Knight Riders | 🔴 Royal Challengers Bangalore | 🔴 Kings XI Punjab |
| 💙 Mumbai Indians | 🟡 Chennai Super Kings | 💗 Rajasthan Royals | 💙 Delhi Capitals |

---

## 📚 Key Learnings

Building this project taught me:
- ✅ Real-world data exploration and cleaning
- ✅ Feature engineering on time-series cricket data
- ✅ Avoiding **data leakage** by splitting on match ID not rows
- ✅ Label encoding for categorical variables
- ✅ Random Forest vs Decision Tree tradeoffs
- ✅ Model serialization with Pickle
- ✅ Building interactive ML apps with Streamlit

---

## 🙋‍♂️ Author

**Manvi Soni**

[![GitHub](https://img.shields.io/badge/GitHub-MANVIS10-181717?style=flat&logo=github)](https://github.com/MANVIS10)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ and lots of 🏏

⭐ Star this repo if you found it helpful!

</div>
