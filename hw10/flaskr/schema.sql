drop table if exists entries;
create table entries(
	id integer primary key autoincrement,
	title text not null,
	text text not null
);
insert into entries(id, title, text) values('title1', 'text1');
insert into entries(id, title, text) values('title2', 'text2');