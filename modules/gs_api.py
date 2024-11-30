from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from data.config import WORDS_LIST_ID, STOP_WORDS_LIST_ID


def get_creds():
	creds = Credentials.from_service_account_file('data/credentials.json')
	scoped = creds.with_scopes(
		['https://www.googleapis.com/auth/documents.readonly']
	)
	return scoped


def get_words_list(stop_words: bool = None) -> set[str]:
	service = build('docs', 'v1', credentials=get_creds())

	if stop_words:
		document_id = STOP_WORDS_LIST_ID
	else:
		document_id = WORDS_LIST_ID

	document = service.documents().get(documentId=document_id).execute()

	return set((
		document.get('body')['content'][1]['paragraph']
		['elements'][0]['textRun']['content']
	).lower().split(', '))


async def check_words_matches(text: str):
	text = text.lower()
	words = get_words_list()

	if bool(set(text.split()).intersection(words)):
		return True

	for word_or_phrase in words:
		if word_or_phrase in text:
			return True

	return False


async def check_stop_words_matches(text: str):
	text = text.lower()
	words = get_words_list(stop_words=True)

	if bool(set(text.split()).intersection(words)):
		return True

	for word_or_phrase in words:
		if word_or_phrase in text:
			return True

	return False
