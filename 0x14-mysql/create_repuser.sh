#!/usr/bin/env bash
#A script that creates the MySQL server user replica_user
create_user="
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'betty';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';"
echo "$create_user" | sudo mysql -uroot -p
