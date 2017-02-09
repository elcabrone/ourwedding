drop table if exists users;
create table users (
	UserID integer primary key autoincrement,
	name varchar(255),
	pw varchar(255)
);

drop table if exists milestones;
create table milestones (
	MID integer primary key autoincrement, 
	activity varchar(255), 
	schedule varchar(255), 
	location varchar(255), 	
	User int
);