# dogFriendlyCamping

Dog Cartoon Image - http://clipart-library.com/clipart/dog-clip-art-27.htm
Tent Outline - http://clipart-library.com/tent-outline-cliparts.html
Dog Cartoon Face  - https://www.gograph.com/vector-clip-art/dog-face.html

Edited using Adobe Fireworks

Search Index
Dont forget to add a bit about createing searhc index within gitpod, using python for the campingVenues collection
restricted to the fields venue_name, location, description and tags

Thanks
Mentor
Kevin @ CI Tutor Support for helpign me to get modal to delete correct record, as part of defensive deletion. 

Include added defensive programming for delete

#Standard and Template below 

# Match the Players
![MUFC - Match the Players screen mockups](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/mufcGame_mockup.PNG)

# Purpose
The purpose of this site, is to host a card matching game for Manchester United Fans.
It is intended to demonstrate some of the skills I have learnt, in HTML,CSS, and Javascript to meet the criteria of milestone 2

The game is aimed at all fans, particularly the younger generation of fans. They will match pairs of player images based on the club. The players will be past and present stars.
The idea was inspired by my 10 year old son, who is a Manchester Untied Fan. He selected the players to be included in the game, and was my main tester from a User Experience perspective. 

# Live Site
The live site is published here using github pages - https://cwill83247.github.io/mufccardgame/

# User Experience Design
First Time Visitor Goals
-	As a first time user I need to quickly and easily understand the purpose of the site.
-	As a first time user I need to be able to understand how to play the game.
-	As a first time user I need to be able to view the website clearly on both tablet and mobile, as well as desktop.
-	As a first time user I need to be able to easily play the game, through responsive design.
-	As a first time user I need to be able to find the game intuitive.
-	As a first time user I need to have feedback on how I have done in the game.

Returning Visitor Goals
-	As a returning visitor I want to be able to start the game quickly
-	As a returning visitor I want to find the game equally challenging

# Design
## Structure
The page will have the Manchester United crest at the top of the page in a header div, which will clearly show users the page is about Manchester United. 

Heading 1 will be under the crest, and display the name of the game.  

The left hand block will contain instructions explaining the purpose of the game and how to play the game. It will also contain timer, score information, and buttons to start a new game, and restart the canvas. 

The right hand block will initially display with start game text, this is so the user has time to read instructions, rather than the game start once the page has loaded. On clicking start the card game area will display 12 cards and the timer countdown will begin. 

The score count will update as pairs of games are matched, and provide the user with an indication of how they are doing. 
## Initial design Experience
The page has been designed to initially ensure the focus is on what the game is about. By using the Manchester United crest clearly at the top of the page, and the theme uses the Manchester United colours. 

I have inntentionally not started the game on load, so the user is initially drawn to my left block, to read the instructions on game play, when they are happy they can click start on the right block, or below the left block. 

The cards display initially showing the Manchester United crest to further enhance the purpose of the game.
## Colour Scheme 
The colours used in my design were red #DA291C; black (rgba 0,0,0,0), and white rgb(255, 255, 255). These colours tie in with the Manchester United crest, and the teams identity.

![Colour Pallete](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/colourpallete.png)

## Typography 
The font used was from Google fonts - Bebas Neueu, I felt this reflected the brand clearly and matched the identity of Manchester United.
https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Lobster&display=swap


## Images
The images used in the site, are of Manchester United Players, past and present as selected by my 10 year old son.
 These are players young and old fans  will recognise. The Main Logo is the Manchester United crest which is the identity of the club. 
 
 The images used were obtained from google images, unfortunatley due to the nature of football, none of these images were available under creative commons license. If this was a site, intended for wider consumption , then would need to purchase image rights via a site such as shutterstock.com 

# Responsiveness 
The game is intended to be quick ,and fun for all users, on desktop, Tablet or Mobile. 

The design responds to varying screen sizes, and devices, changing the layout appropriately to ensure its playable on all device formats. 

