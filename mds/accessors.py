from mds import *

def get_envs(conn, name=None):
	q = conn.session.query(Env).\
		filter(Env.deleted.is_(None))
	if name is not None:
		q = q.filter(Env.name == name)
	return q.all()

def get_envs_by_id(conn, id=None):
	q = conn.session.query(Env).\
		filter(Env.deleted.is_(None))
	if id is not None:
		q = q.filter(Env.id == id)
	return q.all()

def get_flags(conn, name=None):
	q = conn.session.query(Flag).\
		filter(Flag.deleted.is_(None))
	if name is not None:
		q = q.filter(Flag.name == name)
	return q.all()

def get_flags_by_id(conn, id=None):
	q = conn.session.query(Flag).\
		filter(Flag.deleted.is_(None))
	if id is not None:
		q = q.filter(Flag.id == id)
	return q.all()

def get_flag_id(conn, name, env):
	e = conn.session.query(Env).\
		filter(Env.name == env).\
		filter(Env.deleted.is_(None))
	existing = e.first()
	env_id = None
	if existing is not None:
		env_id = existing.id
		q = conn.session.query(Flag).\
			filter(Flag.name == name).\
			filter(Flag.env_id == env_id).\
			filter(Flag.deleted.is_(None))
		return q.all()
		
def get_repotypes(conn, name=None):
	q = conn.session.query(Repotype).\
		filter(Repotype.deleted.is_(None))
	if name is not None:
		q = q.filter(Repotype.name == name)
	return q.all()

def get_repotypes_by_id(conn, id=None):
	q = conn.session.query(Repotype).\
		filter(Repotype.deleted.is_(None))
	if id is not None:
		q = q.filter(Repotype.id == id)
	return q.all()

def get_locations(conn, name=None):
	q = conn.session.query(Location).\
		filter(Location.deleted.is_(None))
	if name is not None:
		q = q.filter(Location.name == name)
	return q.all()

def get_locations_by_id(conn, id=None):
	q = conn.session.query(Location).\
		filter(Location.deleted.is_(None))
	if id is not None:
		q = q.filter(Location.id == id)
	return q.all()

def get_artifacts(conn, name=None):
	q = conn.session.query(Artifact).\
		filter(Artifact.deleted.is_(None))
	if name is not None:
		q = q.filter(Artifact.name == name)
	return q.all()

def get_artifacts_by_id(conn, id=None):
	q = conn.session.query(Artifact).\
		filter(Artifact.deleted.is_(None))
	if id is not None:
		q = q.filter(Artifact.id == id)
	return q.all()

def get_flagmap(conn, artifact_name=None):
	q = conn.session.query(Flagmap).\
		filter(Flagmap.deleted.is_(None))
	if artifact_name is not None:
		artifact_id = conn.session.query(Artifact).\
			filter(Artifact.name == artifact_name, Artifact.deleted.is_(None)).first().id
		q = q.filter(Flagmap.artifact_id == artifact_id)
	return q.all()

def get_flagmap_by_id(conn, artifact_id=None):
	q = conn.session.query(Flagmap).\
		filter(Flagmap.deleted.is_(None))
	if artifact_id is not None:
		q = q.filter(Flagmap.artifact_id == artifact_id)
	return q.all()
