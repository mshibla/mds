CREATE TABLE IF NOT EXISTS repotypes(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(20),
	deleted DATETIME,
	PRIMARY KEY ( id )
) ENGINE=INNODB;

INSERT INTO repotypes ( name ) VALUES ( 'artifactory' );
