from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base

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

	def setup_connection(self):

		db = 'mysql://jenkins:jenkins@qa-mds1.cs4kcrm7ceog.us-east-1.rds.amazonaws.com/mds'
		self.engine = create_engine(db)
		Session = sessionmaker(bind=self.engine)
		self.session = Session()
		self.metadata = MetaData(self.engine)

class Env(Base):
	__tablename__ = 'envs'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	expired = Column(Date)

	def __repr__(self):
		return "<Env(id='%d', name='%s', expired='%s')>" % (self.id, self.name, self.expired)

class Flag(Base):
	__tablename__ = 'flags'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	env_id = Column(Integer)
	expired = Column(Date)

	def __repr__(self):
		return "<Flag(id='%d', name='%s', env_id='%d', expired='%s')>" % (self.id, self.name, self.env_id, self.expired)

class Repotype(Base):
	__tablename__ = 'repotypes'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	expired = Column(Date)

	def __repr__(self):
		return "<Repotype(id='%d', name='%s', expired='%s')>" % (self.id, self.name, self.expired)

class Location(Base):
	__tablename__ = 'locations'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	type_id = Column(Integer)
	location = Column(String)
	expired = Column(Date)

	def __repr__(self):
		return "<Location(id='%d', name='%s', type_id='%d', location='%s', expired='%s')>" % (self.id, self.name, self.type_id, self.location, self.expired)

class Artifact(Base):
	__tablename__ = 'artifacts'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	version = Column(String)
	location_id = Column(Integer)
	expired = Column(Date)

	def __repr__(self):
		return "<Artifact(id='%d', name='%s', version='%s', location_id='%d', expired='%s')>" % (self.id, self.name, self.version, self.location_id, self.expired)

class Flagmap(Base):
	__tablename__ = 'flagmap'

	id = Column(Integer, primary_key=True)
	artifact_id = Column(Integer)
	flag_id = Column(Integer)
	value = Column(String)
	expired = Column(Date)

	def __repr__(self):
		return "<Flagmap(id='%d', artifact_id='%d', flag_id='%d', value='%s', expired='%s')>" % (self.id, self.artifact_id, self.flag_id, self.value, self.expired)



