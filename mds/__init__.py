from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class MDS:
	"""
	Main class
	"""

	def __init__(self):
		"""
		Class instantiation
		"""

		self.engine = None
		self.metadata = None
		self.session = None

		self.setup_connection()
		self.setup_tables()

	def setup_connection(self):
		"""
		Create DB session
		"""
		db = 'mysql://jenkins:jenkins@qa-mds1.cs4kcrm7ceog.us-east-1.rds.amazonaws.com/mds'
		self.engine = create_engine(db, echo=True)
		Session = sessionmaker(bind=self.engine)
		self.session = Session()
		""" self.metadata = MetaData(self.engine) """

	def setup_tables(self):
		"""
		Create tables in DB
		"""
		self.metadata = Base.metadata
		self.metadata.create_all(self.engine)

class Env(Base):
	__tablename__ = 'envs'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(10))
	deleted = Column(DateTime, nullable=True)

	def __repr__(self):
		return "<Env(id='%d', name='%s', deleted='%s')>" % (self.id, self.name, self.deleted)

class Flag(Base):
	__tablename__ = 'flags'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	env_id = Column(Integer, ForeignKey("envs.id"), nullable=True)
	deleted = Column(DateTime, nullable=True)

	def __repr__(self):
		return "<Flag(id='%d', name='%s', env_id='%d', deleted='%s')>" % (self.id, self.name, self.env_id, self.deleted)

class Repotype(Base):
	__tablename__ = 'repotypes'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(20))
	deleted = Column(DateTime, nullable=True)

	def __repr__(self):
		return "<Repotype(id='%d', name='%s', deleted='%s')>" % (self.id, self.name, self.deleted)

class Location(Base):
	__tablename__ = 'locations'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(40))
	type_id = Column(Integer, ForeignKey("repotypes.id"), nullable=False)
	location = Column(String(100))
	deleted = Column(DateTime, nullable=True)

	def __repr__(self):
		return "<Location(id='%d', name='%s', type_id='%d', location='%s', deleted='%s')>" % (self.id, self.name, self.type_id, self.location, self.deleted)

class Artifact(Base):
	__tablename__ = 'artifacts'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	version = Column(String(30))
	location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
	deleted = Column(DateTime, nullable=True)

	def __repr__(self):
		return "<Artifact(id='%d', name='%s', version='%s', location_id='%d', deleted='%s')>" % (self.id, self.name, self.version, self.location_id, self.deleted)

class Flagmap(Base):
	__tablename__ = 'flagmap'

	id = Column(Integer, primary_key=True, autoincrement=True)
	artifact_id = Column(Integer, ForeignKey("artifacts.id"), nullable=False)
	flag_id = Column(Integer, ForeignKey("flags.id"), nullable=False)
	value = Column(String(20))
	deleted = Column(DateTime, nullable=True)

	def __repr__(self):
		return "<Flagmap(id='%d', artifact_id='%d', flag_id='%d', value='%s', deleted='%s')>" % (self.id, self.artifact_id, self.flag_id, self.value, self.deleted)

