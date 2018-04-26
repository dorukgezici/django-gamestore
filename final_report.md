TIE-23506 Web Software Development
 
Spring 2018 course project  
Online game store for JavaScript games

- Group code: **g-056**
- Students in the group:

| Name         | Email                      | Student id |
|:------------ |:--------------------------:| ----------:|
| Doruk Gezici | ali.gezici@student.tut.fi  | 278090     |
| Louis Sugy   | louis.sugy@student.tut.fi  | 273435     |
 

## Filling this final report

In this file, your group reports the features you have implemented, how you implemeted them, and how many points your group thinks the implementation is worth. You have to write a justification for each of the features listed! The feature list is the same as in the course project document.
 
For all the features and different parts of them the following questions (or some permutation of them) has to be answered:
- How and where in your code was the feature implemented?
- How many points your group thinks the implementation is worth?

Give enough information for the grading to happen based on your report. For features, name the modules, filenames, models, function, views etc. that are involved. As the time allocated for the grading is limited, only reported features will be checked.

#### Generic requirements  
###### Valid CSS and HTML
We have tested the HTML with [W3 Nu Html Checker](https://validator.w3.org/nu/). It helped us solve some issues like multiple time the same id because of loops, empty properties, etc.
The code is not 100% valid because of some Django plugins and because of spaces in Heroku paths.

We have checked the CSS with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) without any issue.

###### The service should work on modern browsers
We have tested the service on the following browsers without any issue:

 - Google Chrome on Windows
 - Firefox on Windows and Android
 - Safari on MacOS X

###### Code should be commented well
How does your code reflect this aspect? Give examples!

###### Write your own code
We have written our own code except for some components for extra features which would have been too time-consuming:

 - third party authentication (Social Django)
 - social-media sharing (Django Social Share)
 - email confirmation (Simple Email Confirmation)

We have also used some libraries and plugins:

 - Bootstrap
 - jQuery
 - Cloudinary
 - Ajax Selects
 - Font Awesome

#### Signs of quality
###### Reusability
How does your code reflect this aspect? Give examples!
###### Modularity
How does your code reflect this aspect? Give examples!
###### Versatile use of Django’s features
How does your code reflect this aspect? Give examples!
###### Sensible URL scheme
How does your code reflect this aspect? Give examples!
######  Security
How does your code reflect this aspect? Give examples!
######  Crash & idiot proof
How does your code reflect this aspect? Give examples!
###### Testing your game store
How does your code reflect this aspect? Give examples!
 
#### Mandatory requirements
##### Minimum functional requirements (mandatory)
###### Register as a player and developer
How and where in your code was the feature implemented?
 
##### Authentication (mandatory, 100-200 points)
How many points your group thinks the implementation is worth?
###### Login, logout and register, both as player or developer
How and where in your code was the feature implemented?
###### Email validation (max. +100 points)
How and where in your code was the feature implemented?
 
#### Basic player functionalities (mandatory, 100-300 points)
How many points your group thinks the implementation is worth?
###### As a player: how do players find games in your game store (are they in a category, is there a search functionality, etc.?)
How and where in your code was the feature implemented?
###### As a player: buy games (communication with Simple Paymenents, payment process verification)
How and where in your code was the feature implemented?
###### As a player: play games
How and where in your code was the feature implemented?
###### As a player: see game high scores and record their score
How and where in your code was the feature implemented?
###### As a player: Security restrictions, e.g. player is only allowed to play the games they’ve purchased
How and where in your code was the feature implemented?
 
#### Basic developer functionalities (mandatory 100-200 points)
How many points your group thinks the implementation is worth?
###### As a developer: Add a game (URL) and set price for that game and manage that game (remove, modify)
How and where in your code was the feature implemented?
###### As a developer: Basic game inventory and sales statistics (how many of the developers' games have been bought and when)
How and where in your code was the feature implemented?
###### As a developer: Security restrictions, e.g. developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory, etc.
How and where in your code was the feature implemented?
 
#### Game/service interaction (mandatory 100-200 points)
How many points your group thinks the implementation is worth?
###### Submitting high score's from the game using PostMessage
How and where in your code was the feature implemented?
###### Implementation of PostMessages from service to the game  
How and where in your code was the feature implemented?
 
#### Quality of Work (mandatory 100-200 points)  
How many points your group thinks the implementation is worth?
###### Quality of code (structure of the application, comments)
How does your code reflect this aspect? Give examples!
###### Purposeful use of framework (Don't-Repeat-Yourself principle, Model-View-Template separation of concerns)
How does your code reflect this aspect? Give examples!
###### User experience (styling, interaction)
How does your code reflect this aspect? Give examples!
###### Meaningful testing
How does your code reflect this aspect? Give examples!
 
#### Non-functional requirements (mandatory 100-200 points)
How many points your group thinks the implementation is worth?
 
This covers your project plan (part of final grading, max. 50 points), as well as : "overall documentation, demo, teamwork, and project management as seen from the history of your GitLab project (and possible other sources that you submit in your final report)".  
 
You point out outstanding features of your project here. Much of this can be gathered from the project plan and repository statistics.
 
#### Own JavaScript game(s) (mandatory 100-300  points)
How many points your group thinks the implementation is worth?
###### Your game(s) communicate with the service (the game has to use at least these three service features: high score, save, load)
How and where in your code was the feature implemented?
###### Technical quality of the game (code, comments, communication with the game store)
How does your code reflect this aspect? Give examples!
###### Non-technical qualities of the game AKA the fun factor
Review your own!
 
## Functionality that earns your group extra points
 
#### Save/load and resolution feature (0-100 points)
How and where in your code was the feature implemented?
How many points your group thinks the implementation is worth?
 
#### 3rd party login (0-100 points)
How and where in your code was the feature implemented?
How many points your group thinks the implementation is worth?
 
#### RESTful API (0-100 points)
How and where in your code was the feature implemented?
How many points your group thinks the implementation is worth?
 
#### Mobile Friendly (0-50 points)
How and where in your code was the feature implemented?
How many points your group thinks the implementation is worth?
 
#### Social media sharing (0-50 points)
How and where in your code was the feature implemented?
How many points your group thinks the implementation is worth?

####  Some extra special feature your group has implemented (200 points max.)
If your group has implemented some extra feature(s), they can be considered for extra ponints, if impressive enough.
How and where in your code was the feature(s) implemented?
How many points your group thinks the implementation(s) are worth?

## After you have filled this file 
In your group's GitLab repository:
- add this file as "final_report.md" to the root directory of your group repo
- commit it
- open an issue for this report with title "Final report ready"
- assign the newly created issue to WSD-Plussa

## That’s if for this course project. Now you can high-five and go out to the world as tested Django professionals!