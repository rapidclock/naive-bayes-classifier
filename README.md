# Naive Bayes Classifer
> By Rahul Thomas
---
---
## My Classifier:
#### read_data :
Reading is done using the custom class `CSV_Parser` found in the package `rtml.rt_csv.csv_parser`.
An instance of CSV_Parser is created and the csv_filename is given as the input.
 ```python
 new_csv = CSV_Parser('tweets.csv')
 ```
Next, the tweets and handles are retrieved from the tweets
 ```python
 labels = new_csv.get_by_index(1) 
 feats = new_csv.get_by_index(2)
 ```
The `CSV_Parser.get_by_index($index)` returns a tuple containing the header and a list of contents for that header.
Next, we get the list of tweets and labels(tweet handles) from the above(2nd parameter in the tuple)
```python
labels = labels[1]
feats = feats[1]
```
---
#### cleanup :
Clean up is also done with a custom built class called `CleanUp` class found in the package `rtml.utils.cleanup`.
The input list of sentences are passed to this class along with options to perform for cleanup on each sentence.
`CleanUp(input, [tokenize], [url], [punct], [lower], [stopwords])`
 - **input** - the input list of sentences
 - **tokenize** - flag(def: True) to tokenize the cleaned sentences into list of words.
 - **url** - flag(def: True) to filter urls.
 - **punct** - flag(def: True) to filter punctuations.
 - **lower** - flag(def: True) convert all words to lowecase.
 - **stopwords** - flag(def: True) to filter stopwords. The stopwords are given by default in a file called `stopwords.txt`. You can provide your own words in that file. The words are dynamically loaded at runtime from the file.

We now call the `CleanUp.process() -> List[features]` method to process as per our requirements.
*Note :* If tokenize was set to true, then you get back a List[List[features]], where each feature is a word.
```python
my_cleaner = CleanUp(feats)
feats = my_cleaner.process()
```

Next we split the training and test data using the custom utility function `test_train_split` found in package `rtml.utils.extras`.
```python
# Signature for train_test_split :
test_train_split(features, labels, test_perc=0.5, rand=True)
```
---
#### Naive Bayes Classifier(fit, predict, evaluate):
This is done using the custom class `NaiveBayesClassifier` from the package `rtml.ml_algos.naivebayes`.
First an instance of the class is created.
```python
clf = NaiveBayesClassifier()
```
Next we fit the training data.
```python
clf.fit(feat_train,label_train)
```
##### fit : 
**Signature : `NaiveBayesClassifier.fit(feat_train, label_train)`**
The classifier uses a dictionary methodology to store statistics regarding the features and classes and uses them at the time of testing.
It stores the counts for features, features per class, class statistics total number of features and total number of tweets, words per class.

##### predict : 
We have two options for prediction in this classifier. Although the predictions themselves remain the same, the format of the output and level of detain are different.
_**option 1 :`NaiveBayesClassifier.predict_full(feat_test)`**_
_Given:_ A list of test features(List of List of Words) i.e `[[feat1 ... featn], [feat1 ... featn], ... [feat1 ... featn]]` where each sublist is termed a feature_set.
_Returns:_ `[(pred_class1, pred_perc), (pred_class2, pred_perc) ... (pred_classn, pred_perc)]` for each feature set in the training data ordered _descendingly_ by the precentage.
_**option 2 :`NaiveBayesClassifier.predict(feat_test)`**_
_Given:_ A list of test features(List of List of Words) i.e `[[feat1 ... featn], [feat1 ... featn], ... [feat1 ... featn]]` where each sublist is termed a feature_set.
_Returns:_ `[class, ... class]` A list of classes with highest probability corresponding to each feature set.
This is more useful in calculating metrics and comparing for accuracy.

##### evaluate :
**Signature : `evaluate(orig_label, pred_label)` :**
**Returns : `(label, precision, recall, f1_score)` per class.**
This function evaluates precision, recall, f1-score for each of the class.
---
---
## SK Learn Classifier:
We do some preprocessing for the SK_Learn Naive Bayes Classifier for converting the list of words to Numpy format. 
We use a bag of words type representation for the numpy data.

```python
sk_prep = SK_Prep(feat_train, label_train)
x_train, y_train = sk_prep.build_matrices(feat_train, label_train)
x_test, y_test = sk_prep.build_matrices(feat_test, label_test)
```

Now this pickled and de-pickled and fed into the sk_learn classifier.

After this we use the sklearn library's `accuracy_score` and `classification_report` to calculate the metrics for the sklearn classifier.

From the accuracy comparison between the Custom Classifier and the SK_Learn Classifier, we can see that both classifiers have an accuracy `~90%`.

The Recall, precison and f1-score between the two classifiers are within fractions of each other, therefore we cannot effectively say that there is a difference between them. Hence we cannot give reasons why the two classifiers are different.

_Note:_ The custom classifier performs exactly equally or marginally better on a majority of the cases.

---
---