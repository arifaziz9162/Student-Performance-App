# Student Performance Prediction 🎓

This project predicts student performance based on study habits, previous scores, sleep hours, extracurricular activities, and practice tests.  
It uses a trained machine learning model with preprocessing (scaling + label encoding) and provides an interactive **Streamlit** app.

---

## 🚀 Features
- Streamlit web interface  
- Machine Learning model (pickled)  
- Custom exception handling & logging  
- Preprocessing with `StandardScaler` and `LabelEncoder`

---

## ⚙️ Installation (Anaconda + VS Code)

1. **Clone the repo**
   ```bash
   git clone https://github.com/arifaziz9162/student-performance-app.git
   cd student-performance-app

2. Create a new conda environment
conda create -n student_pred python=3.11
conda activate student_pred

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run student_performance_app.py

📂 Project Structure
├── app.py                     
├── student_pr_final_model.pkl  
├── logger_config.py            
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore

🧑‍💻 Author
MD ARIF AZIZ
📧 arifaziz0125@gmail.com