# Osteoporosis-ai-project
Project how ai can be used - AI can detect osteoporosis by analyzing medical images like X-rays or DEXA scans to identify patterns of bone loss. Machine learning models can predict bone density levels and assess fracture risk. This helps in early diagnosis and personalized treatment planning.

Heres the entire summary 

# 🦴 Osteoporosis Detection using Machine Learning

This project demonstrates how **AI** can be used to detect **osteoporosis** by analyzing pre-extracted image features from medical scans such as X-rays or DEXA. It applies multiple machine learning models to classify bone health status (Normal or Osteoporotic), and evaluates their performance using accuracy metrics and confusion matrices.

---

## 📂 Project Structure

- `pythonproject.ipynb` – Main Jupyter notebook containing all code, models, and visualizations.
- `image_features.csv` – Feature dataset extracted from bone scan images (not included; add your own or use a sample).
- `README.md` – Project overview and usage instructions.

---

## 🚀 How It Works

1. **Load Data**: Reads image-based features from a CSV file.
2. **Preprocessing**: Applies standard scaling to normalize feature values.
3. **Model Training & Testing**:
   - **Support Vector Machines (SVM)** – Linear and RBF kernels
   - **K-Nearest Neighbors (KNN)**
   - **Random Forest Classifier**
   - **Gaussian Naive Bayes**
4. **Evaluation**: Each model is evaluated using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report

---

## 📈 Example Output

Confusion matrix plot:
- X-axis: Predicted labels
- Y-axis: True labels  
Helps visualize model accuracy in distinguishing between Osteoporosis and Normal cases.

---

## 🧠 Tech Stack

- Python
- Jupyter Notebook
- Pandas, NumPy
- Scikit-learn
- Seaborn & Matplotlib

---

## 🛠️ How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/faixanarif/Osteoporosis-ai-project.git
   cd Osteoporosis-ai-project
