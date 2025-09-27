drop table if exists todo;
create table todo (
	id serial primary key NOT NULL,
	title VARCHAR(100) NOT NULL,
	content VARCHAR(300),
	done BOOLEAN DEFAULT FALSE,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	fdate TIMESTAMP,
	author_id INTEGER REFERENCES users(id) ON DELETE CASCADE
	);