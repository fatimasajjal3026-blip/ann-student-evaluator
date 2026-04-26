import pandas as pd

# Load dataset
data = pd.read_excel("dataset.xlsx")

print(data.head())
print(data.columns)
print(data.shape)

# --------------------
# Preprocessing
# --------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = data.drop("result", axis=1)
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --------------------
# ANN Model
# --------------------
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=500)

# Train
model.fit(X_train, y_train)

# --------------------
# Evaluation
# --------------------
from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# --------------------
# Save Model
# --------------------
import joblib

joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("Saved!")