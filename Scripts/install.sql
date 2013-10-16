create schema clubs;
use clubs;
BEGIN;
CREATE TABLE `django_content_type` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `app_label` varchar(100) NOT NULL,
    `model` varchar(100) NOT NULL,
    UNIQUE (`app_label`, `model`)
)
;
CREATE TABLE `auth_permission` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `content_type_id` integer NOT NULL,
    `codename` varchar(100) NOT NULL,
    UNIQUE (`content_type_id`, `codename`)
)
;
CREATE TABLE `auth_group_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`group_id`, `permission_id`)
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_group` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(80) NOT NULL UNIQUE
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_groups` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL,
    UNIQUE (`user_id`, `group_id`)
)
;
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_user_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`user_id`, `permission_id`)
)
;
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `password` varchar(128) NOT NULL,
    `last_login` datetime NOT NULL,
    `is_superuser` bool NOT NULL,
    `username` varchar(30) NOT NULL UNIQUE,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(30) NOT NULL,
    `email` varchar(75) NOT NULL,
    `is_staff` bool NOT NULL,
    `is_active` bool NOT NULL,
    `date_joined` datetime NOT NULL
)
;
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE `auth_permission` ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
CREATE INDEX `auth_permission_37ef4eb4` ON `auth_permission` (`content_type_id`);
CREATE TABLE `django_admin_log` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `action_time` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `content_type_id` integer,
    `object_id` longtext,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint UNSIGNED NOT NULL,
    `change_message` longtext NOT NULL
)
;
ALTER TABLE `django_admin_log` ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
ALTER TABLE `django_admin_log` ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `django_admin_log_6340c63c` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_37ef4eb4` ON `django_admin_log` (`content_type_id`);
CREATE TABLE `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` longtext NOT NULL,
    `expire_date` datetime NOT NULL
)
;
CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);
CREATE TABLE `clubs_members` (
    `member_id` integer NOT NULL PRIMARY KEY,
    `first_name` varchar(50) NOT NULL,
    `last_name` varchar(50) NOT NULL,
    `address` varchar(200) NOT NULL,
    `email` varchar(50) NOT NULL,
    `facebook` varchar(200),
    `twitter` varchar(50),
    `interests` varchar(200)
)
;
ALTER TABLE `clubs_members` ADD CONSTRAINT `member_id_refs_id_3a1273e8` FOREIGN KEY (`member_id`) REFERENCES `auth_user` (`id`);
CREATE TABLE `clubs_club` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `owner_id` integer NOT NULL,
    `name` varchar(100) NOT NULL,
    `club_type` varchar(50) NOT NULL,
    `number_of_members` integer NOT NULL,
    `recruiting_members` bool NOT NULL,
    `creation_date` date NOT NULL,
    `location_latitude` double precision,
    `location_longitude` double precision,
    `address` varchar(200) NOT NULL,
    `contact_number` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `facebook` varchar(200),
    `twitter` varchar(50),
    `likes` integer NOT NULL,
    `description` varchar(200)
)
;
ALTER TABLE `clubs_club` ADD CONSTRAINT `owner_id_refs_member_id_c0a0d050` FOREIGN KEY (`owner_id`) REFERENCES `clubs_members` (`member_id`);
CREATE TABLE `clubs_membership` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `member_id` integer NOT NULL,
    `club_id` integer NOT NULL,
    `date_joined` date NOT NULL,
    `date_last_paid` date,
    UNIQUE (`member_id`, `club_id`)
)
;
ALTER TABLE `clubs_membership` ADD CONSTRAINT `member_id_refs_member_id_8102ceff` FOREIGN KEY (`member_id`) REFERENCES `clubs_members` (`member_id`);
ALTER TABLE `clubs_membership` ADD CONSTRAINT `club_id_refs_id_044955b4` FOREIGN KEY (`club_id`) REFERENCES `clubs_club` (`id`);
CREATE INDEX `clubs_club_cb902d83` ON `clubs_club` (`owner_id`);
CREATE INDEX `clubs_membership_b3c09425` ON `clubs_membership` (`member_id`);
CREATE INDEX `clubs_membership_887dd7e4` ON `clubs_membership` (`club_id`);
CREATE TABLE `stats_users` (
    `number` integer NOT NULL PRIMARY KEY
)
;
CREATE TABLE `stats_clubs` (
    `club_type` varchar(50) NOT NULL PRIMARY KEY,
    `number` integer NOT NULL
)
;
CREATE TABLE `stats_membersperclub` (
    `club_id` integer NOT NULL PRIMARY KEY,
    `clubname` varchar(50) NOT NULL,
    `number` integer NOT NULL
)
;
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE `stats_membersperclub` ADD CONSTRAINT `club_id_refs_id_46e89926` FOREIGN KEY (`club_id`) REFERENCES `clubs_club` (`id`);
COMMIT;
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
if (select count(*) from stats_membersperclub where club_id = new.club_id) = 0 then
insert into stats_membersperclub values (new.club_id, 
(select name from clubs_club where id = new.club_id),
(select count(*) from clubs_membership where club_id = new.club_id));
elseif (select count(*) from stats_membersperclub where club_id = new.club_id) > 0 then
update stats_membersperclub 
set number = (select count(*) from clubs_membership where club_id = new.club_id)
where club_id = new.club_id;
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
where club_id = old.club_id;
end;
|
delimiter ;

delimiter |
create trigger ClubInsert
after insert on clubs_club
for each row
begin
if (select count(*) from stats_clubs where club_type = new.club_type) = 0 then
	insert into stats_clubs values (new.club_type, 
		(select count(*) from clubs_club where club_type = new.club_type));
elseif (select count(*) from stats_clubs where club_type = new.club_type) > 0 then
	update stats_clubs
	set number = (select count(*) from clubs_club where club_type = new.club_type)
	where club_type = new.club_type;
end if;
end;
|
delimiter ;

delimiter |
create trigger ClubDelete
after delete on clubs_club
for each row
begin
delete from stats_membersperclub
where clubclub_idid = old.id;
update stats_clubs
set number = (select count(*) from clubs_club where club_type = old.club_type)
where club_type = old.club_type;
end;
|
delimiter ;

delimiter |
create trigger UsersNumber
after insert on auth_user
for each row
begin
update stats_users
set number = (select count(*) from auth_user);
end;
|
delimiter ;
