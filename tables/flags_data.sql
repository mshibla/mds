INSERT INTO flags ( name, env_id )
	SELECT
		'tested' AS 'name',
		id
	FROM envs
	WHERE name = 'CI';

INSERT INTO flags ( name, env_id )
	SELECT
		'tested' AS 'name',
		id
	FROM envs
	WHERE name = 'QA';

INSERT INTO flags ( name, env_id )
	SELECT
		'tested' AS 'name',
		id
	FROM envs
	WHERE name = 'Prod';

INSERT INTO flags ( name, env_id )
	SELECT
		'ready_for' AS 'name',
		id
	FROM envs
	WHERE name = 'CI';

INSERT INTO flags ( name, env_id )
	SELECT
		'ready_for' AS 'name',
		id
	FROM envs
	WHERE name = 'QA';

INSERT INTO flags ( name, env_id )
	SELECT
		'ready_for' AS 'name',
		id
	FROM envs
	WHERE name = 'Prod';

INSERT INTO flags ( name, env_id )
	SELECT
		'deployed_to' AS 'name',
		id
	FROM envs
	WHERE name = 'CI';

INSERT INTO flags ( name, env_id )
	SELECT
		'deployed_to' AS 'name',
		id
	FROM envs
	WHERE name = 'QA';

INSERT INTO flags ( name, env_id )
	SELECT
		'deployed_to' AS 'name',
		id
	FROM envs
	WHERE name = 'Prod';

