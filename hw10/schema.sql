drop table if exists entries;
create table entries(
	id integer primary key autoincrement,
	title text not null,
	text text not null);
insert into entries(id, title, text) values('0','title2', 'text2');
insert into entries(id, title, text) values('1','title1', 'text1');