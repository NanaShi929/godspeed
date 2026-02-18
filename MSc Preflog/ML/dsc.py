import kagglehub
import pandas as pd
import numpy as np
import os
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Download dataset
path = kagglehub.dataset_download("fredericobreno/play-tennis")
print("Path:", path)

# 2. Load CSV automatically
for f in os.listdir(path):
    if f.endswith(".csv"):
        csv_path = os.path.join(path, f)

df = pd.read_csv(csv_path)
print("\nDataset:\n", df)

# 3. Select correct features (REMOVE day)
features = ['outlook', 'temp', 'humidity', 'wind']
target = 'play'

# ===============================
# TRAIN TEST SPLIT
# ===============================
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df[target])

print("\nTrain size:", len(train_df))
print("Test size:", len(test_df))

# ===============================
# ENTROPY FUNCTION
# ===============================
def entropy(data):
    values, counts = np.unique(data, return_counts=True)
    ent = 0
    for i in range(len(values)):
        prob = counts[i] / sum(counts)
        ent -= prob * math.log2(prob)
    return ent

# ===============================
# INFORMATION GAIN FUNCTION
# ===============================
def information_gain(df, feature, target):
    total_entropy = entropy(df[target])

    values, counts = np.unique(df[feature], return_counts=True)
    weighted_entropy = 0

    for i in range(len(values)):
        subset = df[df[feature] == values[i]]
        subset_entropy = entropy(subset[target])
        weight = counts[i] / sum(counts)
        weighted_entropy += weight * subset_entropy

    ig = total_entropy - weighted_entropy
    return ig

# ===============================
# ID3 ALGORITHM
# ===============================
def ID3(data, features, target):

    # If pure node
    if len(np.unique(data[target])) == 1:
        return np.unique(data[target])[0]

    # If no features left
    if len(features) == 0:
        return data[target].mode()[0]

    # Compute IG
    igs = [information_gain(data, f, target) for f in features]
    best = features[np.argmax(igs)]

    tree = {best: {}}
    remaining = [f for f in features if f != best]

    for value in np.unique(data[best]):
        subset = data[data[best] == value]

        if len(subset) == 0:
            tree[best][value] = data[target].mode()[0]
        else:
            tree[best][value] = ID3(subset, remaining, target)

    return tree

# ===============================
# BUILD TREE USING TRAIN DATA
# ===============================
decision_tree = ID3(train_df, features, target)

# ===============================
# PRINT TREE FUNCTION
# ===============================
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→", tree)
        return
    for key in tree:
        print(indent + key)
        for value in tree[key]:
            print(indent + " ├─", value)
            print_tree(tree[key][value], indent + " │   ")

print("\n--- FINAL ID3 DECISION TREE ---\n")
print_tree(decision_tree)

# ===============================
# PREDICTION FUNCTION
# ===============================
def predict(tree, sample):

    if not isinstance(tree, dict):
        return tree

    root = list(tree.keys())[0]
    value = sample[root]

    if value not in tree[root]:
        return None  # unseen value

    return predict(tree[root][value], sample)

# ===============================
# TEST SET PREDICTIONS
# ===============================
y_true = test_df[target].values
y_pred = []

for _, row in test_df.iterrows():
    pred = predict(decision_tree, row)
    if pred is None:
        pred = train_df[target].mode()[0]
    y_pred.append(pred)

y_pred = np.array(y_pred)

# ===============================
# EVALUATION METRICS
# ===============================
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, pos_label='Yes')
recall = recall_score(y_true, y_pred, pos_label='Yes')
f1 = f1_score(y_true, y_pred, pos_label='Yes')


print("\n--- TEST SET PERFORMANCE ---")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
