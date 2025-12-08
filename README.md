# Growth_Project
Growth_Project is a data-driven application focused on monitoring child growth and providing personalized nutrition suggestions. The project analyzes key child growth parameters—such as age, weight, height, BMI, and activity level—to recommend suitable foods along with required daily calorie intake.
# 🌱 AI-Powered Child Growth Optimizer

> **Project Status:** 🚧 Active Development
> **Role:** Collaborative AI & Web App Project
> **Goal:** Optimize child nutrition using ML-based health tracking.

## 📋 Project Overview
This tool helps parents track their child's growth and get personalized diet plans.
* **Backend:** A Random Forest Classifier (trained on 300+ samples) predicts health status.
* **Frontend:** A Streamlit web dashboard for user interaction and visualization.

---

## 👨‍💻 Developer Guide (For Streamlit / Frontend)

If you are working on `app.py` or the UI, please read this section carefully to ensure the interface connects correctly with the Machine Learning model.

### 1. Model Integration Logic
The model (`child_growth_model.pkl`) is strict about input formats.

* **Model Input Expectation:** `[Age, Gender, Height, Weight]`
* **⚠️ Critical Handling for Gender:**
    * The User sees: "Male" or "Female" (Radio Button).
    * The Model needs: `0` or `1`.
    * **Logic to implement in Streamlit:**
        ```python
        # In app.py
        gender_input = st.radio("Select Gender", ["Male", "Female"])
        gender_numeric = 0 if gender_input == "Male" else 1
        ```

### 2. Output & Diet Plan Mapping
The model does **not** output the diet text directly. It outputs a **Label**. You need to map this label to the correct text dictionary in the Streamlit code.

* **Model Output:** Returns a list containing one string: `['Underweight']` or `['Healthy']` or `['Overweight']`.
* **UI Logic:**
    * Use the output string as a **Key** to fetch details from the `diet_plans` dictionary.
    * *Do not hardcode specific if/else statements for text; use the dictionary structure for cleaner code.*

### 3. Visualizations
The repo includes `matplotlib` and `seaborn`.
* **Growth Chart:** The frontend is responsible for generating the reference line (Standard Growth) vs. the user's point (Input Data).
* *Tip:* Use `st.pyplot(fig)` to render the charts.

---
