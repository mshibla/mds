from datetime import datetime
import mds

def get_locations(conn, name=None, location=None):
	q = conn.session.query(mds.Location).\
		filter(mds.Location.deleted.is_(None))
	if name is not None:
		q = q.filter(mds.Location.name == name)
	if location is not None:
		q = q.filter(mds.Location.location == location)
	return q.all()

def get_locations_by_id(conn, id=None):
	q = conn.session.query(mds.Location).\
		filter(mds.Location.deleted.is_(None))
	if id is not None:
		q = q.filter(mds.Location.id == id)
	return q.all()

def delete_location(conn, name, type):
	t = conn.session.query(mds.Repotype).\
		filter(mds.Repotype.name == type).\
		filter(mds.Repotype.deleted.is_(None)).first()
	q = conn.session.query(mds.Location).\
		filter(mds.Location.name == name).\
		filter(mds.Location.type_id == t.id).\
		filter(mds.Location.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_location_by_id(conn, id):
	q = conn.session.query(mds.Location).\
		filter(mds.Location.id == id).\
		filter(mds.Location.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_location(conn, name, location, type_id):
	l = mds.Location(name=name, location=location, type_id=type_id)
	conn.session.add(l)
	conn.session.commit()
