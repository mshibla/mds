from datetime import datetime
import mds

def get_repotypes(conn, name=None):
	q = conn.session.query(mds.Repotype).\
		filter(mds.Repotype.deleted.is_(None))
	if name is not None:
		q = q.filter(mds.Repotype.name == name)
	return q.all()

def get_repotypes_by_id(conn, id=None):
	q = conn.session.query(mds.Repotype).\
		filter(mds.Repotype.deleted.is_(None))
	if id is not None:
		q = q.filter(mds.Repotype.id == id)
	return q.all()

def delete_repotype(conn, name):
	q = conn.session.query(mds.Repotype).\
		filter(mds.Repotype.name == name).\
		filter(mds.Repotype.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_repotype_by_id(conn, id):
	q = conn.session.query(mds.Repotype).\
		filter(mds.Repotype.id == id).\
		filter(mds.Repotype.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_repotype(conn, name):
	r = mds.Repotype(name=name)
	conn.session.add(r)
	conn.session.commit()
