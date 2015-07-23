CREATE TABLE IF NOT EXISTS repotypes(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(20),
	expired DATE,
	PRIMARY KEY ( id )
) ENGINE=INNODB;

INSERT INTO repotypes ( 'name' ) VALUES ( 'artifactory' );
