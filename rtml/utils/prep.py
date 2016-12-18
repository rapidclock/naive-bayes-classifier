import numpy as np

class SK_Prep():
	"""
	Class used to construct data ready for SK Learn functions.
	"""
	def __init__(self, x_train, y_train):
		"""
		Given a ListOf[ListOf[features]] and ListOf[labels], builds a dictionary for the same.
		Where, a feature is a word.
		"""
		self.feat_dict = {}
		self.label_dict = {}
		self.__build_feature_dictionary(x_train)
		self.__build_label_dictionary(y_train)
		self.__generate_numpy_feat()
		pass

	def __build_feature_dictionary(self, x):
		count = 0
		for feat_set in x:
			for feat in feat_set:
				if feat not in self.feat_dict:
					self.feat_dict[feat] = count
					count += 1
		self.num_of_feat = count

	def __build_label_dictionary(self, y):
		count = 0
		for label in y:
			if label not in self.label_dict:
				self.label_dict[label] = count
				count += 1
		self.num_of_label = count

	def __generate_numpy_feat(self):
		self.feat_row = [0 for x in range(self.num_of_feat)]
		self.numpy_list = np.array([0 for x in range(self.num_of_feat)])

	def build_matrices(self, x_given, y_given):
		"""
		Based on the built dictionary, build the numpy 2D matrix for the given set of features
		and labels.
		Given : ListOf<features> ListOf<labels>
		Returns : Numpy[features], Numpy[labels]
		"""
		vanilla_matrix_feat = self.__build_vanilla_matrix_feat(len(x_given))
		vanilla_matrix_label = self.__build_vanilla_matrix_label(len(y_given))
		matrix_feat = self.__populate_matrix_feat(vanilla_matrix_feat, x_given)
		matrix_label = self.__populate_matrix_label(vanilla_matrix_label, y_given)
		return np.array(matrix_feat), np.array(matrix_label)

	def __build_vanilla_matrix_feat(self, num_of_rows):
		return [self.feat_row[:] for i in range(num_of_rows)]

	def __build_vanilla_matrix_label(self, num_of_rows):
		return [0 for x in range(num_of_rows)]

	def __populate_matrix_feat(self, vanilla_matrix_feat, x_given):
		for i in range(len(x_given)):
			for feat in x_given[i]:
				if feat in self.feat_dict:
					vanilla_matrix_feat[i][self.feat_dict[feat]] += 1
		return vanilla_matrix_feat

	def __populate_matrix_label(self, vanilla_matrix_label, y_given):
		for i in range(len(y_given)):
			vanilla_matrix_label[i] = self.label_dict[y_given[i]]
		return vanilla_matrix_label

	def get_labels(self):
		return [x[1] for x in sorted(self.label_dict.items(), key=lambda x : x[1])]

	def get_display_labels(self):
		print sorted(self.label_dict.items(), key=lambda x : x[1])
		return [x[0] for x in sorted(self.label_dict.items(), key=lambda x : x[1])]
