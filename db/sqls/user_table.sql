drop table if exists users;
create table users (
	id serial primary key NOT NULL,
	username VARCHAR(50) NOT NULL UNIQUE,
	email VARCHAR(200) NOT NULL UNIQUE,
	password VARCHAR(200) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
