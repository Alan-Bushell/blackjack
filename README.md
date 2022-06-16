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


## Game Flow - 
> When the user loads up the game they are presented with the following:

![Begining of game](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/blackjack-home.png)

> The user is then presented with a little menu asking would they like to start the game or read over the rules first.
![Menu](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/menu.png)

> If the user selects the rules this is how it will show:
![Rules](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/rules.png)

> When the player is ready the cardas will be dealt. Here we see the dealers cards first. One hidden card and one shown card:
![Dealer Cards](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/dealers-cards.png)

> When we scroll down we see the players cards with a running total for the player. We do not include a running total for the dealer as he only has one card so for that we know of.
![Players Cards](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/players-cards.png)

> The player is then given the option to Hit or Stand
![Hit or Stand](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/hit-or-stand.png)

> If the player wants to increase their score they can hit and it will look as follows. The player can keep hitting until they choose to stop or until they exceed 21.
![Player Hits](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/player-draws-card.png)

> If the player exceeds 21 that means they have bust and will be shown the following message:
![Player Bust](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/player-bust.png)

> If the player stands at any stage while below 21 it will then shift to the dealers turn. The dealer must hit on 16 or under but stand on 17 or over. If the dealer exceeds 21 they also bust. As seen here:
![Dealer Bust](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/dealer-bust.png)

> If neither the player or dealer busts when the round has finished the programme will determine the winner be checking to see who has the closest to 21 as seen here:
![Check winner](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/none-bust.png)

> If the player is the winner their score in will increase and they will be greeted by a famous robot holding up an applause sign in ascii art as seen here:
![Player Wins](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/win-art.png)

> If the player decides they no longer wish to play again when prompted after the game, they will the be greeted with a thank you message as seen here:
![Thank you](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/thank-you.png)

<a name="left"></a>

### Features left to implement

>I wanted to add a goal for a scoring system. For example: First player to win 10 hands wins the overall game.

> If the player gets a clean sweep. ie wins 10 games without losing then present them with a special secret congratulations message.

> Give the user the ability to place bets

> Give the user the functionality to play multiple hands

> Give the user the ability to spilt their cards if they are dealt two of the same card at the beginning of the game and pay against the dealers cards.

> I really wanted to inject color into the project using colorama and set the traditional red suits to red and leave the black suits as black and white as standard. I also would have liked to add red to errors presented due to invalid entrys and green for success.
Due to personal reasons a decision was made prepare for submission without it due to time constraints.


<a name="tech"></a>
# Technology Used
### Python
Used to create the application


### Heroku
Used to deploy and host the application

### Github
Used to store the code

### Gitpod
IDE used for creating the application

### Git
Used for version control

<a name="testing"></a>
# Testing


### Testing Phase

#### Manual Testing

| Test | Result |
|--|--|
|On run programme the welcome message appears|Pass|
|After welcome message user prompted for name|Pass|
|Once name is input the menu option presents|Pass|
|Selecting 1 from the menu starts the game|Pass|
|Selecting 2 from the menu opens the rules|Pass|
|Dealer hand hidden during first round|Pass|
|When player stands dealer card is shown|Pass|
|When player stands the endgame calculation runs to determin winner|Pass|
|If player wins the player is presented with a win message|Pass|
|If the player wins the ascii art for bender is shown|Pass|
|If the dealer wins the dealer score is incremented|Pass|
|If the dealer wins the player is given a lose message|Pass|
|If the hand is a tie the player is notified|Pass|
|If the hand is a tie, neither player or dealers score increases|Pass|

#### User tests

The following tests are on the error handling throughout the project.
If the error handling works as expected it will be marked as pass.
If it does not work as expected then it will be marked as a fail.
> Enter Name Field
Error Msg: User must enter a name of at least 3 characters and it must be all letters.

| Test | Result |
|--|--|
|User enters a name of less than 3 characters | Pass|
|User tried to enter 3 characters with a number|Pass|
|User tried to enter an empty string|Pass|
|User tried to enter a name with a space in it|Fail|

While I expected the error handling to deal with names of less than 3 characters and only letters, I did not think ahead in case users would want to add multiple word names. For example: 'Handsome Joe'. This will throw an error to the user and advise them of the Error Msg above. 

> Main menu options
Error Msg: Please select 1 to start game or 2 to read the rules

| Test | Result |
|--|--|
|User tried to enter a number other than 1 or 2 | Pass|
|User tried to enter a letter |Pass|
|User tried to enter an empty selection|Pass|
|User tried to enter a special symbol|Pass|

> Hit or stand option
Error Msg: Please enter H to hit or S to stand
As I have the function set to accept the input as .lower() either case style of H(h) or S(s) is considered valid in this programme

| Test | Result |
|--|--|
|User tried to enter a number on hit or stand choice | Pass|
|User tried to enter a letter other than H or S |Pass|
|User tried to enter an empty selection|Pass|
|User tried to enter a special symbol|Pass|

