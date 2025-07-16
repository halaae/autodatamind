import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def run_ml(df):
    st.subheader("🧠 Auto Machine Learning")

    # Choose target
    target = st.selectbox("🎯 Select Target Column", df.columns)

    if target:
        X = df.drop(columns=[target])
        y = df[target]

        # Remove non-numeric columns from features
        X = X.select_dtypes(include=['number'])

        if X.empty:
            st.error("❌ No numeric features to train on.")
            return

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Show metrics
        st.write("✅ **Classification Report**")
        st.text(classification_report(y_test, y_pred))

        st.write("🧩 **Confusion Matrix**")
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        st.pyplot(fig)

        st.success("🎉 Model trained and evaluated!")
