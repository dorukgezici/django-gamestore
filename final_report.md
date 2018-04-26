TIE-23506 Web Software Development
 
Spring 2018 course project  
Online game store for JavaScript games

- Group code: **g-056**
- Students in the group:

| Name         | Email                      | Student id |
|:------------ |:--------------------------:| ----------:|
| Doruk Gezici | ali.gezici@student.tut.fi  | 278090     |
| Louis Sugy   | louis.sugy@student.tut.fi  | 273435     |
 

---

Give enough information for the grading to happen based on your report. For features, name the modules, filenames, models, function, views etc. that are involved. As the time allocated for the grading is limited, only reported features will be checked.

## Generic requirements  
#### Valid CSS and HTML
We have tested the HTML with [W3 Nu Html Checker](https://validator.w3.org/nu/). It helped us solve some issues like multiple time the same id because of loops, empty properties, etc.
The code is not 100% valid because of some Django plugins and because of spaces in Heroku paths.

We have checked the CSS with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) without any issue.

#### The service should work on modern browsers
We have tested the service on the following browsers without any issue:

 - Google Chrome on Windows
 - Firefox on Windows and Android
 - Safari on MacOS X

#### Code should be commented well
How does your code reflect this aspect? Give examples!

#### Write your own code
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

## Signs of quality
#### Reusability
Though we have not made extensive use of division into components (except for a separate app for API), individual fragments of code can easily be reused since the MTV design pattern divides the code in a practical and logical way.

For example, one might want to implement a website with an advanced search feature, they can use almost directly the pieces of the template and the view related to this feature, just changing some names of fields to adapt to other objects.

#### Modularity
The code follows strictly the MTV design pattern and the DRY principles.
Therefore features can be added without any changes, and changes in the existing code generally imply very few modifications (the only sensible part being models, altering them can obviously break features).

#### Versatile use of Django’s features

 - The views are class-based views (`ListView`, `DetailView`, `FormView`, `CreateView`, `UpdateView`, etc)
 - The authentication system is a builtin (we extend `AbstractUser` class)
 - We use template inclusion to have consistent style, follow DRY principle and reduce amount of code
 - We use some plugins for extra features and better user experience

#### Sensible URL scheme
The URL scheme is organized in hierarchical way and is meant to be simple and human readable.

The URL of the website leads to the catalog of games which is the most important pages. The other pages are organized in the following way:

 - `admin`
 - `signup`
 - `activate/<key>`
 - accounts
    - `accounts/login`
    - `accounts/logout`
    - `accounts/reset-password`
    - `accounts/reset-password-done`
    - `accounts/reset-password-confirm/<uidb64>/<token>`
 - profile
    - `profile/<pk>`
    - `profile/switch-to-developer`
 - game
    - `game/<pk>`
    - `game/add`
    - `game/update/<pk>`
    - `game/delete/<pk>`
 - tag
    - `tag/add`
 - payment
    - `payment/success`
    - `payment/cancel`
    - `payment/error`

####  Security
The authentication system provided by Django is quite secure. Access rights are checked in the views, and forms include a session token.

Django also protects against SQL injections, XSS, DDoS, etc.

####  Crash & idiot proof
Not saying that our friends are idiots, we did let friends try the store to see if something was not clear or if they could break some features.

In case you try to access a resource you're not allowed to (for example if somebody shared the url of a game you don't own), an error page will be displayed.

#### Testing your game store
We first tested all the main use cases of our system, and then, as explained in the point above, we gave the link to a few friends to have feedback and report bugs.
 

## Minimum functional requirements (mandatory)

#### Register as a player and developer
All users share the model `User` which inherits from `AbstractUser`. This model has a boolean field `is_developer`.

The registration is done in the view `RegistrationView`, the template is in `gamestore/templates/registration/signup.html`. Third-party registration is done with app `social_django`.
 
### Authentication (mandatory, 100-200 points)
The authentication uses Django's authentication system, the template is overriden in `gamestore/templates/registration/login.html`. Third-party authentication is done with app `social_django`.

#### Login, logout and register, both as player or developer
Cf points above about registration and authentication.

#### Email validation (max. +100 points)
Email validation is done through the app `simple_email_confirmation`. The class `User` inherits `SimpleEmailConfirmationUserMixin` and implements a method `get_token`.

