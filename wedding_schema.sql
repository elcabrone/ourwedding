drop table if exists milestones;
create table milestones (
	MID integer primary key autoincrement, 
	activity varchar(255), 
	schedule varchar(255), 
	location varchar(255)	
);