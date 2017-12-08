# cs-385-project

TIC-TAC-TOE Game

requierements: \n
-Install Python
-Install/setup virtualenvwrapper
-Install Django

After installing python, the enviornmental variables, and setting up Django on our cloud instance, we used the command:

`sudo python manage.py runserver 0.0.0.0:80`

to start our server. Port 80 is the only one accesible by the external IP address of the VM instance

Our project is a web based tic-tac-toe application that can be played by multiple users at once. It uses a single server to run our django and media files and a seperate server to run our database. For our web app we decided on using the django web-development package that talks to a server running a mysql database. At the moment we have the website with bare-bones ui and can not properly track player activity. We only recently implemented the database and have not yet begun communicating with it to determine user teams. We have integrated a python Tic-Tac-Toe game script to be run in the Django servers, which now accepts inputs from link based web traffic. 

	One of the issues that we might run into should our website be under heavy load is the non-scalable nature of django. According to Django they can support 432,000 requests per hour without any significant degradation, however by Django doesn’t natively provide many options to support scalability. Currently with Django, each node running a server creates one instance of a game. We believe that with multiple nodes running Django servers and being managed by a load balancer we can scale our project to run multiple games at the same time. With the integration of a database, scaling a single game match can be possible so that multiple nodes can pull data from the database and not have a session rely on just one instance. 
  
	Learning the Django structure was a big challenge for us. Figuring out the web routing in addition with the integration of a python script gave us many hardships and took a long time to understand. Integration of the database and our application is a big roadblock we have faced. Restructuring our program to allow users to choose specific games to join and/or set users into specific teams would be a major step up and is something that would take much longer to implement.
