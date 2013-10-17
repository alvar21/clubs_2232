##FEATURES
General
* i. List of all clubs
* ii. List of all members
* iii. List members of a club
* iv. Various statistics 
* v. Search for clubs (location{suburb,town,zipcode,within location}, name, type)
* vi. Search for members
* vii. Using geopy, coordinates are automatically added when a new club is created or the club's address is changed
* viii. An unauthorised page pops out every time someone tries to do something outside their given powers.
* 
USERS
* i. Able to create/join/quit a club (only able to join if club is recruiting)
* ii. Able to view clubs joined (Clubs --> My Clubs)
* iii. Able to view membership information
* iv. Able to edit information (changing password included)
* 
OWNERS
* i. Able to delete/edit own clubs
* ii. Able to edit club members' information
* iii. Able to edit club members' membership information
* iv. Able to kick members out of clubs
*
Admins
* i. Able to delete/edit all clubs
* ii. Able to edit members' information
* iii. Able to edit members' membership information
* iv. Able to kick members out of clubs
*

##Weaknesses
1. Default users (users with username firstname_lastname, inserted via data.sql) are not able to change their usernames.
2. Owners are not able to transfer their ownership.
3. When an owner quits a club, he would still be a owner club.

###Notes:
* i. On creation of a club, the current user will be the owner of the club.
* ii. Some members may not choose to reveal their addresses, so we give them the option to add their address to our databse by editing their information on the member edit page, or to not do so.
* iii. The admin/owner tab only appears when the user is an admin or an owner. (Use admin123//123 to test out these features)

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
* iii. There is a signal to update indexes whenever there new entries or updates to existing entries.

