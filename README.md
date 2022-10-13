# Hangman
[View the Live Project here](https://project3-ahorcado.herokuapp.com/)
![Initial Image](https://res.cloudinary.com/lizac/image/upload/v1665585631/project3-hangman/sizes_fu7p5x.png)
## Table of Contents
+ [List of Features](#list-of-features)
  + [Existing Features](#existing-features)
  + [Future Features](#future-features)
+ [UX/UI](#uiux)
  + [Site Goals](#site-goals)
  + [Target Audience](#target-audience)
  + [User stories](#user-stories)
  + [Flowchart](#flowcharts)
+ [Technologies Used](#technologies-used)
  + [Languages Used](#languages-used)
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
+ [Testing](#testing)
  + [Validator Testing](#validator-testing)
  + [Manual Testing](#manual-testing)
  + [Testing User Stories](#testing-user-stories)
  + [Browser Compatibility](#browser-compatibility)
  + [Debugging](#debugging)
  + [Unfixed Bugs](#unfixed-bugs)
+ [Deployment](#deployment)
+ [Credits](#credits)
  + [Content](#content)
  + [Code](#code)
  + [Media](#media)
+ [Acknowledgements](#acknowledgements)

## List of Features:

### Existing Features:
#### **Welcoming & Let’s play:**
The user enters the webpage and is greeted by a stylised Hangman title page with a gallows below. The user is prompted to play the game.

![Welcome display](https://res.cloudinary.com/lizac/image/upload/v1665584096/project3-hangman/welcomingstart_mcm9nz.png)

#### **Game section:**
The website will automatically begin the game. 
The user is asked to guess the word by entering individual letters.
If the input letter is in the selected word, the user is notified and the letter replaces the underscore. 

![Correct letter display](https://res.cloudinary.com/lizac/image/upload/v1665583896/project3-hangman/in_the_word_dtxxvi.png)

In the case that the user inputs a key that is already displayed among underscores (i.e. already answered correctly), they will receive a message saying the letter is already in use.

![Used letter display](https://res.cloudinary.com/lizac/image/upload/v1665583929/project3-hangman/alreadyguessed_nvwsbq.png)

If the user's input is incorrect (i.e. a letter not in the selected word), the user will be notified and the hangman image develops one segment at a time.

![Incorrect letter display](https://res.cloudinary.com/lizac/image/upload/v1665583911/project3-hangman/not_in_the_word_czbcns.png)

If the user’s input is a character that is not a letter, they will receive a message that it is not a valid input

![Not a letter display](https://res.cloudinary.com/lizac/image/upload/v1665583924/project3-hangman/not_valid_eqvpqq.png)

#### **Game ending:**
The game will be completed when the user fills all the letters in the selected word or when the hangman appears in his entirety. In the event that the user wins, the “you win!” message in the keyboard layout appears.
 
![You win display](https://res.cloudinary.com/lizac/image/upload/v1665585019/project3-hangman/you_win_h8bxw8.png)

When the game completes by reaching the limit of incorrect attempts, a 'game over' ascii art will display below the hangman image.

![Game Over display](https://res.cloudinary.com/lizac/image/upload/v1665585013/project3-hangman/gameover_rluhnv.png)

#### **Replay section:**
The user has the option to replay the game or to exit the application.
If the user selects “Y” the application starts the game again.
If the user selects “N” or another character other than Y, the game ends and displays a goodbye message.

![Goodbye display](https://res.cloudinary.com/lizac/image/upload/v1665585248/project3-hangman/goodbye_aalg9r.png) 

[Back to Top](#hangman)

### Future Features:
- Option to select a game with words relating to a chosen theme.
- Customisation - Create displays through HTML and CSS.
- Interface development - option to view available letters or used letters.
- Personalisation - username creation.

## UI/UX:
### Site Goals:

This website is designed to allow the user to access an easy to play and educational word based guessing game. This has been achieved using the classic Hangman layout.

### Target Audience:

This website functions as a simple word based guessing game for anyone who would like to test their knowledge and expand their vocabulary. 

[Back to Top](#hangman)

### User Stories:

- As a user, I want clarity of what I am seeing on the application.
- As a user, I want education as well as a challenge in a quiz.
- As a user, I want an easy to navigate interface.
- As a user, I want a clear indication when I choose an incorrect or correct answer.
- As a user, I want to have the choice to play again.
- As a user, I want to have the choice to end the game.

### Flowcharts:

Flowcharts created in the designing UX/UI stage:
![Flowcharts](https://res.cloudinary.com/lizac/image/upload/v1665488284/project3-hangman/White_Minimal_Flowchart_tf5lv3.png)

[Back to Top](#hangman)

## Technologies Used

### **Languages Used:**
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

[Back to Top](#hangman)


## Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/):
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub](https://github.com/):
    - GitHub is used to store the project's code after being pushed from Git.
3. [Canva](https://canva.com/):
    - Canva was used to create the flowcharts during the design process.
4. [Am I responsive?](https://ui.dev/amiresponsive?url=https%3A%2F%2Fbytes.dev):
    - This application was used for visualization of the application on diferent devices.
5. [Cloudinary](https://cloudinary.com/):
    - Cloudinary was used to store and link the images.
6. [Heroku](https://dashboard.heroku.com/) 
    - Heroku was used for deployment, the specification is in the deployment section.
7. The Code Institute's GitHub full template for Python is used in order for the program to display properly in the deployed site on Heroku.

[Back to Top](#hangman)

## Testing

#### **Validator Testing:**
In the process of validating the project, the validator pep8 was unfunctioning. I saw the recommendation on student support to use the pycodestyle built in the workspace on gitpod. Below are the screenshots of the results. The code is too long and the white spaces mensages are due to the ASCII art. This doesn't present significant issues and I couldn't change this due to lack of time.
![tooloong](https://res.cloudinary.com/lizac/image/upload/v1665657667/project3-hangman/line_to_loong_ascii_jq4rvf.png)
![whitespaces](https://res.cloudinary.com/lizac/image/upload/v1665657677/project3-hangman/white_spaces_bodyparts_idtwhc.png)

#### **Manual Testing:**
|  Feature | Expectation | Action | Result|
|-------------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------------------------------|
| **Welcoming & Start** | Welcome message and game will open automatically | Open the game app | Welcome & Game opened automatically|
| **Choose a Letter** | The letter selected will apear and return a value if it is the correct answer or not.| Input a letter | A message will appear saying if  the letter is correct or incorrect|
| **Choosing a caracter that is not a letter** | If the input is not a letter, the user can't send it| Invalid input | The character apears that is not valid|
| **Play again** | If the user selects “Y” the game starts again| Start again the game| The game starts again |
| **End Play** | If the user selects “N” or another character other than Y, the game will end| End the game| The game ends and a goodbye message appears |

[Back to Top](#hangman)

#### **Testing User Stories:**
Results:
- As a user, the game is very straightforward and easy to play. 
- As a user, the selection of english words introduces me to a wider vocabulary.
- As a user, the linear and consistent webpage is easy to navigate. 
- As a user, I can see if my chosen letter is a correct or incorrect answer.
- As a user, I am free to play again.
- As a user, I can choose to end the game.

#### **Browser Compatibility:**
The website has had manual tests conducted on the below browsers and no errors were detected.
- Google Chrome
- Microsoft Edge
- Safari
- Firefox

#### **Debugging:**
The underscore was spaced correctly, but the letters of the word appeared in the wrong order. I solved this by eliminating the space between the underscore.

#### **Unfixed Bugs:**

No unfixed bugs that I'm aware of.

[Back to Top](#hangman)

## Deployment
The site has been deployed through Heroku.
The site has been developed on GitPod, committed and pushed to GitHub. Heroku will update automatically once the site is deployed. 

Deployment Heroku proccess:
1. Log in Heroku. 
2. Click in the "New" button in the top right.
3. Select "Create New App"
4. Choose a name to the App and choose a region.
5. Click in "Create App" button.
6. You must then create a Config Var called PORT. Set this to 8000.
7. When you create the app, you will need to add two buildpacks from the Settings tab. Select  "Add Buildpacks". 
8. Add Python and save, do the same for Node.js, in that order. Python must show first in the list.
The ordering is as follows:
    1. heroku/python
    2. heroku/nodejs
9. Go to Deploy in the nav bar. In Deployment Method, select GitHub/Connect to GitHub.
10. In Connect to GitHub, write the repository name and click in search.
11. Once the route for the repository appears under the search, click the "Connect" button.
12. The deployment can be Manual or Automatic, select your preference. Automatic has the advantage of updating your deployed site as you push the commit in GitHub.
13. Verify that "Branch to deploy" is master/main.
14. Click Deploy and the link with live project will appear. [View the Live Project here](https://project3-ahorcado.herokuapp.com/)

- The link to access [this repository](https://github.com/lizac9/project3-hangman). 
- The steps to "[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)" the repository. 
- The steps to "[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)" the repository.

[Back to Top](#hangman)

## Credits

#### **Content:**
The words chosen were randomly selected.

#### **Code:**
External resources relevant to this code:
- How to pick a random english word from a list: https://stackoverflow.com/questions/594273/how-to-pick-a-random-english-word-from-a-list
- While function https://ellibrodepython.com/while-python
- Hangman with python https://youtu.be/pFvSb7cb_Us
- Hangman https://youtu.be/m4nEnsavl6w
- Code Institute Submitions https://github.com/Code-Institute-Submissions/hangman-2

#### **Media:**
- Ascii Art: https://patorjk.com/

## Acknowledgements
- My mentor, for all their guidance and expertise. 
- Fellow students, for their patience and assistance.
- Code Institute for their support.


[Back to Top](#hangman)