Email validation is present but we didn't restrict features to validated accounts because we understand that testers would like to be able to use a fake email to avoid spam.
 
### Basic player functionalities (mandatory, 100-300 points)
We have implemented all the features and made it a lot better than what was expected, so we think we should get 300 points.

#### As a player: how do players find games in your game store (are they in a category, is there a search functionality, etc.?)
The main page of the game store contains a dropdown with a form. The form allows to:

 - filter games by keywords
 - filter games by tags
 - filter games by maximum price
 - sort games by
    - most recent first
    - cheapest first
    - alphabetic order

Filtering games modify the url so you can share a search to a friend or bookmark it.

Games are then displayed in a responsive grid with the following information :

 - title
 - price
 - cover picture (there is a default cover if left empty)
 - tags
 - developer name
 - price and button to purchase if not owned, "play" button otherwise

The catalog also contains a pagination system, which divides the result in pages of 12 games (because the number of columns can be 1, 2, 3 or 4). A range 3 pages is displayed in a widget at the bottom, and buttons for the next and previous ones if they exist.


This view has been implemented in `IndexView`, inheriting from Django's `ListView`. The search system is implemented in method `get_queryset` which filters the results according to the GET parameters.
Additional data used by the template is provided in method `get_context_data`.

#### As a player: buy games (communication with Simple Payments, payment process verification)
When the user clicks the "pay ...€" button, the service Simple Payments is opened, and then the user sees a message confirming that the payment was a success, with a button redirecting to homepage.
Payment status is implemented in the view `payment_view`.

#### As a player: play games
The game views allows a user to play a game, see the high scores, and share the game on social media. If the developer of the game accesses this page, they see a button to edit the game.

If the game sens a correct `SETTING` message, the game will be *fully responsive*, even if the original game page has a fixed size. If no such message is received, arbitrary size is chosen.

#### As a player: see game high scores and record their score
The scores are recorded when the game sends them to the store, and displayed on the game page. The best scores are displayed and a button allows to show a modal window with all scores in a scrollable area.

Currently, the page needs to be reloaded to have the last scores (we would have changed that with AJAX with more time).

#### As a player: Security restrictions, e.g. player is only allowed to play the games they’ve purchased
The player is only allowed to play the games they have purchased (cf `GameView.get`).
 
### Basic developer functionalities (mandatory 100-200 points)
We should get almost all the points, maybe not all because developers statistics miss temporal info.

#### As a developer: Add a game (URL) and set price for that game and manage that game (remove, modify)
How and where in your code was the feature implemented?
#### As a developer: Basic game inventory and sales statistics (how many of the developers' games have been bought and when)
How and where in your code was the feature implemented?
#### As a developer: Security restrictions, e.g. developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory, etc.
How and where in your code was the feature implemented?
 
### Game/service interaction (mandatory 100-200 points)
How many points your group thinks the implementation is worth?
#### Submitting high score's from the game using PostMessage
How and where in your code was the feature implemented?
#### Implementation of PostMessages from service to the game  
How and where in your code was the feature implemented?
 
### Quality of Work (mandatory 100-200 points)  
How many points your group thinks the implementation is worth?
#### Quality of code (structure of the application, comments)
How does your code reflect this aspect? Give examples!
#### Purposeful use of framework (Don't-Repeat-Yourself principle, Model-View-Template separation of concerns)
How does your code reflect this aspect? Give examples!
#### User experience (styling, interaction)
How does your code reflect this aspect? Give examples!
#### Meaningful testing
How does your code reflect this aspect? Give examples!
 
## Non-functional requirements (mandatory 100-200 points)
How many points your group thinks the implementation is worth?
 
This covers your project plan (part of final grading, max. 50 points), as well as : "overall documentation, demo, teamwork, and project management as seen from the history of your GitLab project (and possible other sources that you submit in your final report)".  
 
You point out outstanding features of your project here. Much of this can be gathered from the project plan and repository statistics.
 
## Own JavaScript game(s) (mandatory 100-300  points)
How many points your group thinks the implementation is worth?
#### Your game(s) communicate with the service (the game has to use at least these three service features: high score, save, load)
How and where in your code was the feature implemented?
#### Technical quality of the game (code, comments, communication with the game store)
How does your code reflect this aspect? Give examples!
#### Non-technical qualities of the game AKA the fun factor
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