# wyguide

This is our final project for CS50, which takes the idea of Harvard's Q-guide that allows students to rate a class and a professor, and applies it to our high school. As you will notice when running the program, you can log in / register to the site, as well as review and read reviews about courses at Whitney Young. Be careful, because you will get an apology message if you try to select a class and teacher combination that does not exist. For example, Rosemarie Foy + AP Literature and Composition works, but Rosemarie Foy and Honors Biology will not. (She does not teach that class).

WYGuide should be run through the CS50 IDE using Flask. 

In the database provided, we have stored a variety of names of teachers and courses. We have also pre-written some reviews for the classes so that you can see how the reviews are displayed on each page. On the Index page, you will be able to see the average "overall" score for the teachers that have been reviewed. If you click "view reviews", you can view the reviews for a specific class taught by a specific teacher. If you click "Submit a Review", you will be prompted to select which course and teacher, and then fill out a form. These reviews are then stored in the database and will be accessible through the aforementioned means.

A lot of the baseline code in application.py and helpers.py came from pset7 (Finance Stock Trading site) of CS50.
