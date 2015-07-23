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