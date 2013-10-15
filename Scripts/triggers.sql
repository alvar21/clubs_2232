delimiter |
create trigger EditUser
after update on clubs_members
for each row
begin
update auth_user
set first_name = new.first_name, last_name = new.last_name, email = new.email
where id = new.member_id;
end;
|
delimiter ;

delimiter |
create trigger NumberOfMembers1
after insert on clubs_membership
for each row
begin
update clubs_club
set number_of_members = (select count(*) from clubs_membership where club_id = new.club_id)
where id = new.club_id;
if (select count(*) from stats_membersperclub where clubid = new.club_id) = 0 then
insert into stats_membersperclub values (new.club_id, 
(select name from clubs_club where id = new.club_id),
(select count(*) from clubs_membership where club_id = new.club_id));
elseif (select count(*) from stats_membersperclub where clubid = new.club_id) > 0 then
update stats_membersperclub 
set number = (select count(*) from clubs_membership where club_id = new.club_id)
where clubid = new.club_id;
end if;
end;
|
delimiter ;

delimiter |
create trigger NumberOfMembers2
after delete on clubs_membership
for each row
begin
update clubs_club
set number_of_members = (select count(*) from clubs_membership where club_id = old.club_id)
where id = old.club_id;
update stats_membersperclub
set number = (select count(*) from clubs_membership where club_id = old.club_id)
where clubid = old.club_id;
end;
|
delimiter ;

delimiter |
create trigger ClubInsert
after insert on clubs_club
for each row
begin
if (select count(*) from stats_clubs where clubtype = new.club_type) = 0 then
insert into stats_clubs values (new.club_type, 
(select count(*) from clubs_club where club_type = new.club_type));
elseif (select count(*) from stats_clubs where clubtype = new.club_type) > 0 then
update stats_clubs
set number = (select count(*) from clubs_club where club_type = new.club_type)
where clubtype = new.club_type;
end if;
end;
|
delimiter ;

delimiter |
create trigger ClubDelete
after delete on clubs_club
for each row
delete from stats_membersperclub
where clubid = old.id;
update stats_clubs
set number = (select count(*) from clubs_club where club_type = old.club_type)
where clubtype = old.club_type;
end;
|
delimiter ;

delimiter |
create trigger UsersNumber
after insert on auth_user
for each row
begin
update stats_users
set number = (select count(*) from auth_user)
where current = 'void';
end;
|
delimiter ;
