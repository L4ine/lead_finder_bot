import time
import logging

from asyncio import sleep

from telethon import TelegramClient
from telethon.types import Message

from db.db_api import get_setting, get_sources, \
	record_exists, add_record

from modules.gs_api import check_words_matches
from data.config import TG_API_ID, TG_API_HASH


async def parse_source(source: str) -> None:
	try:
		client = TelegramClient(
			'data/userbot',
			TG_API_ID,
			TG_API_HASH,
			system_version='4.16.30-vxCUSTOM'
		)
		await client.start()
	except Exception as exc:
		logging.error(f'Error in parse_source - userbot block: {exc}')
		return

	target_channel_setting = await get_setting('target_channel')

	if not target_channel_setting:
		return

	target_entity = await client.get_entity(target_channel_setting.value)

	try:
		source_entity = await client.get_entity(source)

		messages: list[Message] = await client.get_messages(source_entity, limit=10)

		for post in messages:
			try:
				if await record_exists(source, post.id):
					continue

				if not await check_words_matches(post.message):
					continue

				await client.forward_messages(
					target_entity, post.id, source_entity
				)

				await add_record(source, post.id)
				await sleep(15)

			except Exception as exc:
				logging.error(f'Error in parse_source - forward_messages block \
					{source}/{post.id}: {exc}')

	except Exception as exc:
		logging.error(f'Error in parse_source - get_messages block: {exc}')

	client.disconnect()


async def parse_sources() -> None:
	try:
		while True:
			print('Парсер запущён...')

			sources = await get_sources()

			start = time.time()

			for source in sources:
				await parse_source(source.username)
				await sleep(240)

			total = time.time() - start

			print(f'Всё ({len(sources)}) обработалось за {total}с ({(total)/60}м)')
			await sleep(1200)
	except Exception as exc:
		logging.error(exc)
