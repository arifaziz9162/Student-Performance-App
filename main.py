import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from logger_config import logger

# ----------------------------- Custom Exception ----------------------------
class PredictionError(Exception):
    """ Custom exception for prediction related errors."""
    pass

# ----------------------------- Prediction class ------------------------------
class StudentPerformacePredictor:
    def __init__(self, model_path="student_pr_final_model.pkl"):
        try:
            with open(model_path, "rb") as file:
                self.model, self.scaler, self.le = pickle.load(file)
            logger.info("Model, scaler, and label encoder loaded successfully.")
        except Exception as e:
            logger.error("An unexpected error occurred while loading model file: %s", e, exc_info=True)
            raise PredictionError("Failed to load the model file.")

    def preprocess(self, data):
        try:
            data["Extracurricular Activities"] = self.le.transform([data["Extracurricular Activities"]])[0]
            df = pd.DataFrame([data])
            df_transformed = self.scaler.transform(df)
            logger.info("Data preprocessing successfully.")
            return df_transformed
        except Exception as e:
            logger.error("An unexpected error occurred while preprocessing data: %s", e, exc_info=True)
            raise PredictionError("Failed to preprocess data.")

    def predict(self, data):
        try:
            processed_data = self.preprocess(data)
            prediction = self.model.predict(processed_data)
            logger.info("Prediction successful.")
            return prediction
        except Exception as e:
            logger.error("An unexpected error occurred during prediction: %s", e, exc_info=True)
            raise PredictionError("Failed to predict.")

def main():
    st.title("Student Performance Prediction")
    st.write("Enter your data to get a prediction for your performance")

    hours_studied = st.number_input("Hours Studied", min_value = 1, max_value = 10, value = 5)
    previous_score = st.number_input("Previous Scores", min_value = 40, max_value = 100, value = 70)
    extra_curr_act = st.selectbox("Extracurricular Activities", ['Yes', 'No'])
    sleeping_hours = st.number_input("Sleep hours", min_value = 4, max_value = 10, value = 7)
    number_of_paper_solved = st.number_input("Sample Question Papers Practiced", min_value = 0, max_value = 10, value = 5)

    if st.button("Predict-Your_Score"):
        user_data = {
            "Hours Studied":hours_studied,
            "Previous Scores":previous_score,
            "Extracurricular Activities":extra_curr_act,
            "Sleep Hours":sleeping_hours,
            "Sample Question Papers Practiced":number_of_paper_solved
        }
        try:
            predictor = StudentPerformacePredictor()
            prediction = predictor.predict(user_data)
            st.success(f"Your prediction result is {prediction[0]:.2f}")
        except PredictionError as pe:
            st.error(f"Prediction failed: {pe}")
        except Exception as e:
            st.error("An unexpected error occurred. Check logs file for details.")
            logger.critical("Crash Progam: %s", e, exc_info=True)

if __name__ == "__main__":
    main()
