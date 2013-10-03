BEGIN;
CREATE TABLE `clubs_members` (
    `first_name` varchar(50) NOT NULL,
    `last_name` varchar(50) NOT NULL,
    `address` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `facebook` varchar(200) NOT NULL,
    `twitter` varchar(50),
    `interests` varchar(200)
)
;
CREATE TABLE `clubs_club` (
    `clubID` integer NOT NULL PRIMARY KEY,
    `owner_id` integer NOT NULL,
    `name` varchar(50) NOT NULL,
    `club_type` varchar(50) NOT NULL,
    `number_of_members` integer NOT NULL,
    `creation_date` date NOT NULL,
    `address` varchar(50) NOT NULL,
    `contact_number` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `facebook` varchar(200) NOT NULL,
    `twitter` varchar(50)
)
;
ALTER TABLE `clubs_club` ADD CONSTRAINT `owner_id_refs_memberID_c0a0d050` FOREIGN KEY (`owner_id`) REFERENCES `clubs_members` (`memberID`);
CREATE TABLE `clubs_membership` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `member_id` integer NOT NULL,
    `club_id` integer NOT NULL,
    `date_joined` date NOT NULL,
    `date_last_paid` date NOT NULL
)
;
ALTER TABLE `clubs_membership` ADD CONSTRAINT `club_id_refs_clubID_044955b4` FOREIGN KEY (`club_id`) REFERENCES `clubs_club` (`clubID`);
ALTER TABLE `clubs_membership` ADD CONSTRAINT `member_id_refs_memberID_8102ceff` FOREIGN KEY (`member_id`) REFERENCES `clubs_members` (`memberID`);
CREATE TABLE `clubs_users` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `member_id` integer,
    `username` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL,
    `first_name` varchar(50) NOT NULL,
    `last_name` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `date_registered` date NOT NULL,
    `user_type` varchar(50) NOT NULL
)
;
ALTER TABLE `clubs_users` ADD CONSTRAINT `member_id_refs_memberID_9001ea9d` FOREIGN KEY (`member_id`) REFERENCES `clubs_members` (`memberID`);
CREATE INDEX `clubs_club_cb902d83` ON `clubs_club` (`owner_id`);
CREATE INDEX `clubs_membership_b3c09425` ON `clubs_membership` (`member_id`);
CREATE INDEX `clubs_membership_887dd7e4` ON `clubs_membership` (`club_id`);
CREATE INDEX `clubs_users_b3c09425` ON `clubs_users` (`member_id`);

COMMIT;
