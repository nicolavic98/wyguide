# wyguide

This is our final project for CS50, which takes the idea of Harvard's Q-guide that allows students to rate a class and a professor, and applies it to our high school. As you will notice when running the program, you can log in / register to the site, as well as review and read reviews about courses at Whitney Young taught by specific teachers, as a class taught by two different teachers can sometimes mean two very different experiences. You can only create reviews once you are logged in, but you can read reviews regardless of being logged in or not (just not on the index page). Be careful, because you will get an apology message if you try to select a class and teacher combination that does not exist. For example, Rosemarie Foy + AP Literature and Composition works, but Rosemarie Foy + Honors Biology will not. This is because Rosemarie Foy does not teach Honors Biology. 

To get to the site, you can first register on the page, and once you are logged as mentioned before you have access to all the information and permissions on the site, as well as the option to change your password.

WYGuide should be run through the CS50 IDE using "flask run". Make sure you have all of the files and the SQL database, "wyguide.db". 

In the database provided, we have stored a variety of names of teachers and courses. We have also pre-written some reviews for the classes so that you can see how the reviews are displayed on each page. On the Index page, you will be able to see the 10 most recently submitted reviews that have been written. If you click "view reviews", you can view the reviews for a specific class taught by a specific teacher, using the same form as found on "Submit a Review". If you click "Submit a Review", you will be prompted to select which course and teacher, and then fill out a form. These reviews are then stored in the database and will be accessible through the aforementioned means.

A lot of the baseline code in helpers.py and our methods for login/logout/register came from pset7 (Finance Stock Trading site) of CS50, both distribution code and our own submitted portions of that assignment. 

If you have any curiosity as to the color scheme of the site, the short answer is our school colors. The long answer is our being extra, but that is a story for another time :)
