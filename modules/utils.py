import re


def extract_username(message: str) -> str:
	pattern = r'@([A-Za-z0-9_]+)'
	match = re.search(pattern, message)

	if match:
		return re.sub(r'\W+', '', match.group(1))
	else:
		return ''
