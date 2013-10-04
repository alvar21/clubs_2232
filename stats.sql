create table stats_users (current varchar(50), number int);
insert into stats_users values (current, 0);
create table stats_clubs (clubtype varchar(50), number int);
create table stats_membersperclub (clubid int, clubname varchar(50), number int, FOREIGN KEY (clubid) references clubs_club(id));

