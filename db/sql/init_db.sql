CREATE DATABASE ofpp DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'ofpp'@'localhost' IDENTIFIED BY '#ofpp#';
GRANT ALL PRIVILEGES ON ofpp.* TO 'ofpp'@'localhost';
FLUSH PRIVILEGES;
