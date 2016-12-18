import cPickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Unpickling the train - test split.
print 'UnPickling Data. Please wait...'
(x_train, y_train, x_test, y_test, labels, display_names) = cPickle.load(open('save.p', 'rb'))
print 'UnPickling completed'

# Creating clas of the SK Learn Classifier.
sk_clf = MultinomialNB()

# Fitting Training Data into the classifier.
sk_clf.fit(x_train, y_train)

# Predicting the test data.
y_pred = sk_clf.predict(x_test)

# Printing SK Learn Accuracy.
print 'Accuracy of SK Learn Classifier - ', accuracy_score(y_test, y_pred)

# Printing Metrics of precision, recall, f-score per class.
print (classification_report(y_test, y_pred, labels=labels, target_names=display_names))