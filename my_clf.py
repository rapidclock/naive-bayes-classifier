from rtml.rt_csv.csv_parser import CSV_Parser
from rtml.utils.cleanup import CleanUp
from rtml.utils.extras import test_train_split, print_list
from rtml.ml_algos.naivebayes import NaiveBayesClassifier
from rtml.utils.analytics import accuracy, evaluate, print_metrics
from rtml.utils.prep import SK_Prep
import cPickle

# Parsing CSV File
new_csv = CSV_Parser('tweets.csv')

# Getting Labels and Features from the CSV, by index of column in the csv.
labels = new_csv.get_by_index(1) 
feats = new_csv.get_by_index(2)

# Removing the header of the Column
labels = labels[1]
feats = feats[1]

# Performing cleanup and tokenization of the features
my_cleaner = CleanUp(feats)
feats = my_cleaner.process()

# Randomly Split training and testing data
feat_train, label_train, feat_test, label_test = test_train_split(feats, labels, 0.4)

# Create new class of the custom home-made classifier.
clf = NaiveBayesClassifier()

# Fitting the training data.
clf.fit(feat_train,label_train)

# Predicting based on test data.
final_pred = clf.predict(feat_test)

# Accuracy of Custom Classifier.
print 'Accuracy of Custom Classifier - ', accuracy(label_test, final_pred)

# Generating metrics of precision, recall, f-score by class.
metrics = evaluate(label_test, final_pred)
print_metrics(metrics)

#### Data Prep for SK-Learn ####

# numpy-izing the lists and pickling for use by SK Learn.
sk_prep = SK_Prep(feat_train, label_train)

x_train, y_train = sk_prep.build_matrices(feat_train, label_train)
x_test, y_test = sk_prep.build_matrices(feat_test, label_test)

# Numeric value for labels.
label_ids = sk_prep.get_labels()
# Actual Display name for labels.
display_names = sk_prep.get_display_labels()

print 'Pickling the data. Please wait...'
cPickle.dump((x_train, y_train, x_test, y_test, label_ids, display_names), open('save.p', 'wb'))
print 'Pickling Completed'
