# ===============================
# Logistic Regression - Heart Disease Prediction
# ===============================

# 1. Import required libraries
import kagglehub
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 2. Download dataset using KaggleHub
path = kagglehub.dataset_download(
    "dileep070/heart-disease-prediction-using-logistic-regression"
)

print("Dataset path:", path)

# 3. Load dataset
df = pd.read_csv(path + "/framingham.csv")

# 4. Select features and target
features = [
    'male',
    'age',
    'education',
    'currentSmoker',
    'cigsPerDay',
    'BPMeds',
    'prevalentStroke',
    'prevalentHyp',
    'diabetes',
    'totChol'
]

X = df[features]
y = df['TenYearCHD']

# 5. Handle missing values
X = X.fillna(X.mean())
y = y.fillna(y.mode()[0])

# 6. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 8. Make predictions
y_pred = model.predict(X_test)

# 9. Evaluate model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# 10. Print results
print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:")
print(cm)
