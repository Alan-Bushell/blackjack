# Blackjack


## A Python command line game
> This application is a Python based blackjack style card game. The game takes the user's name to begin with and then proceeds into the game.

### - By Alan Bushell

### **[Live site](https://blackjack-abushell.herokuapp.com/)**



### **[Repository](https://github.com/Alan-Bushell/blackjack)**

  
## Table of contents


 1. [ Pre-Project Planning ](#plan)  
 2. [ Features Left to Implement ](#left)  
 3. [ Technology used ](#tech) 
 4. [ Testing ](#testing)  
 5. [ Bugs ](#bugs)  
 6. [ Deployment](#deployment)
 7. [ Credits](#credits)
 8. [ Content](#content)  
 9. [ Acknowledgements](#acknowledgements)  


## Flow

<a name="plan"></a>
### Pre-project Planning

> For project 3 I decided I wanted to make a blackjack style python game in the command line. 

Once I decided on this concept I started to work out my flow and used Lucid Chart to create an easy to follow process. I wanted to create this early on so I can understand the logic needed to complete the project and in what order I should approach it from. 

> Please see the below flow chart to better understand the initial design and concept
![Lucid Flow Chart](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/flowchart.png)

### Pre-Planning Structure

### Structure

#### Deck structure
- Suits

- Card numbers

- Face Cards

- Values for cards

For loop over suits and cards to generate deck of 52 cards.

#### Player Structure

- Name

- Player Cards

- Player Card Value

- Player Score

** If player hits and requests additional card then score, cards and value need to be updated**

#### Dealer Structure

- Dealer Cards

- Dealer Hidden Card

- Dealer Logic

** If dealer has 16 on reveal of hidden card, dealer must hit until they exceed 16**


#### Compartitive structure

- If either player or dealer exceeds 21 then they bust and the other wins

- Who ever has a higher score while remaining at 21 or lower wins


<a name="left"></a>

### Additional ideas


<a name="tech"></a>
# Technology Used
### Python

<a name="testing"></a>
# Testing


### Testing Phase

#### Manual Testing

| Test | Result |
|--|--|
|||


#### User tests

 
|Test|Result  |
|--|--|
|||


<a name="bugs"></a>
## **Bugs**

### Identified bug where the clear function does not always work. This bug is still in place and after multiple attempts to rectify this issue it is left unfixed.
> Attempts to fix it involved utilizing different clear options sourced from Stackoverflow, importing os and sys to develop a clear function based on user device.
> While everything worked perfectly in gitpod development space, once deployed to heroku it was not consistent.
> Final attempt to rectify was to contact Code Institute student support but unfortunately a fix could not be found.

### Identified infified bug on adding dealer value to terminal to show running score. To fix this bug the dealers score is not present until the player stands.
> This bug showed the dealers total score including hidden card value while the player had the option to hit or stand. As this would give the player the advantage 
> I decided to remove this visibility until after the player stood and the dealer hidden card was revealed. A more elegant solution would be possible to only show card[0].value but due to time contstraints I was forced to use a more convenient solution.

### Endless loop at the play again functio when player says no and wants to exit game
> This issue caused the player to be stuck in an endless cycle of do you want to play the game again. The error was caused due to a missing break statement which
> has since been fixed. Now when the player decided they do not want to play again the game exits and presents them with a thank you for playing banner.

<a name="deployment"></a>
## Deployment


<a name="credits"></a>
## Credits

Multiple resources used to better understand the logic and flow of a gaming programme in Python.

### Stack Exchange - https://codereview.stackexchange.com/questions/177523/simple-oop-blackjack-game-in-python
> Assisted in understanding the OOP concepts in python when applied to this type of game

### IT guys - https://www.youtube.com/watch?v=8QTsK1aVMI0
> Interesting approach to building a blackjack game with python. - As I progressed through the project I covered off more and more material to help me better understand the core logic of how to implement a blackjack game. The process shown and covered in this material closely matched how I had already built my classes in python and reassured me that I was on the right track throughout.

### Anthony Tapias - https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
> Developing a deck of cards in python using oop. Useful resource to create and instantialise a deck of cards using classes. While I was already successful in doing this through for loops, this resource gave me some inspiration in how to approach the problem in a more efficient oop way.

<a name="content"></a>
## Content & Resources

### w3 schools
> Used to reference Python Structure

### ASCII Art -  https://patorjk.com
> Used to create the ascii art used for this project, mainly the welcome to blackjack banner and the thank you for playing banner.

### ASCIIART.EU - https://www.asciiart.eu/television/futurama
> Used this website for the bender applause ascii for when a user wins a hand.

### Code Institute
> Project created in line with course content and within project 3 scope.

### Stack Overflow
> Used to reference different synthax issues from existing older boards. Also used to query clear function issues when I ran into them as referenced in the terminal bug in the big section.

<a name="acknowlegements"></a>
## Acknowledgements

### Dick Vanderlen
> My mentor in the CI who provided me with great feedback and guidance at the inception of this project.
