import os
import logging

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import RedirectResponse

from telethon import TelegramClient

from data.config import APP_URL, TG_API_ID, TG_API_HASH, \
	ADMIN_LIST


router = APIRouter()


@router.post(f"/{APP_URL}/upload/")
async def handle_form(
	request: UploadFile = File(None),
	save: str = Form(None),
	test: str = Form(None)
):
	if save:
		if request:
			file_location = os.path.join('data', 'userbot.session')

			with open(file_location, "wb+") as file_object:
				file_object.write(request.file.read())

		return RedirectResponse(f'/{APP_URL}/userbot', status_code=303)

	if test:
		try:
			async with TelegramClient(
				'data/userbot', TG_API_ID, TG_API_HASH, system_version='4.16.30-vxCUSTOM'
			) as client:
				for admin in ADMIN_LIST:
					channel_entity = await client.get_entity(admin)
					await client.send_message(channel_entity, 'Привет! Я в порядке!')
		except Exception as exc:
			logging.error(exc)

		return RedirectResponse(f'/{APP_URL}/userbot', status_code=303)
