from utils import *

class Test:
	def test_parse_yes_no_to_bool_yes(self):
		result = parse_yes_no_to_bool("yes")
		assert result == True

	def test_parse_yes_no_to_bool_no(self):
		result = parse_yes_no_to_bool("no")
		assert result == False