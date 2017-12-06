Our project was implemented with Python, HTML, Flask, Jinja, and SQL. We wanted our website to be modern and user-friendly, as reflected in design choices. We also themed the website to be blue and orange, our school's colors. 

We used an SQL database to store data, through both storing reviews in the database and through retrieving reviews in order to be displayed. It was also used to store user info (username and passwords), as well as the list of classes and teachers so that correct combinations could be selected when reading/viewing reviews.

In the HTML documents, we used tables to display the reviews stored within the SQL database. Using CSS, we were able to style the tables with orange and blue backgrounds to represent our school spirit! Additionally, we used Jinja for-loops to iterate through the reviews in the SQL database and display them within the tables. Our HTML files also allowed us to have an interactive navigational bar that reacts to when the user hovers over certain options. We were also able to display our school spirit by including our school's logo throughout the site, and to display the lovely dolphin sketch every time the user has an error.

Python was used to create the different app routes for navigating the site, as well as determining which sites are only accessible through logging in. If you are not a registered user, you can view reviews submitted in the past, but not make any of your own. You're also able to access the register page, but obviously cannot log in until an account is made.

We also used most of the helpers.py file from PSET 7 to have the same functionality as the Finance website, which was a huge inspiration for the design of our own site

We tried using Google App Engine to store our data (Datastore) and to run the site, but eventually decided SQL and Flask were simpler to implement.
