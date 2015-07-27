from datetime import datetime
import mds

def get_flags(conn, name=None):
	q = conn.session.query(mds.Flag).\
		filter(mds.Flag.deleted.is_(None))
	if name is not None:
		q = q.filter(mds.Flag.name == name)
	return q.all()

def get_flags_by_id(conn, id=None):
	q = conn.session.query(mds.Flag).\
		filter(mds.Flag.deleted.is_(None))
	if id is not None:
		q = q.filter(mds.Flag.id == id)
	return q.all()

def get_flag(conn, name, env):
	e = conn.session.query(mds.Env).\
		filter(mds.Env.name == env).\
		filter(mds.Env.deleted.is_(None))
	existing = e.first()
	env_id = None
	if existing is not None:
		env_id = existing.id
		q = conn.session.query(mds.Flag).\
			filter(mds.Flag.name == name).\
			filter(mds.Flag.env_id == env_id).\
			filter(mds.Flag.deleted.is_(None))
		return q.all()

def delete_flag(conn, name, env):
	e = conn.session.query(mds.Env).\
		filter(mds.Env.name == env).\
		filter(mds.Env.deleted.is_(None)).first()
	q = conn.session.query(mds.Flag).\
		filter(mds.Flag.name == name).\
		filter(mds.Flag.env_id == e.id).\
		filter(mds.Flag.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_flag_by_id(conn, id):
	q = conn.session.query(mds.Flag).\
		filter(mds.Flag.id == id).\
		filter(mds.Flag.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_flag(conn, name, env_id=None):
	f = mds.Flag(name=name, env_id=env_id)
	conn.session.add(f)
	conn.session.commit()
