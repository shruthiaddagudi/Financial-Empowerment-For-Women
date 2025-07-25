import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# App Title
st.title("💰 Financial Empowerment for Women")
st.subheader("Take control of your finances with smart tools and insights!")

# Sidebar Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Expense Tracker", "SIP Calculator", "EMI Calculator", "Investment Tracker", "AI Insights", "Gamified Learning"])

# Expense Tracker
def expense_tracker():
    st.header("📊 Expense Tracker")
    st.write("Track your daily expenses and manage your budget.")
    
    if "expenses" not in st.session_state:
        st.session_state.expenses = pd.DataFrame(columns=["Category", "Amount"])
    
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"])
    amount = st.number_input("Amount Spent (₹)", min_value=0.0, format="%.2f")
    
    if st.button("Add Expense"):
        new_expense = pd.DataFrame([[category, amount]], columns=["Category", "Amount"])
        st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
        st.success("Expense Added Successfully!")
    
    st.write(st.session_state.expenses)

# SIP Calculator
def sip_calculator():
    st.header("📈 SIP Calculator")
    principal = st.number_input("Monthly Investment (₹)", min_value=0.0, format="%.2f")
    rate = st.number_input("Expected Return Rate (% per annum)", min_value=0.0, max_value=100.0, format="%.2f")
    tenure = st.number_input("Investment Duration (Years)", min_value=1, max_value=50, step=1)
    
    if st.button("Calculate SIP Maturity"):
        n = tenure * 12
        r = (rate / 100) / 12
        maturity = principal * (((1 + r) ** n - 1) / r) * (1 + r)
        st.success(f"Maturity Amount: ₹{maturity:.2f}")

# EMI Calculator
def emi_calculator():
    st.header("🏦 EMI Calculator")
    loan = st.number_input("Loan Amount (₹)", min_value=0.0, format="%.2f")
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, format="%.2f")
    tenure = st.number_input("Loan Duration (Years)", min_value=1, max_value=50, step=1)
    
    if st.button("Calculate EMI"):
        n = tenure * 12
        r = (rate / 100) / 12
        emi = (loan * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        st.success(f"Monthly EMI: ₹{emi:.2f}")

# Investment Tracker
def investment_tracker():
    st.header("📊 Investment Portfolio Tracker")
    st.write("Manage and track your investments.")
    investment = st.text_input("Investment Name")
    amount = st.number_input("Investment Amount (₹)", min_value=0.0, format="%.2f")
    
    if "portfolio" not in st.session_state:
        st.session_state.portfolio = pd.DataFrame(columns=["Investment", "Amount"])
    
    if st.button("Add Investment"):
        new_investment = pd.DataFrame([[investment, amount]], columns=["Investment", "Amount"])
        st.session_state.portfolio = pd.concat([st.session_state.portfolio, new_investment], ignore_index=True)
        st.success("Investment Added Successfully!")
    
    st.write(st.session_state.portfolio)

# AI Investment Insights
def ai_insights():
    st.header("🔮 AI-Powered Investment Forecast")
    st.write("Predict your future investments using AI.")
    
    years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
    returns = np.array([5, 7, 9, 12, 15, 18, 22, 27, 33, 40])
    model = LinearRegression().fit(years, returns)
    
    future_years = np.array([i for i in range(1, 16)]).reshape(-1, 1)
    predictions = model.predict(future_years)
    
    plt.figure(figsize=(8, 5))
    plt.plot(future_years, predictions, marker='o', linestyle='-', color='b', label='Projected Growth')
    plt.xlabel("Years")
    plt.ylabel("Investment Returns (%)")
    plt.title("Projected Investment Growth Over 15 Years")
    plt.legend()
    st.pyplot(plt)

# Gamified Learning
def gamified_learning():
    st.header("🎮 Gamified Learning")
    st.write("Learn finance with fun quizzes and rewards!")
    question = "What is the best way to build an emergency fund?"
    options = ["Invest in stocks", "Save in a high-interest account", "Spend less", "Buy gold"]
    answer = st.radio("Choose the correct answer:", options)
    
    if st.button("Submit Answer"):
        if answer == "Save in a high-interest account":
            st.success("Correct! Emergency funds should be easily accessible with good interest.")
        else:
            st.error("Incorrect! Try again.")

# Page Routing
if option == "Expense Tracker":
    expense_tracker()
elif option == "SIP Calculator":
    sip_calculator()
elif option == "EMI Calculator":
    emi_calculator()
elif option == "Investment Tracker":
    investment_tracker()
elif option == "AI Insights":
    ai_insights()
elif option == "Gamified Learning":
    gamified_learning()
