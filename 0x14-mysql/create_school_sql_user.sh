#!/usr/bin/env bash
#A script that creates the MySQL server user holberton_user,(school checker account)
create_user="
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';"
echo "$create_user" | sudo mysql -uroot -p
