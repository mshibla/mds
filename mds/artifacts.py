from datetime import datetime
import mds

def get_artifacts(conn, name=None):
	q = conn.session.query(mds.Artifact).\
		filter(mds.Artifact.deleted.is_(None))
	if name is not None:
		q = q.filter(mds.Artifact.name == name)
	return q.all()

def get_artifacts_by_id(conn, id=None):
	q = conn.session.query(mds.Artifact).\
		filter(mds.Artifact.deleted.is_(None))
	if id is not None:
		q = q.filter(mds.Artifact.id == id)
	return q.all()

def query(conn, artifact_id=None, artifact_name=None, artifact_version=None, env_id=None, env_name=None, location_id=None, location_name=None, location_value=None, repotype_id=None, repotype_name=None, flag_id=None, flag_name=None, flagmap_id=None, flagmap_value=None, verbose=None, command=None):
	"""
	Query artifacts
	"""
	q = conn.session.query(mds.Artifact).\
		filter(mds.Artifact.deleted.is_(None))
	if artifact_id:
		q = q.filter(mds.Artifact.id == artifact_id)
	if artifact_name:
		q = q.filter(mds.Artifact.name == artifact_name)
	if artifact_version:
		q = q.filter(mds.Artifact.version == artifact_version)
	if location_id:
		q = q.filter(mds.Artifact.location_id == location_id)
	if location_name and (repotype_id or repotype_name) and not (location_id):
		if repotype_id:
			l = conn.session.query(mds.Location).\
				filter(mds.Locaiton.deleted.is_(None)).\
				filter(mds.Location.type_id == repotype_id).\
				filter(mds.Location.name == location_name)
			location_id = l.first().id
			q = q.filter(mds.Artifact.location_id == location_id)
		elif repotype_name:
			repotype_id = mds.repotypes.get_repotypes(conn, name=repotype_name)[0].id
			l = conn.session.query(mds.Location).\
				filter(mds.Location.deleted.is_(None)).\
				filter(mds.Location.type_id == repotype_id).\
				filter(mds.Location.name == location_name)
			location_id = l.first().id
			q = q.filter(mds.Artifact.location_id == location_id)
	artifacts = q.all()
	answer = {}
	"""
	Query flags
	"""
	for artifact in artifacts:
		f = conn.session.query(mds.Flagmap).\
			filter(mds.Flagmap.deleted.is_(None)).\
			filter(mds.Flagmap.artifact_id == artifact.id)
		if flag_id:
			f = f.filter(mds.Flagmap.flag_id == flag_id)
		if flag_name and env_id and not flag_id:
			q = conn.session.query(mds.Flag).\
				filter(mds.Flag.name == flag_name).\
				filter(mds.Flag.env_id == env_id).\
				filter(mds.Flag.deleted.is_(None))
			flag = q.first()
			f = f.filter(mds.Flagmap.flag_id == flag.id)
		if flag_name and env_name and not env_id and not flag_id:
			env_id = mds.envs.get_envs(conn, name = env_name)[0].id
			q = conn.session.query(mds.Flag).\
				filter(mds.Flag.name == flag_name).\
				filter(mds.Flag.env_id == env_id).\
				filter(mds.Flag.deleted.is_(None))
			flag = q.first()
			f = f.filter(mds.Flagmap.flag_id == flag.id)
		if flagmap_value:
			f.filter(mds.Flagmap.value == flagmap_value)
		flagmaps = f.all()
		flags = []
		for flagmap in flagmaps:
			flags.append(flagmap.flag)
		answer[artifact.id] = {'artifact': artifact, 'flags': flags}

	return answer

def delete_artifact(conn, name, version, location):
	l = conn.session.query(mds.Location).\
		filter(mds.Location.name == location).\
		filter(mds.Location.deleted.is_(None)).first()
	q = conn.session.query(mds.Artifact).\
		filter(mds.Artifact.name == name).\
		filter(mds.Artifact.version == version).\
		filter(mds.Artifact.location_id == l.id).\
		filter(mds.Artifact.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def delete_artifact_by_id(conn, id):
	q = conn.session.query(mds.Artifact).\
		filter(mds.Artifact.id == id).\
		filter(mds.Artifact.deleted.is_(None))
	for row in q.all():
		row.deleted = datetime.now
	conn.session.commit()

def add_artifact(conn, name, version, location_name):
	l = conn.session.query(mds.Location).\
		filter(mds.Location.name == location_name).\
		filter(mds.Location.deleted.is_(None)).first()
	q = conn.session.query(mds.Artifact).\
		filter(mds.Artifact.name == name).\
		filter(mds.Artifact.version == version).\
		filter(mds.Artifact.location_id == l.id).\
		filter(mds.Artifact.deleted.is_(None))
	existing = q.all()
	if not existing:
		a = mds.Artifact(name=name, version=version, location_id=l.id)
		conn.session.add(a)
		conn.session.commit()

def update_artifact_flag(conn, artifact_id, flag_id, value=None):
	q = conn.session.query(mds.Flagmap).\
		filter(mds.Flagmap.artifact_id == artifact_id).\
		filter(mds.Flagmap.flag_id == flag_id).\
		filter(mds.Flagmap.deleted.is_(None))
	existing = q.all()
	if existing:
		for row in existing:
			row.value = value
	else:
		fm = mds.Flagmap(artifact_id=artifact_id, flag_id=flag_id, value=value)
		conn.session.add(fm)
	conn.session.commit()
