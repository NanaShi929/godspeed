#Library Method

import pandas as pd
import kagglehub
import os
import numpy as np
from sklearn.model_selection import train_test_split


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Download dataset
path = kagglehub.dataset_download("abhishek14398/salary-dataset-simple-linear-regression")

# Load CSV
# Correcting path construction and filename based on inspection of kernel state
csv_file = os.path.join(path, "Salary_dataset.csv")
data = pd.read_csv(csv_file)

x = data["YearsExperience"].values
y = data["Salary"].values
# Reshape x for sklearn
X = x.reshape(-1, 1)
Y = y

# Train Test Split (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predictions
Y_pred_test = model.predict(X_test)

# R2 Score on Test Data
r2_lib = r2_score(Y_test, Y_pred_test)

print("Library Method Results")
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)
print("Test R2 Score:", r2_lib)
