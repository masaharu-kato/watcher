
CREATE DATABASE location_db;

USE location_db;

CREATE TABLE location_log (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `datetime` DATETIME NOT NULL,
    `x` DOUBLE NOT NULL,
    `y` DOUBLE NOT NULL
);

CREATE USER location_db_user_inserter IDENTIFIED BY 'heiKeenei0Qui9pi';
GRANT INSERT ON location_log TO location_db_user_inserter;

CREATE USER location_db_user_reader IDENTIFIED BY 'aetoeLeexeeVah6u';
GRANT SELECT ON location_log TO location_db_user_reader;