The blocks will stack on top of each other for tablet and mobile to ensure more user friendly when they don’t have suitable screen sizes. It has been tested manually, and by viewing via Google chrome > inspect option.
# Future developments
-	Rather than have 6 images, would like a bank of 50 images with 6 getting randomly  selected each time a game starts.
-	At the end of the game provide some fact or statistic about Manchester United.
-	Create levels of difficulty, either by having less time to match, or the images are harder to make a match.

# Wireframes
![Desktop Wireframe](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/desktop-wireframe.png)
![Tablet Wireframe](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/tablet-wireframe.png)
![Mobile Wireframe](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/mobile-wireframe.png)


# Deployment
## Github Pages
Deploying site so live using GitHub Pages

1.	Log in to GitHub and locate the GitHub Repository.
2.	Locate the "Settings" option (top of the page).
3.	Click on "Pages" will open "GitHub Pages" Section.
4.	Under "Source", click the dropdown called "None" and select "Main Branch".
5.	The page will automatically refresh.
6.	At the top near github header to locate the now published site link
7. The link can sometime take a while for your site to be live initally so give it 15 minutes and then use the link to see your deployed site.

## Cloning GitHub Repository
1. Log in to GitHub and locate the GitHub Repository. 
2. Under the repository name, click "Clone or download". 
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. 
4. Open Git Bash. 
5. Change the current working directory to the location where you want the cloned directory to be made. 
6. Type git clone, and then paste the URL you copied.

# Testing Tools
The Lighthouse, W3C Markup Validator, JSHint and the Lighthouse report were used to determine whether there were any errors in the code. I ensured standards were met in design, and also accessebility.

-	W3C Markup Validator
-	W3C CSS Validator
-	Lighthouse report
-	JS Hint

![CSS Validation](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/W3C_WSSValidation_pass.PNG)
![Lighthouse Performance](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/LighthouseViewer_Performance.PNG)
![Lighthouse Accessebility](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/LighthouseViewer_Accessebility.PNG)

# Testing User Stories from UX Section
##	First time visitor goals
- As a first time user I need to quickly and easily understand the purpose of the site.
--	The theme of the site is easily identifiable, and the instructions are clearly displayed, the design is clean and simple with focus on the users experience.

-	As a first time user I need to be able to understand how to play the game.
--	The instructions are clearly displayed, and when the page initially loads the focus is on the instructions rather than the game.
![how to play](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/howtoplay.PNG)
-	As a first time user I need to be able to view the website clearly on both tablet and mobile, as well as desktop.
--	The game is easy to play on all screen sizes, and devices ensuring it is enjoyable to play.

