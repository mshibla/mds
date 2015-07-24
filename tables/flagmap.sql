CREATE TABLE IF NOT EXISTS flagmap(
	id INT NOT NULL AUTO_INCREMENT,
	artifact_id INT NOT NULL,
	flag_id INT NOT NULL,
	value VARCHAR(20),
	deleted DATETIME,
	PRIMARY KEY ( id ),
	INDEX artifact_idx ( artifact_id ),
	INDEX flag_idx ( flag_id ),
	FOREIGN KEY ( artifact_id )
		REFERENCES artifacts( id )
		ON DELETE CASCADE,
	FOREIGN KEY ( flag_id )
		REFERENCES flags( id )
		ON DELETE CASCADE
) ENGINE=INNODB;