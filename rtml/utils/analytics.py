from ..exceptions.RTMLError import SizeMismatchException


def accuracy(orig_label, pred_label):
	if len(orig_label) != len(pred_label):
		raise SizeMismatchException('original and predicted values are unequal in size.')
	n_o = len(orig_label)
	n_p = len(pred_label)
	total_count = n_o
	acc_count = 0
	for i in range(total_count):
		if orig_label[i] == pred_label[i]:
			acc_count += 1
	final_accuracy = (float(acc_count)/total_count)
	return final_accuracy

def evaluate(orig_label, pred_label):
	list_of_labels = set(orig_label[:])
	result = []
	pred_dict = {}
	orig_dict = {}
	for label in pred_label:
		if label in pred_dict:
			pred_dict[label] += 1
		else:
			pred_dict[label] = 1
	for label in orig_label:
		if label in orig_dict:
			orig_dict[label] += 1
		else:
			orig_dict[label] = 1
	for label in list_of_labels:
		acc_pred_count = 0
		for i in xrange(len(orig_label)):
			if pred_label[i] == label:
				if pred_label[i] == orig_label[i]:
					acc_pred_count += 1
		precision = float(acc_pred_count)/pred_dict[label]
		recall = float(acc_pred_count)/orig_dict[label]
		f1_score = 2.0 * ((precision * recall)/(precision + recall))
		result.append((label, precision, recall, f1_score))
	return result

def print_metrics(eval):
	print 'Custom Classifier Metrics Below :'
	for record in eval:
		print 'Class - ', record[0],' Precision - ', record[1], ' Recall - ', record[2], ' F-Score - ', record[3]