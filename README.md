#Welcome to clubs_2232
Please visit Setup and Instructions.txt for instructions on how to:
1. Run clubs_2232 remotely
2. Run clubs_2232 locally

##FEATURES
* i.	Users are able to create/join/quit a club.
* ii.	Once a new club is created, the current user would be the owner.
* iii. 	Lists members of a club.
* iv. 	View a member's membership information (last paid, date joined)
* v. 	Owners are able to edit their members' membership information (last paid)
* vi. 	Admins are able to edit/delete a club.
* vii. 	Various statistics provided.
* viii. Co-ordinates can be retrieved from address during club registration automatically.
* ix. 	Lists the clubs a member has joined (Clubs -> My Clubs).
* x. 	Admins and owners are able to edit members' info.
* xi. 	An unauthorised page pops out every time tries to do something outside their given powers.
* xii. 	If an owner quits a club, he may not be a member of the club, but he will still own the club.
* xiii. Members are able to join a club if the club is recruiting members (the 'join' button should appear)
* xiv. 	Works on Firefox, Safari (Mac and iOS) 
* xv. 	Search by club names/types/locations(suburb,town,city,zipcode,within radius)
* xvi. 	Search by members 

##Weaknesses
1. Default users (users with username firstname_lastname, inserted via data.sql) are not able to change their usernames.
2. Owners are not able to transfer their ownership.

###Notes:
* i. 	On creation of a club, the current user will be the owner of the club.
* ii. 	Some members may not choose to reveal their addresses, 
			*	we give them the option to add their address to our databse 
			*	by editing their information on the member edit page, or to not do so.

##TRIGGERS:
* i. 	On Members table update, the Users table will be updated correspondingly.
* ii. 	On membership entry addition, an update to the club's entry in stats_membersperclub table and an update to the number of members who have joined the club will be triggered.
* iii. 	On membership entry deletion, an update to the stats of current number of users in the database and an update to the number of members of the club will be triggered.
* iv. 	On club creation, an update to the number of clubs per club type will be triggered.
* v. 	On club deletion, an update to the number of clubs per club type and a deletion of its entry from stats_membersperclub table will be triggered.
* vi. 	On user registration, an update to the total number of users will be triggered.

##SIGNALS (django database triggers):
* i. 	A signal is triggered on creation of a new user to create a member entry with the same id as the primary key of the created user. The first_name, last_name, email correspond as well.
* ii. 	A signal is triggered on address edition to update the coordinates of the club's location.
* iii. 	A signal is triggered whenever there new entries or updates to existing entries to update search indexes .

