#!/usr/bin/env bash
#A script that creates the MySQL server user holberton_user,(school checker account)
create_dbntable="
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50),
  PRIMARY KEY(id)
);
INSERT INTO nexus6(name) VALUES
  ('Leon'),
  ('Abdul');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';"
echo "$create_dbntable" | sudo mysql -uroot -p
