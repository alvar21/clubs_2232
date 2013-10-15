#TODO
1. UML - Check BCNF/4NF (Alvar)
2. Setup Installation file (Alvar)
3. Deployment to Server (Alvar)
4. Database Testing List - WIP (Ian and William)
5. ##Unliking clubs??

### Registration
	- Register as a user of the system (end user registration should only be possible)
	- Register a club with all details completed.

### Updating club
	- Update club details (as a owner, correct club)
	- Update club details (as a owner, wrong club, should not be possible)
	- Update club details (as an administrator)
	- Update club details as a end user (should not be possible)

### Club deletion
	- Delete a club (as an owner, correct club)
	- Delete a club (as an owner, wrong club, should not be possible)
	- Delete a club (as an administrator)
	- Delete club details as a end user (should not be possible)

### Search for club:
	- By name
	- By club type
	- By suburb
	- By 'within radius of location'
	
### List details of club
	- Name
	- Address
	- Type
	- Location
	- Number of members
	- Creation Date
	- Recruiting members (TRUE/FALSE)
	- Contact (phone number)
	- Facebook page
	- Twitter account (handle)
	- Description
	- List of members of club

### Membership
	- Join a club which is recruiting members
	- Join a club which is not recruiting members (should not be possible)
	- Quit a club not owned by the user
	- Quit a club owned by the user
---

##FEATURES
* i. Users are able to create/join/quit a club.
* ii. Once a new club is created, the current user would be the owner.
* iii. Able to list members of a club (at the club's view)
* iv. Able to view a member's membership information (last paid, date joined)
* v. Owners are able to edit their members' membership information (last paid)
* vi. Admins are able to edit/delete a club.
* vii. Various statistics provided.
* viii. Coordinates can be retrieved from address during club registration automatically.
* ix. Able to list the clubs a member joined.
* x. Admins and owners are able to edit members' info.
* xi. Unauthorised page pops out every time tries to do something outside their given powers.

##Weaknesses
1. Default users (users with username firstname_lastname) are not able to change their usernames.
2. Owners are not able to transfer their ownership.
3. If an owner quits a club, he may not be a member of the club, but he will still own the club.

Notes:
* i. On creation of a club, the current user will be the owner of the club.
* ii. Some members may not choose to reveal their addresses, so we give them the option to add their address to our databse by editing their information on the member edit page, or to not do so.

##TRIGGERS:
* i. There is a trigger that updates the user table correspondingly to the edited member info.
* ii. A trigger activated whenever a membership entry is added into the database. It will update the club's entry in stats_membersperclub table and update the number of members of the club the member joined.
* iii. A trigger activated whenever a membership entry is deleted the database. It will update the stats of current number of users in the database and update the number of members of the club the member left.
* iv. On club creation, there is a trigger to update the number of clubs categorised by their types.
* v. On club deletion, there is a trigger to update the number of clubs categorised by their types and delete its entry from stats_membersperclub table.
* vi. A trigger to update the total number of users when a user is registered.
##SIGNALS:
* vii. A signal to create a member entry with the same id to the primary key of the new user created. The first_name, last_name, email corresponds to the new user's.

##GROUPS:
* i. Owners
* ii. Administrators
* iii. End-users
