from datetime import datetime
import mds

def get_flagmap(conn, artifact_name=None):
	q = conn.session.query(mds.Flagmap).\
		filter(mds.Flagmap.deleted.is_(None))
	if artifact_name is not None:
		artifact_id = conn.session.query(mds.Artifact).\
			filter(mds.Artifact.name == artifact_name, mds.Artifact.deleted.is_(None)).first().id
		q = q.filter(mds.Flagmap.artifact_id == artifact_id)
	return q.all()

def get_flagmap_by_id(conn, artifact_id=None):
	q = conn.session.query(mds.Flagmap).\
		filter(mds.Flagmap.deleted.is_(None))
	if artifact_id is not None:
		q = q.filter(mds.Flagmap.artifact_id == artifact_id)
	return q.all()

def delete_flagmap(conn, artifact_id, flag_id):
	q = conn.session.query(mds.Flagmap).\
		filter(mds.Flagmap.artifact_id == artifact_id).\
		filter(mds.Flagmap.flag_id == flag_id).\
		filter(mds.Flagmap.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_flagmap_by_id(conn, id):
	q = conn.session.query(mds.Flagmap).\
		filter(mds.Flagmap.artifact_id == artifact_id, mds.Flagmap.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_flagmap(conn, artifact_id, flag_id, value=None):
	fm = mds.Flagmap(artifact_id=artifact_id, flag_id=flag_id, value=value)
	conn.session.add(fm)
	conn.session.commit()
