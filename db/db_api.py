from datetime import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from data.config import DATABASE_URL

from db.models import Setting, Record, Source


engine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session = sessionmaker(
	bind=engine,
	class_=AsyncSession,
	expire_on_commit=False
)


async def get_setting(name: str) -> Setting:
	async with async_session() as session:
		res = await session.execute(
			Setting.__table__.select()
			.where(Setting.sys_name == name)
		)
		return res.fetchone()


async def get_record(source: str, tg_id: int) -> Record:
	async with async_session() as session:
		res = await session.execute(
			Record.__table__.select()
			.where(Record.source == source, Record.tg_id == tg_id)
		)
		return res.fetchone()


async def get_sources() -> list[Source]:
	async with async_session() as session:
		res = await session.execute(
			Source.__table__.select()
			.where(Source.is_active == True)
		)
		return res.fetchall()


async def add_record(source: str, tg_id: int) -> None:
	async with async_session() as session:
		new_post = Record(
			source=source,
			tg_id=tg_id,
			publish_datetime=datetime.now()
		)

		session.add(new_post)
		await session.commit()


async def record_exists(source: str, tg_id: int) -> bool:
	return not not await get_record(source, tg_id)
