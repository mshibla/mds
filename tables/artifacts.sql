CREATE TABLE IF NOT EXISTS artifacts(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50),
	version VARCHAR(30),
	location_id INT NOT NULL,
	expired DATE,
	PRIMARY KEY ( id ),
	INDEX location_idx ( location_id ),
	FOREIGN KEY ( location_id )
		REFERENCES locations( id )
		ON DELETE CASCADE
) ENGINE=INNODB;