from datetime import datetime
import mds

def get_envs(conn, name=None):
	q = conn.session.query(mds.Env).\
		filter(mds.Env.deleted.is_(None))
	if name is not None:
		q = q.filter(mds.Env.name == name)
	return q.all()

def get_envs_by_id(conn, id=None):
	q = conn.session.query(mds.Env).\
		filter(mds.Env.deleted.is_(None))
	if id is not None:
		q = q.filter(mds.Env.id == id)
	return q.all()

def delete_env(conn, name):
	q = conn.session.query(mds.Env).\
		filter(mds.Env.name == name).\
		filter(mds.Env.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_env_by_id(conn, id):
	q = conn.session.query(mds.Env).\
		filter(mds.Env.id == id).\
		filter(mds.Env.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_env(conn, name):
	e = mds.Env(name=name)
	conn.session.add(e)
	conn.session.commit()
