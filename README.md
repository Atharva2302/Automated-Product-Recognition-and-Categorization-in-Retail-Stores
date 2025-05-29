# Automated-Product-Recognition-and-Categorization-in-Retail-Stores
This project focuses on building an automated product recognition and categorization system using deep learning, specifically Convolutional Neural Networks (CNNs). It is designed for use in retail environments to streamline inventory management and checkout systems.

---

## 📁 Project Contents

- `custom_cnn_model.py` – Code for a CNN model built from scratch.
- `vgg16_transfer_learning.py` – Code using VGG16 pre-trained model.
- `data_preprocessing.py` – Data loading, augmentation, and preprocessing logic.
- `utils/` – Helper functions for image handling, plotting, and model evaluation.
- `results/` – Output files, confusion matrices, and model summaries.
- `Dessertation.pdf` – Full dissertation report.
- `README.md` – Project overview and instructions.
- `requirements.txt` – Python dependencies.

---

## 🔍 Project Objective

To design and implement an automated deep learning system that can:
- Accurately classify retail products into categories: **fruits**, **vegetables**, and **packaged goods**.
- Compare performance between a **custom CNN** and a **VGG16 transfer learning model**.
- Provide scalable solutions for **real-time retail applications**.

---

## 🧪 Methodology

The project follows the **CRISP-DM** data science lifecycle:
1. **Business Understanding**
2. **Data Collection & Exploration** (Kaggle image datasets)
3. **Data Preparation** (grayscale conversion, resizing, augmentation)
4. **Modeling**
   - Custom CNN with ReLU and softmax
   - VGG16 with frozen layers + fine-tuning
5. **Evaluation** (Accuracy, Precision, Recall, F1-score)
6. **Deployment Concept** (Model saving/loading for real-time integration)

---

## 📊 Key Results

| Model        | Accuracy | Notable Features |
|--------------|----------|------------------|
| Custom CNN   | ~92%     | Lightweight, effective with augmentation |
| VGG16        | ~96%     | Pre-trained efficiency, faster convergence |

- **VGG16 outperformed the custom model** in terms of overall accuracy and speed.
- **Data augmentation** improved generalisation and reduced overfitting, especially for underrepresented classes.

---

## 🛠️ Technologies Used

- Python 3.x
- TensorFlow / Keras
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn
- VGG16 (Transfer Learning)

---
## 👨‍💻 Author
Atharva Sapkal
