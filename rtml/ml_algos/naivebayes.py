from ..exceptions.RTMLError import SizeMismatchException

class NaiveBayesClassifier():
	def __init__(self):
		self.labels = {}
		self.label_split = {}
		self.features = {}
		self.feature_bar_label = {}
		self.train_size = 0
		self.total_feats = 0

	def fit(self, feat_train, label_train):
		if len(feat_train) != len(label_train):
			raise SizeMismatchException('features and labels have unequal lengths')
		length = len(feat_train)
		self.train_size = length
		for i in xrange(length):
			feat_list = feat_train[i]
			label = label_train[i]
			for feat in feat_list:
				self.total_feats += 1
				if self.features.has_key(feat):
					self.features[feat] = self.features.get(feat) + 1
				else:
					self.features[feat] = 1
				f_b_l = (feat, label)
				if f_b_l in self.feature_bar_label:
					self.feature_bar_label[f_b_l] = self.feature_bar_label.get(f_b_l) + 1
				else:
					self.feature_bar_label[f_b_l] = 1
				if self.labels.has_key(label):
					self.labels[label] = self.labels.get(label) + 1
				else:
					self.labels[label] = 1
			if self.label_split.has_key(label):
				self.label_split[label] = self.label_split.get(label) + 1
			else:
				self.label_split[label] = 1

	def predict_full(self, feat_test):
		"""
		Given :
		feat-test -> LoF[LoF[feature]]
		Result :
		prediction -> LoF[LoF[class_prob]]
		where,
		LoF[class_prob] is sorted descending based on the probability.
		class_prob -> (class, prob_for_class)
		"""
		list_of_labels = self.labels.keys()
		results = []
		# Getting each list of features from the list of lists.
		for feat_list in feat_test:
			class_prob = []
			# Calculating the probability for each label(as per naive bayes).
			for label in list_of_labels:
				prob = (self.__prob_feat_given_label(label, feat_list) * self.__prob_label(label))/self.__prob_feats(feat_list)
				class_prob.append((label, prob))
			# Normalizing the calculated probabilities.
			sum = 0
			for label, prob in class_prob:
				sum += prob
			for i in range(0, len(class_prob)):
				label, prob = class_prob[i]
				norm_prob = prob/sum
				class_prob[i] = (label, norm_prob)
			# Sorting based on the probabilities per class.
			class_prob.sort(key = lambda item : item[1], reverse=True)
			results.append(class_prob)
		return results


	def __filter_predictions(self, feat_test):
		"""
		Filters out the class with the highest probability score from the full
		list of predictions per feature set.
		"""
		results = self.predict_full(feat_test)
		filtered_list = []
		for item in results:
			filtered_list.append(item[0])
		return filtered_list
		
	def predict(self, feat_test):
		"""
		Returns a list of classes which correspond to the index of the training set data.
		"""
		interm_pred = self.__filter_predictions(feat_test)
		label_pred = []
		for item in interm_pred:
			label_pred.append(item[0])
		return label_pred

	def __prob_feat_given_label(self, label, tr_feats):
		"""
		Introduces Laplace Smoothening to the regular P(feature|class)
		"""
		prob_product = 1
		for feat in tr_feats:
			f_b_l = (feat, label)
			occ = 1
			if f_b_l in self.feature_bar_label:
				occ += self.feature_bar_label[f_b_l]
			freq = self.labels[label] + 1
			prob = float(occ)/freq
			prob_product *= prob
		return prob_product

	def __prob_label(self, label):
		return float(self.label_split[label])/self.train_size

	def __prob_feats(self, tr_feats):
		prob_product = 1
		for feat in tr_feats:
			if feat in self.features:
				occ = self.features[feat]
				frq = self.total_feats
				prob = float(occ)/frq
				prob_product *= prob
			else:
				occ = 1
				frq = self.total_feats + 1
				prob = float(occ)/frq
				prob_product *= prob
		return prob_product

	def __test_label(self, label):
		return float(self.labels[label])/self.total_feats

