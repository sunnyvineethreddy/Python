from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB

# Loading the dataset
iris = datasets.load_iris()

#
model = GaussianNB()
# # getting the data and response of the dataset
x = iris.data
y = iris.target

splits = train_test_split(x,y,test_size=0.2)
# target_names = ['class 0', 'class 1', 'class 2']
X_train, X_test, y_train, y_test =splits
#print(splits)
model.fit(X_train,y_train)
expected = y_test
predicted = model.predict(X_test)

# The classification_report function builds a text report showing the main classification metrics
print(metrics.classification_report(expected,predicted))

# Compute confusion matrix to evaluate the accuracy of a classification
print(metrics.confusion_matrix(expected,predicted))

# Accuracy Score
print("Accuracy",metrics.accuracy_score(expected,predicted))
# Precision Score
print("Precision",metrics.precision_score(expected,predicted, average='micro'))
# Recall Score
print("Recall",metrics.recall_score(expected,predicted, average='micro'))
# F1 score can be interpreted as a weighted average of the precision and recall
print("f1 score",metrics.f1_score(expected,predicted, average='micro'))
