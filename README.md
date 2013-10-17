#DEPLOYMENT NOTES
- Accessible via: http://secure-plains-7416.herokuapp.com/ 

#TO-DOs 
2. Setup Installation file (Alvar)
3. Deployment to Server (Alvar)
5. Add Users Table to Data Dictionary.txt (Ian)
6. Database Testing List - WIP (Ian and William)
7. Unliking clubs (Alvar)
10. Change Bootstrap used (Alvar)


#Test Check List
### Registration
	- Register as a user of the system (end user registration should only be possible) - PASS
	- Register a club with all details completed - PASS

### Updating club
	- Update club details (as a owner, correct club) - PASS
	- Update club details (as a owner, wrong club, should not be possible) - PASS
	- Update club details (as an administrator) - PASS
	- Update club details as a end user (should not be possible)

### Club deletion
	- Delete a club (as an owner, correct club) - FAIL
	- Delete a club (as an owner, wrong club, should not be possible)
	- Delete a club (as an administrator)
	- Delete club details as a end user (should not be possible)

### Search for club:
	- By name - PASS
	- By club type - PASS
	- By suburb - PASS
	- By town - PASS
	- By city - PASS
	- By postcode - PASS
	- By 'within radius of location' - PASS

### Search for members:
	- By name - PASS

### Membership
	- Join a club which is recruiting members - PASS
	- Join a club which is not recruiting members (should not be possible) - PASS
	- Quit a club not owned by the user - PASS
	- Quit a club owned by the user - PASS (still owner)
	
### Update member profile
	- Changing password - PASS
	- Change/Add details - PASS
	

### Views
	- View a club with all details present - PASS
	- View a member with all details present - PASS
---

##FEATURES
* i. Users are able to create/join/quit a club.
* ii. Once a new club is created, the current user would be the owner.
* iii. Lists members of a club.
* iv. View a member's membership information (last paid, date joined)
* v. Owners are able to edit their members' membership information (last paid)
* vi. Admins are able to edit/delete a club.
* vii. Various statistics provided.
* viii. Co-ordinates can be retrieved from address during club registration automatically.
* ix. Lists the clubs a member has joined (Clubs -> My Clubs).
* x. Admins and owners are able to edit members' info.
* xi. An unauthorised page pops out every time tries to do something outside their given powers.
* xii. If an owner quits a club, he may not be a member of the club, but he will still own the club.
* xiii. Members are able to join a club if the club is recruiting members (the 'join' button should appear)
* xiv. Works on Firefox, Safari (Mac and iOS) 
##Weaknesses
1. Default users (users with username firstname_lastname, inserted via data.sql) are not able to change their usernames.
2. Owners are not able to transfer their ownership.

###Notes:
* i. On creation of a club, the current user will be the owner of the club.
* ii. Some members may not choose to reveal their addresses, so we give them the option to add their address to our databse by editing their information on the member edit page, or to not do so.

##TRIGGERS:
* i. On Members table update, the Users table will be updated correspondingly.
* ii. On membership entry addition, an update to the club's entry in stats_membersperclub table and an update to the number of members who have joined the club will be triggered.
* iii. On membership entry deletion, an update to the stats of current number of users in the database and an update to the number of members of the club will be triggered.
* iv. On club creation, an update to the number of clubs per club type will be triggered.
* v. On club deletion, an update to the number of clubs per club type and a deletion of its entry from stats_membersperclub table will be triggered.
* vi. On user registration, an update to the total number of users will be triggered.

##SIGNALS (django database triggers):
* i. A signal is triggered on creation of a new user to create a member entry with the same id as the primary key of the created user. The first_name, last_name, email correspond as well.
* ii. A signal is triggered on address edition to update the coordinates of the club's location.


