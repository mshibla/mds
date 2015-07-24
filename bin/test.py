#!/usr/bin/python

from mds import *

conn = MDS()

for row in conn.session.query(Env, Env.name).all():
	print row.Env, row.name
