from sqlalchemy import Column, Integer, BigInteger, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Setting(Base):
	__tablename__ = 'settings'

	id = Column(Integer, primary_key=True, autoincrement=True)
	sys_name = Column(Text, nullable=False)
	name = Column(Text, nullable=False)
	value = Column(Text, nullable=True)

	def __str__(self):
		return f'#{self.name}'


class Record(Base):
	__tablename__ = 'records'

	id = Column(Integer, primary_key=True, autoincrement=True)
	source = Column(Text, nullable=False)
	tg_id = Column(BigInteger, nullable=False, unique=True)
	publish_datetime = Column(DateTime, nullable=False)

	def __str__(self):
		return f'#{self.id}'


class Source(Base):
	__tablename__ = 'sources'

	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(Text, nullable=False)
	is_active = Column(Boolean, default=False)

	def __str__(self):
		return f'#{self.id} ({self.username})'
