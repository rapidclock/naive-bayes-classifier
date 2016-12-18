import random
from ..exceptions.RTMLError import SizeMismatchException, OutOfRangeException


def test_train_split(features, labels, test_perc=0.5, rand=True):
	"""
	used to randomly(or not) split up data into test and train sample sets.

	Attrbs:
	features - The Feature set.
	labels - The Labels for the Features.
	test_perc - Testing set Percentage. Should be between 0 and 1. O.5 by Default.
	rand - Random sample or continuous block sampling. True by Default.
	"""
	if len(features) != len(labels):
		raise SizeMismatchException('features and labels have unequal lengths')
	if test_perc > 1.0 or test_perc < 0:
		raise OutOfRangeException('test percentage should be between 0 and 1.0')
	feat_train = []
	label_train = []
	feat_test = []
	label_test = []
	total_length = len(features)
	test_size = int(round(total_length * test_perc))
	if rand:
		feat_train = list(features[:])
		label_train = list(labels[:])

		for i in xrange(test_size):
			index = random.randint(0, total_length-1-i)
			feat = feat_train.pop(index)
			label = label_train.pop(index)
			feat_test.append(feat)
			label_test.append(label)
	else:
		feat_test = features[:test_size]
		label_test = labels[:test_size]
		feat_train = features[test_size:total_length]
		label_train = labels[test_size:total_length]
	return feat_train, label_train, feat_test, label_test


def print_list(lst):
	"""
	Prints Each item in a collection on one line
	"""
	for item in lst:
		print item