The following tests will show pass if the functionality works as intended or fail if it does not
> Play again option
Error Msg: Please enter Y to play again or any other key to exit

| Test | Result |
|--|--|
|User tried to enter y to play again  | Pass|
|User tried to enter a number to exit|Pass|
|User tried to enter any other letter than y to exit|Pass|
|User tried to enter a an empty string to exit |Fail|

### Pep8 Checker tool

> I used the Pep8 checker tool to validate my python code and ensure it was free from errors. As shown here:

![Pep8](https://github.com/Alan-Bushell/blackjack/blob/main/assets/images/readme/pep8.png)

<a name="bugs"></a>
## **Bugs**

### Identified bug where the clear function does not always work. This bug is still in place and after multiple attempts to rectify this issue it is left unfixed.
> Attempts to fix it involved utilizing different clear options sourced from Stackoverflow, importing os and sys to develop a clear function based on user device.
> While everything worked perfectly in gitpod development space, once deployed to heroku it was not consistent.
> Final attempt to rectify was to contact Code Institute student support but unfortunately a fix could not be found.

### Identified bug on adding dealer value to terminal to show running score. To fix this bug the dealers score is not present until the player stands.
> This bug showed the dealers total score including hidden card value while the player had the option to hit or stand. As this would give the player the advantage 
> I decided to remove this visibility until after the player stood and the dealer hidden card was revealed. A more elegant solution would be possible to only show card[0].value but due to time contstraints I was forced to use a more convenient solution.

### Endless loop at the play again functio when player says no and wants to exit game
> This issue caused the player to be stuck in an endless cycle of do you want to play the game again. The error was caused due to a missing break statement which
> has since been fixed. Now when the player decided they do not want to play again the game exits and presents them with a thank you for playing banner.

### Incorrect score being added to player when they bust.
> Inspected the outcome code for player bust and I incorrectly had the player score to increment instead of the dealer. Fixed this bug and it is now tracking correctly.

<a name="deployment"></a>
## Deployment

####
Navigate to heroku.com & log in.

Click "new" and create a new App.

Give the application a name and then choose your region and Click "Create app".

On the next page click on the Settings tab to adjust the settings.

Click on the 'config vars' button.

Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.

Buildpacks now need to be added. 

These install future dependancies that we need outside of the requirements file.

Select Python first and then node.js and click save. 

**Make sure they are in this order.**

Then go to the deploy section and choose your deployment method. 

To connect with github select github and confirm.

Search for your repository select it and click connect.

You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes. 

For this option choose the branch to deploy and click enable automatic deploys. 

This can be changed at a later date to manual. 

Manual deployment deploys the current state of a branch.

Click deploy branch.

We can now click on the open App button above to view our application.

<a name="credits"></a>
## Credits

Multiple resources used to better understand the logic and flow of a gaming programme in Python.

### [Stack Exchange](https://codereview.stackexchange.com/questions/177523/simple-oop-blackjack-game-in-python)
> Assisted in understanding the OOP concepts in python when applied to this type of game

### [IT guys](https://www.youtube.com/watch?v=8QTsK1aVMI0)
> Interesting approach to building a blackjack game with python. - As I progressed through the project I covered off more and more material to help me better understand the core logic of how to implement a blackjack game. The process shown and covered in this material closely matched how I had already built my classes in python and reassured me that I was on the right track throughout.

### [Anthony Tapias](https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3)
> Developing a deck of cards in python using oop. Useful resource to create and instantialise a deck of cards using classes. While I was already successful in doing this through for loops, this resource gave me some inspiration in how to approach the problem in a more efficient oop way.

<a name="content"></a>
## Content & Resources

### w3 schools
> Used to reference Python Structure

### ASCII Art -  https://patorjk.com
> Used to create the ascii art used for this project, mainly the welcome to blackjack banner and the thank you for playing banner.

### [ASCIIART.EU](https://www.asciiart.eu/television/futurama)
> Used this website for the bender applause ascii for when a user wins a hand.

### Code Institute
> Project created in line with course content and within project 3 scope.

### Stack Overflow
> Used to reference different synthax issues from existing older boards. Also used to query clear function issues when I ran into them as referenced in the terminal bug in the big section.


### Youtube
> One of the best free learning platforms in the world and has I use it every day when coding to help me better understand concepts from different perspectives.

<a name="acknowlegements"></a>
## Acknowledgements

### Dick Vlaanderen
> My mentor in the CI who provided me with great feedback and guidance at the inception of this project.

### My CI Cohort
> My team and cohort leader Kasia have been great to work with. I enjoy our brief chats and the knowledge sharing amongst the group is fantastic.

### Ken Sheridan
> A special shout out to Ken Sheridan. I approached Ken when it was no longer possible for me to book in my remaining mentor sessions due to personal circumstances.

> I wanted to get another set of eyes on my completed project and receive any feedback or opinions regarding the completed project. Ken was right on hand to give my project a good once over and his support is greatly appreciated.
