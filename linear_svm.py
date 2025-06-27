from sklearn.svm import LinearSVC

linear_svm = LinearSVC(random_state=42, max_iter=10000)
linear_svm.fit(X_train_scaled, y_train)
y_pred = linear_svm.predict(X_test_scaled)
print("Linear SVM Accuracy:", accuracy_score(y_test, y_pred))
