import kagglehub
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Download dataset
path = kagglehub.dataset_download("nikhil7280/student-performance-multiple-linear-regression")

# Load dataset
csv_file = [f for f in os.listdir(path) if f.endswith(".csv")][0]
df = pd.read_csv(os.path.join(path, csv_file))

# Independent variables (all columns except last)
X = df.iloc[:, :-1]

# Dependent variable (last column)
y = df.iloc[:, -1]

# Convert categorical columns to numeric
X = pd.get_dummies(X, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Coefficients
intercept = model.intercept_
coefficients = model.coef_

# Predictions on test data
y_pred = model.predict(X_test)

# R-squared value
r2 = r2_score(y_test, y_pred)

# Output

print("R-squared value:", round(r2, 3))
