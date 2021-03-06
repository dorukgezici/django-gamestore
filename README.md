Project Plan
===

#### URL: [django-reinhardt.herokuapp.com](https://django-reinhardt.herokuapp.com)

For the final report, see [final_report.md](final_report.md)

## Group

- Name: *Django Reinhardt* (for the [Jazz singer](https://en.wikipedia.org/wiki/Django_Reinhardt))
- Group code: **g-056**
- Students in the group:

| Name         | Email                      | Student id |
|:------------ |:--------------------------:| ----------:|
| Doruk Gezici | ali.gezici@student.tut.fi  | 278090     |
| Louis Sugy   | louis.sugy@student.tut.fi  | 273435     |


## Features and implementation

### Mandatory features

*All mandatory features will be implemented first.*

Here are details about some of the features that we will implement (most of the features don't require any further explanation):

- We will extend the class `AbstractUser` to create the `User` class ;
- The developer will be a user with some privileges, so we will have a `is_developer` BooleanField on our `User` class ;
- Email validation -> Gmail SMTP Server ;
- For communication with games, we will have `Score` and `GameState` models for leaderboard & saving/loading ;
- We will have `Payment` model to keep track of who buys and owns the games for how much ;
- We will implement a **search function**: keywords, tags ;
- We will have a `Tag` model with a many-to-many relation to `Game` model, so that it makes the search easier ;
- Developer statistics: sales, number of downloads.

### JavaScript Game

We will create a Flappy Bird clone with a bee as the player character instead (ITU's mascot -> Bee).
- Player has only one move, jump. It will be controlled by a tap on the screen, mouse-click or pressing the space button on the keyboard.
- There will be randomized obstacles with a small opening in which the player needs to pass through by jumping & falling.
- Playing the game and staying alive will be hard (Just like regular Flappy Bird).
- The game will implement the API given in the description.
- There will be a leaderboard / high score table.
- The game will be mobile-friendly and screen size will be dynamic.
- We'll use the front-end game development library *ExcaliburJS* for development.


### Extra features

*We will try to implement all optional features if we have enough time.*

Here is a non-exhaustive list of the optional features we are going to implement:

- More visualisation of developer statistics (graphs, control the time range) ;
- Mobile Friendly -> *Bootstrap* ;
- API following REST conventions ;
- 3rd party login: Facebook (*python-social-auth*) ;
- Sharing games: Facebook, Twitter ;


## Methodology and tools

- Agile methods
    - Weekly face-to-face meetings
    - Coding nights
- Project management tools:
    - Features board updated regularly
- Technology:
    - The game will be made with *ExcaliburJS* library ;
    - The game will be hosted on *GitHub pages* with SSL ;
    - The store will use *jQuery* JS library ;
    - The store will use *Bootstrap* for a responsive front-end ;
    - The whole project will be deployed on *Heroku*.


## Timetable

### 1st week (M 12th - M 18th)

- [x] Meet each other, project plan
- [x] Set up & deploy the project

### 2nd week (M 19th - M 25th)

- [x] JS game

### 3rd week (M 26th - A 1st)

- [x] User models
- [x] Signup and login forms & views
- [x] Game and tag models
- [x] View to add a new game
- [x] View to edit a game

**April 5th: JS Game deadline.**

### 4th week (A 2nd - A 8th)

- [x] Simple page to play a game
- [x] Advanced features of playing: save & load, scores
- [x] Search a game
- [x] Simple developer stats

### 5th week (A 9th - A 15th)

- [x] Front-end design (responsive)

**April 15th: Testing deadline.**

### 6th week (A 16th - A 22nd)

- [x] 3rd party login (Facebook)
- [x] Sharing (Facebook)
- [ ] Enhanced dev stats -> this feature has been abandoned (not enough time)
- [x] Enhanced game search

**April 26th: Final submission.**

**April 26th - 28th: Project demonstrations.**


## Some retrospective notes

We are quite happy with how the development went.
Though we were only two people working in this project, since the third guy said he felt overwhelmed by the workload and then stopped replying to the messages, we have been able to implement most of the extra features listed in our early project plan.

Concerning project management tools, we didn't use the online tools as we met physically, we just used a board of the next features to implement, and checked them while coding, and when all features were implemented we decided the next ones with the project plan and the advancement of the project.
A huge part of the work has been done while working in the same room, and some parts individually.

Concerning the repartition of the work, it has been quite equal, though some parts have been mostly done by one of the teammates: Doruk was more comfortable implementing features like email verification, third-party authentication, API, thanks to previous experience, and Louis made most of the game, also thanks to some experience in game development.


## Testing the game store

There shouldn't be any problem to test the game store. You can create an account, either as a developer or normal account (this can be changed later into developer account), and then purchase and play games, or even add some if you are a developer. The interface is easy to use so it shouldn't be a problem.
You can play with the features like the advanced search: try out different combinations and parameters.

More information about the features in [final_report.md](final_report.md).
