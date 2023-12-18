# ARCASECA

Container waitress:
1. `arca`
	-	Chest, Box, Coffin, Cell, Cupboard, Container


2. pedi`seca`
	- Waitress, Waiting woman, Handmaiden

  

## What is it?

Lightweight game server management panel.

  

## Tools

 - frontend/backend:
	 - [django](https://www.djangoproject.com/)
- docker communication
	- [logging drivers plugins](https://docs.docker.com/config/containers/logging/plugins/)
	- [docker package libraryv (python)](https://docker-py.readthedocs.io/en/stable/)

## Front-end
-  web view
	- web sites
		- login
			- User must be always logged in for making changes and see graphs or container list etc.
			- No registration - Administrator manages users.
		- dashboard (Main page)
			- Container list with general information about them.
			- Graphs of hardware usage
		- container view
			- Console of container
			- Detailed Graph of container hardware usage
			- Filesystem?
		- settings
			- Users
				- Password change
				- Two factor authentication
				- Own logs
			- Administrator
				- Log view of all users
				- Admin button that redirects administrator to django admin panel
				- Two factor authentication
	- thoughts
		- No big hardware usage of itself
		- Being able to determine if system will be overloaded (Graphs, etc.)
		- No registrations!!!!

## Back-end
- log system
	- Log **EVERYTHING** 
	- Must be saved locally also (Access without turned on server)
- data collecting
	- MariaDB
	- real-time container mode
- security
	- Salt to hash 
	- Don't import lot of libraries (Potential risk)
- thoughts
	- Try to avoid data or memory, sql leak
	- Need to make backups somehow

## Production
- Its not open-source.

