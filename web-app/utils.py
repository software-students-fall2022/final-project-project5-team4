
def extract_first_sentence(text: str) -> str:
	return text.split('.')[0]

def parse_yes_no_to_bool(text: str) -> bool:
	return text == 'yes'