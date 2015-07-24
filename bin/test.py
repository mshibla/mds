#!/usr/bin/python

import mds

conn = Artifacts.setup_connection()

for row in session.query(Env, Env.name).all():
	print row.Env, row.name
