import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Trained Model
model = joblib.load('child_growth_model.pkl')

# Define Diet Plans (Hardcoded based on predictions)
diet_plans = {
    'Underweight': {
        'Calories': '1600 - 1800 kcal (High Calorie)',
        'Focus': 'Protein & Healthy Fats',
        'Breakfast': 'Oatmeal with whole milk, banana, and peanut butter.',
        'Lunch': 'Rice/Roti with Dal (add ghee), potato fry, and yogurt.',
        'Snack': 'Boiled eggs, nuts (almonds/walnuts), or fruit smoothie.',
        'Dinner': 'Paneer butter masala with paratha or Chicken stew.'
    },
    'Healthy': {
        'Calories': '1400 - 1600 kcal (Maintenance)',
        'Focus': 'Balanced Nutrients',
        'Breakfast': 'Idli/Dosa with sambar or Scrambled eggs with toast.',
        'Lunch': 'Rice, mixed vegetable curry, dal, and cucumber salad.',
        'Snack': 'Fruit salad, roasted chana, or milk.',
        'Dinner': 'Roti with mixed veg sabzi or Grilled fish/chicken.'
    },
    'Overweight': {
        'Calories': '1200 - 1400 kcal (Calorie Deficit)',
        'Focus': 'Fiber & Low Sugar',
        'Breakfast': 'Vegetable upma or Whole wheat toast with avocado/egg white.',
        'Lunch': 'Brown rice/Roti, spinach dal, and lots of green salad.',
        'Snack': 'Carrot sticks, apple slices, or buttermilk (no sugar).',
        'Dinner': 'Lentil soup (Dal) with veggies, no heavy cream/butter.'
    }
}

# 2. Setup the Streamlit Page
st.set_page_config(page_title="Growth Optimizer", layout="wide")

st.title("🌱 AI-Powered Child Growth Optimizer")
st.markdown("### Personalized Diet Recommendation for Real-time Health Management")
st.write("Enter your child's details below to get a customized nutrition plan.")

# 3. Sidebar Inputs
st.sidebar.header("Child's Details")
age = st.sidebar.slider("Age (Years)", 2, 10, 5)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", 70.0, 150.0, 100.0)
weight = st.sidebar.number_input("Weight (kg)", 10.0, 60.0, 15.0)

# Remember: We trained with Male=0, Female=1
gender_numeric = 0 if gender == "Male" else 1

# 4. Prediction Button
if st.button("Analyze & Generate Diet Plan"):
    
    # Create a dataframe for the model input (must match training columns)
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender_numeric],
        'Height (cm)': [height],
        'Weight (kg)': [weight]
    })
    
    # Calculate BMI
    bmi = round(weight / ((height/100) ** 2), 1)
    
    # Make Prediction
    prediction = model.predict(input_data)[0]
    
    # Display Results in Columns
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Health Snapshot")
        st.metric(label="BMI Score", value=bmi)
        
        # Dynamic Color for Status
        if prediction == "Healthy":
            st.success(f"**Status: {prediction}**")
        elif prediction == "Underweight":
            st.warning(f"**Status: {prediction}**")
        else:
            st.error(f"**Status: {prediction}**")
            
        st.info(f"Predicted Needs: {diet_plans[prediction]['Focus']}")

    with col2:
        st.subheader("🥗 Recommended Diet Plan")
        plan = diet_plans[prediction]
        
        st.table(pd.DataFrame({
            'Meal Time': ['Breakfast', 'Lunch', 'Evening Snack', 'Dinner'],
            'Suggestion': [plan['Breakfast'], plan['Lunch'], plan['Snack'], plan['Dinner']]
        }))
        st.caption(f"**Daily Calorie Target:** {plan['Calories']}")

    # 5. Visualization (Growth Chart)
    st.markdown("---")
    st.subheader("📊 Growth Analysis Chart")
    
    # Generate dummy reference data for the plot background
    # (Just for visual context to show where the child stands)
    ages = np.arange(2, 11)
    ideal_weights = (ages * 2) + 8  # Approx formula
    
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Plot 'Standard' line
    sns.lineplot(x=ages, y=ideal_weights, color='gray', linestyle='--', label="Avg Standard Growth", ax=ax)
    
    # Plot User's Child
    ax.scatter(age, weight, color='red', s=200, zorder=5, label="Your Child")
    ax.text(age, weight+1, "  You are here", color='red', fontsize=12)
    
    ax.set_xlabel("Age (Years)")
    ax.set_ylabel("Weight (kg)")
    ax.set_title(f"Growth Comparison for {age} Year Old {gender}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

else:
    st.info("👈 Please enter details in the sidebar and click 'Analyze'")
