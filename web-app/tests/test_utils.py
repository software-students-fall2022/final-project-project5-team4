from utils import *

class Tests:
    def test_extract_first_sentence(self):
        sentence = "This is a sentence. This is one also."
        first = extract_first_sentence(sentence)
        assert first == "This is a sentence."

    def test_parse_yes_no_to_bool(self):
        yesNo = "yes"
        tf = parse_yes_no_to_bool(yesNo)
        assert tf == True
