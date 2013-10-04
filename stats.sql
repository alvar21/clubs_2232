create table stats_users (number int);
insert into stats_users values (0);
create table stats_clubs (clubtype varchar(50), number int);
create table stats_membersperclub (clubid int, clubname varchar(50), number int, FOREIGN KEY (clubid) references clubs_club(id));

