DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
id INTEGER PRIMARY KEY autoincrement,
titulo STRING not null,
texto STRING not null,
data_criacao timestamp null default current_timestamp

);