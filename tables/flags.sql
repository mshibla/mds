CREATE TABLE IF NOT EXISTS flags(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50),
	env_id INT,
	expired DATE,
	PRIMARY KEY ( id ),
	INDEX env_idx ( env_id ),
	FOREIGN KEY ( env_id )
		REFERENCES envs( id )
		ON DELETE CASCADE
) ENGINE=INNODB;

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'tested' AS 'name',
		id
	FROM envs
	WHERE name = 'CI';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'tested' AS 'name',
		id
	FROM envs
	WHERE name = 'QA';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'tested' AS 'name',
		id
	FROM envs
	WHERE name = 'Prod';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'ready_for' AS 'name',
		id
	FROM envs
	WHERE name = 'CI';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'ready_for' AS 'name',
		id
	FROM envs
	WHERE name = 'QA';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'ready_for' AS 'name',
		id
	FROM envs
	WHERE name = 'Prod';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'deployed_to' AS 'name',
		id
	FROM envs
	WHERE name = 'CI';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'deployed_to' AS 'name',
		id
	FROM envs
	WHERE name = 'QA';

INSERT INTO flags ( 'name', 'env_id' )
	SELECT
		'deployed_to' AS 'name',
		id
	FROM envs
	WHERE name = 'Prod';

