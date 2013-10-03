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
create trigger NumberOfMembers
after insert on clubs_membership
for each row
begin
update clubs_club
set number_of_members = (select count(*) from clubs_membership where club_id = new.club_id)
where id = new.club_id;
end;
|
delimiter ;

