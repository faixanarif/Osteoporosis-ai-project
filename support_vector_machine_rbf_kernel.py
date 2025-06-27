from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

rbf_svm = SVC(kernel='rbf', random_state=42)
rbf_svm.fit(X_train_scaled, y_train)
y_pred = rbf_svm.predict(X_test_scaled)
print(f"RBF SVM Accuracy: {accuracy_score(y_test, y_pred):.4f}")

