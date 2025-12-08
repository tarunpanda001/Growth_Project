# Growth_Project – Child Growth & Nutrition Optimizer

Live App: **[https://child-growth-optimizer.streamlit.app/](https://child-growth-optimizer.streamlit.app/)**

## 📌 Overview

**Growth_Project** is a web-based application designed to track child growth and recommend personalized nutrition and calorie intake. By taking simple inputs such as age, weight, height, gender, and activity level, the app provides:

* Growth evaluation (BMI, growth category)
* Daily calorie requirement
* Recommended foods & portion sizes
* Nutrient distribution insights

This app helps parents, caregivers, and pediatric nutrition learners make informed decisions about a child's nutrition and growth.

---

## 🛠️ Tech Stack

### **Frontend & App Framework**

* **Streamlit** – Builds the interactive UI and handles user input

### **Backend & Logic**

* **Python** – Core logic for calculations
* **Pandas / NumPy** – Data handling and food/nutrient lookup

### **Visualization**

* **Matplotlib / Seaborn / Streamlit Charts** – For growth and nutrient visualizations

### **Deployment**

* **Streamlit Community Cloud** – For hosting the live app

---

## 🧑‍💻 How to Use the App

1. Open the app: **[https://child-growth-optimizer.streamlit.app/](https://child-growth-optimizer.streamlit.app/)**
2. Enter required child metrics:

   * Age
   * Gender
   * Weight
   * Height
   * Activity level
3. Click **Submit** or **Calculate**.
4. The app will display:

   * Growth status & BMI
   * Recommended daily calorie intake
   * Suggested foods with portion sizes
   * Nutrient breakdown visuals (if present)
5. Update the inputs anytime to get new recommendations.

---

## 📁 Project Structure

```
Growth_Project/
│
├── app.py                  # Main Streamlit app
├── src/
│   ├── growth_calculator.py
│   ├── calorie_engine.py
│   ├── food_recommender.py
│   └── visualizer.py
│
├── data/
│   └── food_nutrition.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── README.md
└── requirements.txt
```

---
## 🔮 Future Enhancements

* AI-based personalized diet planner
* Growth anomaly detection system
* Weekly & monthly food plans
* Mobile app version

---

## 👨‍💻 Author

**Tarun** – Developer of the Child Growth & Nutrition Optimizer

---
