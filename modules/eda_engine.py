import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df):
    st.subheader("🧾 Dataset Summary")

    # Shape & Columns
    st.write("**Shape of Data:**", df.shape)
    st.write("**Column Names:**", df.columns.tolist())

    # Data Types
    st.write("**Data Types:**")
    st.write(df.dtypes)

    # Null values
    st.write("**Missing Values:**")
    st.write(df.isnull().sum())

    # Descriptive Stats
    st.write("**Descriptive Statistics:**")
    st.write(df.describe())

    # Correlation Heatmap
    st.write("**Correlation Heatmap:**")
    corr = df.select_dtypes(include='number').corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Boxplots for numerical columns
    st.write("**Boxplots for Numerical Columns:**")
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x=col, ax=ax)
        st.pyplot(fig)

    # Categorical value counts
    st.write("**Top Categorical Columns Value Counts:**")
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols[:3]:  # Limit to 3 for speed
        st.write(f"**{col}**")
        st.write(df[col].value_counts())
