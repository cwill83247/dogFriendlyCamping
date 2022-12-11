# Dog Friendly Camping 
## ADD IMAGE of screens ----- 

# Purpose
The purpose of this site, is to provide a front end to a searchable database of dog friendly camping venues. It is intended to allow users to register, login and add camping venues that are suitable for dogs
It is intended to demonstrate some of the skills I have learnt, in HTML,CSS, Javascript, Python,Flask, JINJA templating and MongoDB to meet the criteria of milestone 3

The site is aimed at Adults of all ages, the idea was inspired by the addition of a dog to the family, and need to find camping venues/sites that allow dogs. 

# Live Site
The live site is published here using Heroku - https://dogfriendlycamping.herokuapp.com/

# User Experience Design
First Time Visitor Goals
-	As a first time user I need to quickly and easily understand the purpose of the site.
-	As a first time user I need to be able to navigate the site easily.
-	As a first time user I need to be able to view the website clearly on both tablet and mobile, as well as desktop.
-	As a first time user I need to be able to easily register with the site.
-	As a first time user I need to be able to find information quickly and intuitively.


Returning Visitor Goals
-	As a returning visitor I want to be able to log into the site easily
-	As a returning visitor I want to find venues i have added easily
-	As a returning visitor I want to Create, Update and delete venues linked to me.

# Design
## Structure
The site has been split into several pages with different access levels.
- Pages that a registered user can view.
- Pages that an unregistered user can view.
- Pages that an Admin can view.

The design went through several design ideas before settling on the current design, with my intial design after user research be considered amaetuer, and not fit for a professional website.

The Index page has been designed as the shopfront to the site, to briefly explain what the site is about, encourage a user to register and contribute to the site.

Site Navigation has been placed at the top of the page so easily identifiable, and intuitive for a vistor of the site.
Branding has been placed just below, that reflects the purpose of the site. Colours wewre taken from researching other outdoor websites. The dark theme for the header fitted my intention in design.

A footer was added so consitent throught the site.

## Initial design Experience
The pages have been designed to represent a brand throughout the site, be intuitive to the user, whilst focussing on the content. 
I have tried to limit clutter, and to provide a clean look and feel in terms of design for the user.

## Colour Scheme 
The colours used in my design were identified from researching other websites, that had an outdoor intention, it seemed a common theme for them to have a darker header, with white logo. I then used colours to compliment the intial dark grey.

## Branding
Once the colour scheme had been identified I developed the logo ideas intially using - https://looka.com/, I then created the logo and tailored the design using Fireworks.
The Peaks in the header were designed using https://app.haikei.app credit for the tutorial demonstrating this website - ttps://www.youtube.com/watch?v=lPJVi797Uy0

Images used for the logo design from - https://www.gograph.com/vector-clip-art/dog-face.html

# ADD COLOUR PALLETTE !!!!

## Typography 
# ADD !!!!!!!!

# Responsiveness 
The site is intended to be quick,and intuitive for all users, on desktop, Tablet or Mobile. 

The design responds to varying screen sizes, and devices, changing the layout appropriately to ensure its useable on all device formats. 

Primary responsiveness is acheived by using the Bootstrap CSS Framework.

# Future developments
-	Pagination for results.
-	Filtering options os easy to navigata as the content grows.
-	Searchable by post code, location or via a map.
-   Improve Design
-   Improve authentication and access to a more robust solution. 

# Wireframes
## ADD

# Deployment
## Heroku
Deploying site so live using Heroku

The code for this website was written in Gitpod, pushed to GitHub and was deployed using Heroku.

The database used was MongoDB.

The following process was used to deploy this website:

1. Create a "requirements.txt" file using the command "pip3 freeze --local > requirements.txt"
2. Create a "Procfile" using the command "echo web: python app.py > Procfile"
3. Push these changes to your repository by using "git add -A", "git commit -m 'your commit message here'" and then "git push"
4. Ensure you have a .gitignore file in your repository
5. Add "env.py" and "pycache/" to your .gitignore file to ensure that no sensitive information is added to your repository
6. Login or sign up to Heroku
7. Click "New" on the top right of the dashboard and select "Create new app"
8. Include an "App name", choose a region and click "Create app"
9. Click the "Deploy" tab and under "Deployment method" select "GitHub"
10. Search to find your GitHub repository and click "Connect". Please note: do not enable automatic deployment yet as this will cause errors
11. Click the "Settings" tab and click "Reveal Config Vars" from Config Vars
12. Enter the key value pairs that match those in your env.py file:
13. Go back to the "Deploy" tab and click "Enable Automatic Deployment"
14. In the "Deploy" tab under "Manual deploy", select "main"
15. Click "Deploy Branch"
16. Once the app has finished building click "Open App" to open your site.

## Cloning GitHub Repository
1. Log in to GitHub and locate the GitHub Repository. 
2. Under the repository name, click "Clone or download". 
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. 
4. Open Git Bash. 
5. Change the current working directory to the location where you want the cloned directory to be made. 
6. Type git clone, and then paste the URL you copied.


# Testing Tools
The Lighthouse, W3C Markup Validator,and the Lighthouse report were used to determine whether there were any errors in the code. I ensured standards were met in design, and also accessebility.

-	W3C Markup Validator
-	W3C CSS Validator
-	Lighthouse report

## ADD CSS Screenshot
## ADD Lightohouse Accessebility
## ADD Lighthouse Performance

# Testing User Stories from UX Section
##	First time visitor goals
- As a first time user I need to quickly and easily understand the purpose of the site.
--	The theme of the site is easily identifiable, and the purpose clearly displayed, the design is clean and simple with focus on the users experience.
![initial screen](https://dogfriendlycamping.herokuapp.com/static/images/userstory1.fw.png)

-	As a first time user I need to be able to navigate the site easily.
--	navigation is clear and consistent throughout the site.


## Returning Visitor Goals

- As a returning visitor I want to be able to log into the site easily
-- logging int othe site is quick and easy with clear messages.
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
-   JINJA Templating
-	Chrome developer tools: Was used to inspect code, use of console was used to debug code, screen options were used to test on different screen sizes, different devices.
-  Mockup Generator - http://techsini.com/multi-mockup/index.php

# Credits
## Images



# Acknowledgements and thanks.

## Spence Bariball (Mentor)
Helping to keep me motivated, and being supportive when felt overwhelmed. Giving great advice, and suggesting workarounds/solutions to issues.


## Tutor Assistance
Kevin @ CI for helping me resolve an issue with defensive programming, and the r 

## Slack Community




# dogFriendlyCamping

Dog Cartoon Image - http://clipart-library.com/clipart/dog-clip-art-27.htm
Tent Outline - http://clipart-library.com/tent-outline-cliparts.html
Dog Cartoon Face  - https://www.gograph.com/vector-clip-art/dog-face.html

https://looka.com/ INITIAL LOGO DESIGN IDEA, and then deisgned using Fireworks


https://www.youtube.com/watch?v=lPJVi797Uy0  SVG Design for Peaks

https://app.haikei.app/  to create SVG

Edited using Adobe Fireworks

Search Index
Dont forget to add a bit about createing searhc index within gitpod, using python for the campingVenues collection
restricted to the fields venue_name, location, description and tags

Thanks
Mentor
Kevin @ CI Tutor Support for helpign me to get modal to delete correct record, as part of defensive deletion. 

Include added defensive programming for delete

#Standard and Template below 