- As a first time user I need to be able to find the game intuitive.
-- The game is very intuitive, it is clear it is about Manchester United, and the aim of the game is to match players. Feedback is good from the game.
![game area](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/gamearea.PNG)
- As a first time user I need to have feedback on how I have done in the game.
-- The game clearly shows the counter, counting down, the number of cards matched and at the end of the game provided information on how I have done.
![modal](https://github.com/cwill83247/mufccardgame/blob/main/assets/images/modalpopup.PNG)
## Returning Visitor Goals

- As a returning visitor I want to be able to start the game quickly
-- New game options, and restart options are clearly visible.
![timer and score]("https://github.com/cwill83247/mufccardgame/blob/main/assets/images/timer and score.PNG")
- As a returning visitor I want to find the game equally challenging
-- The cards are always displayed in random positions, so its always equally challenging.

# Further Testing
- The Javascript was run through JSHint to ensure correct with no coding issues
- CSS was run through W3C validation, and successfully passed
- HTML was run through W3C validation, and passed with no errros 
- Test script was created and run, using JEST to test some of the functionality as part of TDD principal.
- Manual testing was carried out, against my user stories.
- Family members tested the game, and gave me feedback. 

Testing has been a continous process, after every commit, the code was tested to ensure the game functioned as expected.

# Errors and Bugs
-When the page loaded the game started straight away not giving the user time to read the instructions. I resolved this by adding a html element that loads initially, and then on clicking start game changes to display the cards.

- Not being able to remove event listeer at appropriate time - added an if statement with the remove event lister as part of script.

- My Son identified that he could double click on a card and it would then match, leaving us then with odd numbers, and not making game very enjoyable.  I resolved this by adding an if statement to check if the id’s matched then not allow the match to take place. 

- During testing I also identified that if no match the 2nd card didn’t display the image, it effectively flipped back immediately. I used setTimout to briefly show both cards, before flipping back.

- Images were displaying a small inserts within the card - this was resolved by changing the padding settigns with the CSS.

- It wasnt very clear when the game had ended for the user i.e they had matched all cards, or time had run out - this was resolved with the use of a modal to overlay the card area, and prpvide feedback to the users.

- Responsiveness provided several challenges, as wanted cards to remain responsive. I used the grid layout to cut down the number of cards shown as the screen size decreased.

# Validation

- HTML - Validator used - https://validator.w3.org/ Passes all test

- Accessibility - Lighthouse Viewer chrome developer tools - https://developers.google.com/web/tools/lighthouse page achieve 91%

- CSS - Jigsaw W3C Validator CSS - https://jigsaw.w3.org/css-validator/ This document validates as CSS level 3 + SVG !

- JS Hint - https://jshint.com/ - only error is related to module.exports as part of JEST testing and doesnt effect game play.

# Technologies used
-	HTML
-	CSS
-	Javascript

# Applications and Libraries 
-	Bootstrap: Bootstrap was used to assist with the responsiveness and styling of the website.
-	Google Fonts: Google fonts were used to import the Bebas Neueu.
-	Gitpod: Git add, commit and push commands were used to maintain version control.
-	GitHub: was used as my online repository to score code, commit messages and versioning
-	GitHub Pages: was used to deploy my live site, and host my site
-	Balsamiq: Balsamiq was used to create the wireframes during the design process.
-	Chrome developer tools: Was used to inspect code, use of console was used to debug code, screen options were used to test on different screen sizes, different devices.
- Mockup Generator - http://techsini.com/multi-mockup/index.php

# Credits
## Images

- Ronaldo -  https://bleacherreport.com/articles/10012193-cristiano-ronaldo-scores-brace-in-triumphant-manchester-united-return
- Casameiro - https://www.news.ro/sport/acord-intre-real-madrid-si-manchester-united-pentru-casemiro-1922404219182022082220825174
- Sancho - https://www.caughtoffside.com/2021/09/30/sancho-stats-for-man-united/
- Rooney - https://www.premierleague.com/video/single/1053627
- Scholes - https://www.pinterest.co.uk/pin/300615343849672341/
- Fernandes - https://www.manutd.com/en/news/detail/bruno-fernandes-exclusive-interview-before-psg-v-man-utd-on-20-october-2020
- Club Badge/crest - https://en.wikipedia.org/wiki/Manchester_United_F.C.

It is recognised due to the commercial value of Manchester United, its players and sponsors, that if this site was intended for a wider audience then images would need to be purchased with the correct licensing. 

# Acknowledgements and thanks.

## Spence Bariball (Mentor)
Helping to keep me motivated, and being supportive when felt overwhelmed. Giving great advice, and suggesting workarounds/solutions to issues.

## CYC-Apr-2022 Slack group
For generally keeping me in a good headspace.

## Sean and John - Tutor Assistance
Helping me with JEST, and in particular issues was having when testing elements that get created/updated in the DOM

## Ania Kubow 
Fantastic tutorial, and explanations for generating the cards using JavaScript - "Learn JavaScript by Building 7 Games - Full Course"
https://www.youtube.com/watch?v=ec8vSKJuZTk&t=5449s

## Bobby Hadz
Excellent explanation in relation to removign event listener, and why may get issues.
https://bobbyhadz.com/blog/javascript-remove-event-listener-not-working#:~:text=To%20resolve%20the%20removeEventListener%20not,will%20not%20remove%20the%20listener.

## Slack Community
Had issue/errors when initally testing using JSHINT 
https://app.slack.com/client/T0L30B202/search/search-eyJkIjoianNsaW50IiwicSI6IlUwM0FTQVFMS1BHIiwiciI6ImpzbGludCJ9/thread/C7HD37Q1F-1628782478.134000

## W3 Schools
Tutorial showing how to create a modal overlay
https://www.w3schools.com/howto/howto_css_modals.asp



