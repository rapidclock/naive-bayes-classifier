import csv
from ..exceptions.RTMLError import IndexOOBException

class CSV_Parser():
	"""
	CSV Parser class : Used to parse a csv file into headers and lines.

	Has Useful functions to aid csv processing.
	"""
	def __init__(self, filename=None):
		"""
		Signature : String
		filename(String) - name of the csv file.

		If filename is not initially specified, or if a new File has to be processed,
		use the set_file(filename) function of this class
		"""
		if filename != None:
			self.filename = filename
			self.process()

	def process(self):
		"""
		Used to preprocess the csv file.
		Also builds meta-data.
		"""
		reader = csv.reader(open(self.filename))
		all_lines = []
		for line in reader:
			all_lines.append(line)
		self.headers = all_lines[0]
		self.lines = all_lines[1:]
		self.col_count = len(self.headers)
		self.line_count = len(self.lines)

	def get_by_index(self, index):
		"""
		Given a valid index of a column in the file, 
		returns a tuple containing the header and all values for that header.
		"""
		if(index >= self.col_count):
			raise IndexOOBException('You gave an index greater than num of columns')
		else:
			line_list = [item[index] for item in self.lines]
			return (self.headers[index], line_list)

	def get_headers(self):
		"""
		Returns all headers for the file
		"""
		return self.headers

	def get_lines(self):
		"""
		Returns all lines for the file.
		"""
		return self.line