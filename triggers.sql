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
end;
|
delimiter ;

delimiter |
create trigger OwnerCheck
after delete on clubs_club
for each row
begin
if (select count(*) from clubs_club where owner_id = old.owner_id) = 0 thenauth_user_groupsauth_user_groups
delete from auth_user_groups
where user_id = old.owner_id;
end if;
end;
|
delimiter ;
