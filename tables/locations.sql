CREATE TABLE IF NOT EXISTS locations(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(40),
	type_id INT NOT NULL,
	location VARCHAR(100),
	expired DATE,
	PRIMARY KEY ( id ),
	INDEX type_idx ( type_id ),
	FOREIGN KEY ( type_id )
		REFERENCES repotypes( id )
		ON DELETE CASCADE
) ENGINE=INNODB;