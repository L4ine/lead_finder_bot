from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from data.config import WORDS_LIST_ID


def get_creds():
	creds = Credentials.from_service_account_file('data/credentials.json')
	scoped = creds.with_scopes(
		['https://www.googleapis.com/auth/documents.readonly']
	)
	return scoped


def get_words_list() -> list[str]:
	service = build('docs', 'v1', credentials=get_creds())
	document = service.documents().get(documentId=WORDS_LIST_ID).execute()
	return (
		document.get('body')['content'][1]['paragraph']
		['elements'][0]['textRun']['content']
	).split(',')


async def check_words_matches(text):
	return bool(set(text.split()).intersection(get_words_list()))
