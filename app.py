import asyncio
import logging

from uvicorn import Config, Server

from modules.loader import app
from modules.parser import parse_sources


if __name__ == "__main__":
	try:
		logging.basicConfig(
			filename='app.log',
			format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s \
				[%(asctime)s]  %(message)s',
			level=logging.INFO,
		)

		# Создание нового event loop'а
		loop = asyncio.new_event_loop()

		# Запуск веба
		config = Config(
			app=app,
			host='127.0.0.1',
			port=5000,
			root_path='',
			proxy_headers=True,
			forwarded_allow_ips='*'
		)
		server = Server(config)
		loop.create_task(server.serve())

		print('Веб начал работу...')
		logging.info('The web is running...')

		# Запуск парсера
		loop.create_task(parse_sources())

		print('Бот начал работу...')
		logging.info('The bot is running...')

		loop.run_forever()
	except (KeyboardInterrupt, SystemExit):
		logging.error('Bot stopped!')
	except Exception as exc:
		logging.error(exc)
