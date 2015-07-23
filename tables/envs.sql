CREATE TABLE IF NOT EXISTS envs(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(10),
	expired DATE,
	PRIMARY KEY ( id )
) ENGINE=INNODB;

INSERT INTO envs ( name ) VALUES ( 'CI' );
INSERT INTO envs ( name ) VALUES ( 'QA' );
INSERT INTO envs ( name ) VALUES ( 'Prod' );
