class RTMLError(Exception):
	"""
	Base class for all exceptions in this module
	"""
	pass


class IndexOOBException(RTMLError):
	"""
	Used to indicate that some index is out of bounds of a collection.
	"""
	def __init__(self, value=''):
		self.value = value
	def __str__(self):
		return repr(self.value)


class SizeMismatchException(RTMLError):
	"""
	Used to indicate that two sets of Collections have different lengths.
	"""
	def __init__(self, value=''):
		self.value = value
	def __str__(self):
		return repr(self.value)


class OutOfRangeException(RTMLError):
	"""
	Used to indicate that value should lie within a certain range.
	"""
	def __init__(self, value='value out of range'):
		self.value = value
	def __str__(self):
		return repr(self.value)