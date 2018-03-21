Project Plan
===

#### URL: [django-reinhardt.herokuapp.com](https://django-reinhardt.herokuapp.com)

## Group

- Name: *Django Reinhardt* (for the [Jazz singer](https://en.wikipedia.org/wiki/Django_Reinhardt))
- Group code: **g-056**
- Students in the group:

| Name         | Email                      | Student id |
|:------------ |:--------------------------:| ----------:|
| Doruk Gezici | ali.gezici@student.tut.fi  | 278090     |
| Ilkka Niemi  | ilkka.niemi@student.tut.fi | 201813     |
| Louis Sugy   | louis.sugy@student.tut.fi  | 273435     |


## Features and implementation

### Mandatory features

*All mandatory features will be implemented first.*

Here are details about some of the features that we will implement (most of the features don't require any further explanation):

- We will extend the class `AbstractUser` to create the `Player` class ;
- The developer will be a player with some privileges, so we will implement `Developer` class with a one-to-one relation to `Player` ;
- Email validation -> Django's Console Backend ;
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
    - GitLab issues board & backlog
- Technology:
    - The game will be made with *ExcaliburJS* library ;
    - The game will be hosted on GitHub pages with SSL ;
    - The store will use *jQuery* JS library ;
    - The store will use *Bootstrap* for a responsive front-end ;
    - The whole project will be deployed on Heroku.


## Timetable

### 1st week (M 12th - M 18th)

- [x] Meet each other, project plan
- [ ] Set up the project

### 2nd week (M 19th - M 25th)

- [ ] JS game

### 3rd week (M 26th - A 1st)

- [ ] User models
- [ ] Signup and login forms & views
- [ ] Game and tag models
- [ ] View to add a new game
- [ ] View to edit a game

**April 1st: JS Game deadline.**

### 4th week (A 2nd - A 8th)

- [ ] Simple page to play a game
- [ ] Advanced features of playing: save & load, scores
- [ ] Search a game
- [ ] Simple developer stats

### 5th week (A 9th - A 15th)

- [ ] Front-end design (responsive)

**April 15th: Testing deadline.**

### 6th week (A 16th - A 22nd)

- [ ] 3rd party login
- [ ] Sharing
- [ ] RESTful API
- [ ] Enhanced dev stats
- [ ] Enhanced game search

**April 22nd: Final submission.**

**April 22nd - 28th: Project demonstrations.**