from mds import *
from datetime import datetime

def delete_env(conn, name):
	q = conn.session.query(Env).\
		filter(Env.name == name).\
		filter(Env.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_env_by_id(conn, id):
	q = conn.session.query(Env).\
		filter(Env.id == id).\
		filter(Env.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_artifact(conn, name, version, location):
	l = conn.session.query(Location).\
		filter(Location.name == location).\
		filter(Location.deleted.is_(None)).first()
	q = conn.session.query(Artifact).\
		filter(Artifact.name == name).\
		filter(Artifact.version == version).\
		filter(Artifact.location_id == l.id).\
		filter(Artifact.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_artifact_by_id(conn, id):
	q = conn.session.query(Artifact).\
		filter(Artifact.id == id).\
		filter(Artifact.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_flag(conn, name, env):
	e = conn.session.query(Env).\
		filter(Env.name == env).\
		filter(Env.deleted.is_(None)).first()
	q = conn.session.query(Flag).\
		filter(Flag.name == name).\
		filter(Flag.env_id == e.id).\
		filter(Flag.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_flag_by_id(conn, id):
	q = conn.session.query(Flag).\
		filter(Flag.id == id).\
		filter(Flag.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_flagmap(conn, artifact_id, flag_id):
	q = conn.session.query(Flagmap).\
		filter(Flagmap.artifact_id == artifact_id).\
		filter(Flagmap.flag_id == flag_id).\
		filter(Flagmap.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_flagmap_by_id(conn, id):
	q = conn.session.query(Flagmap).\
		filter(Flagmap.artifact_id == artifact_id, Flagmap.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_location(conn, name, type):
	t = conn.session.query(Repotype).\
		filter(Repotype.name == type).\
		filter(Repotype.deleted.is_(None)).first()
	q = conn.session.query(Location).\
		filter(Location.name == name).\
		filter(Location.type_id == t.id).\
		filter(Location.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_location_by_id(conn, id):
	q = conn.session.query(Location).\
		filter(Location.id == id).\
		filter(Location.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_repotype(conn, name):
	q = conn.session.query(Repotype).\
		filter(Repotype.name == name).\
		filter(Repotype.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_repotype_by_id(conn, id):
	q = conn.session.query(Repotype).\
		filter(Repotype.id == id).\
		filter(Repotype.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_artifact(conn, name, version, location):
	l = conn.session.query(Location).\
		filter(Location.name == location).\
		filter(Location.deleted.is_(None)).first()
	q = conn.session.query(Artifact).\
		filter(Artifact.name == name).\
		filter(Artifact.version == version).\
		filter(Artifact.location_id == l.id).\
		filter(Artifact.deleted.is_(None))
	existing = q.all()
	if existing is None:
		a = Artifact(name=name, version=version, location_id=l.id)
		conn.session.add(a)
		conn.session.commit()

def update_artifact_flag(conn, artifact_id, flag_id, value=None):
	q = conn.session.query(Flagmap).\
		filter(Flagmap.artifact_id == artifact_id).\
		filter(Flagmap.flag_id == flag_id).\
		filter(Flagmap.deleted.is_(None))
	existing = q.all()
	if existing:
		for row in existing:
			row.value = value
	else:
		fm = Flagmap(artifact_id=artifact_id, flag_id=flag_id, value=value)
		conn.session.add(fm)
	conn.session.commit()
