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

## Generic requirements  
#### Valid CSS and HTML
We have tested the HTML with [W3 Nu Html Checker](https://validator.w3.org/nu/). It helped us solve some issues like multiple time the same id because of loops, empty properties, etc.
The code is not 100% valid because of some Django plugins and because of spaces in Heroku paths.

We have checked the CSS with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) without any issue.

#### The service should work on modern browsers
We have tested the service on the following browsers without any issue:

 - Google Chrome on Windows
 - Firefox on Windows and Android
 - Safari on MacOS X and iOS

#### Code should be commented well
The views and models of the `gamestore` app are commented, and the templates have IDs to be easily readable.

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
We should get 180-190 the points, maybe not all because developers statistics don't present the evolution of sales over time.

#### As a developer: Add a game (URL) and set price for that game and manage that game (remove, modify)
The developer can add a game from the developer dropdown in navbar, which opens the view `GameCreateView` based on template `game_create.html`, and edit it from the edit button on game page and profile view, which opens the view `GameUpdateView` based on template `game_update.html`. This view also allow to delete the game.

The game info includes name, price, cover picture, url and tags.

#### As a developer: Basic game inventory and sales statistics (how many of the developers' games have been bought and when)
The developer can see the statistics through the profile page accessible both from profile dropdown and from developer dropdown. This page is `ProfileView` based on template `profile.html`.

The developer statistics show the number of sales for every game, with a link to the game, and an edit button to access the update view.

#### As a developer: Security restrictions, e.g. developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory, etc.
All these security restrictions are implemented in the view. They prevent both from loading a form that you're not allowed, and making a post request with wrong data like changing the developer of your game to somebody else.
 
### Game/service interaction (mandatory 100-200 points)
We should get all the 200 points as the service is fully implemented and tested with the other groups' games.

Game/service interaction is handled by JavaScript in `gamestore/templates/message_receiver.html` which then uses the app `api`. Some cases will be described below.

#### Submitting high score's from the game using PostMessage
The javascript function `receiveMessage` in `gamestore/templates/message_receiver.html` calls the function `saveGamescore` which uses the API (view `save_gamescore` of the app `api`) to save a score.

The model to save scores is `Score`.

A similar system is used to save game states with the model `GameState`.

#### Implementation of PostMessages from service to the game  
As messages from game to service, the messages from service to game are also handled with JS in `gamestore/templates/message_receiver.html`, and use the `api` app to access data if needed (when loading a previously saved gama state for example).
 
### Quality of Work (mandatory 100-200 points)  
We should get 175-200 points for a good use of the framework and a good overall quality of code.

#### Quality of code (structure of the application, comments)
The structure of the application respects the MTV design pattern and DRY principle. Also the html and css are separated, except for some exceptional properties in the html. The REST API has been written as a separate app.

The views and models are commented, and we have used IDs in the templates to make them very understandable.

#### Purposeful use of framework (Don't-Repeat-Yourself principle, Model-View-Template separation of concerns)
There's nothing more to add to what's been said previously. The code is written according to DRY principle and MTV design pattern.

There's no point in using [proof by example](https://en.wikipedia.org/wiki/Proof_by_example) here.

#### User experience (styling, interaction)
User-experience has been at the center of our design process. The very intuitive and responsive design, the powerful features (like advanced search), are the proof of this will to enhance user experience.

#### Meaningful testing
There was already a point about testing above. Let's apply the DRY principle to this report.
 
## Non-functional requirements (mandatory 100-200 points)
We think we deserve 175-200 points for teamwork and project management, as we've worked in sprints, divided the workload equally, and made good use of versioning tools.
 
Moreover, as it will be described below, we have made more than what was expected of us.
 
## Own JavaScript game(s) (mandatory 100-300  points)
We think the game is worth 300 points, for respecting all requirements and presenting effort in gameplay, user experience and graphics.

#### Your game(s) communicate with the service (the game has to use at least these three service features: high score, save, load)
The game implements the following service features:
 - `SETTING` in the beginning to send width and height.
 - `SCORE` at the end of every game to send the score.
 - `SAVE` when the personal best score is beaten, to display in game the personal best score.
 - `LOAD_REQUEST` to request to load the personal best score to display it in game.
 - `LOAD` to load the game state from the service.

#### Technical quality of the game (code, comments, communication with the game store)
The game has been realized following the *update method design pattern*: it is divided in scenes which contain actors, and the methods `update` and `draw` of the scene are called by the game engine and call these same methods for the child actors.

More information about how we structured and implemented the game in [its documentation](https://github.com/Nyrio/flappy-bee/blob/master/README.md).

#### Non-technical qualities of the game AKA the fun factor
The game uses only our own assets drawn and animated with Louis' drawing tablet on the free and open source painting software Krita.

The fun factor has been guaranted by watching friends play it and balancing the game well. It can be pretty addictive. Just [see by yourself](https://nyrio.github.io/flappy-bee/).


## Functionality that earns your group extra points
 
#### Save/load and resolution feature (0-100 points)
We should get 100 points for this feature. The implementation was explained previously in this document (JavasScript function, using the API to write and read the model `GameState`).
 
#### 3rd party login (0-100 points)
We should get 80-100 points.

The feature was implemented with the help of the plugin Social Django.
 
#### RESTful API (0-100 points)
We should get 100.

The feature is implemented in the app `api` and is demonstrated on the profile page of a user registered as developer.
 
#### Mobile Friendly (0-50 points)
We should get 50 points (if not more, that's quite a lot of work actually).

This has been made with the help of Bootstrap and personal code (making the game page fully responsive with an iframe on content which can be responsive or fixed size was tough).
 
#### Social media sharing (0-50 points)
We should get 40-50 points.

This feature is available on game view, and has been implemented with the help of the plugin Django Social Share.

####  Some extra special feature your group has implemented (200 points max.)

 - Tags system and cover pictures for games
 - Advanced search and pagination system in game catalog
 - Advanced responsive and intuitive design
 - View of the player's purchases
 - Game showing a lot more effort than most of the others.

---

## TODO 

- open an issue for this report with title "Final report ready"
- assign the newly created issue to WSD-Plussa