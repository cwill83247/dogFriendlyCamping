# Dog Friendly Camping 
![mockup](https://dogfriendlycamping.herokuapp.com/static/images/dfcmockup.PNG)

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

The design went through several design ideas before settling on the current design, with my intial design after user research being considered amaetuer, and not fit for a professional website.

![old logo](https://dogfriendlycamping.herokuapp.com/static/images/logo.fw.png)
![new logo](https://dogfriendlycamping.herokuapp.com/static/images/newDFClogo2.fw.png)

The Index page has been designed as the shopfront to the site, to briefly explain what the site is about, encourage a user to register and contribute to the site.

Site Navigation has been placed at the top of the page so easily identifiable, and intuitive for a vistor of the site.
Branding has been placed just below, that reflects the purpose of the site. Colours wewre taken from researching other outdoor websites. The dark theme for the header fitted my intention in design.

A footer was added so consitent throught the site.

# Database Design

MongoDB was used as a non relational database, to hold the collections as listed below, they were stored in a DB "dog_friendly_camping" 

## Structure 
![db schema](https://dogfriendlycamping.herokuapp.com/static/images/dbschema.PNG)

- users (Collection)
-- _id : unique id system generated
-- username: a username created by a visitor to the site
-- password: password created by user stored using SHA256

- campingVenues (Collection)
-- _id : unique id system generated
-- venue_name: name of the venue

- venueType (Collection)

## Search Index
Search index created within Gitpod, using python for the campingVenues collection to allow a search facility for users of the site when lookign for venues.
The search was restricted to the fields - venue_name, location, description and tags.

# Initial design Experience
The pages have been designed to represent a brand throughout the site, be intuitive to the user, whilst focussing on the content. 
I have tried to limit clutter, and to provide a clean look and feel in terms of design for the user.

## Colour Scheme 
The colours used in my design were identified from researching other websites, that had an outdoor intention, it seemed a common theme for them to have a darker header, with white logo. I then used colours to compliment the intial dark grey.

![colour pallete](https://dogfriendlycamping.herokuapp.com/static/images/colourpallete.PNG)

## Branding
- Once the colour scheme had been identified I developed the logo ideas intially using - https://looka.com/, I then created the logo and tailored the design using Fireworks.
- The Peaks in the header were designed using https://app.haikei.app credit for the tutorial demonstrating this website - ttps://www.youtube.com/watch?v=lPJVi797Uy0

- Images used for the logo design from - https://www.gograph.com/vector-clip-art/dog-face.html

## Typography 
- Typography was provided by the Bootstrap CSS
- Navigation was 'Poppins' with sans-serif as a backup
 - Logo design used Franklin Gothic Demi form Adobe Fireworks

# Responsiveness 
The site is intended to be quick,and intuitive for all users, on desktop, Tablet or Mobile. This has been tsted across desktop, tablet and mobile. The design responds to varying screen sizes, and devices, changing the layout appropriately to ensure its useable on all device formats. 
- Primary responsiveness is acheived by using the Bootstrap CSS Framework.

# Future developments
-	Pagination for results.
-	Filtering options os easy to navigata as the content grows.
-	Searchable by post code, location or via a map.
-   Improve Design
-   Improve authentication and access to a more robust solution. 

# Wireframes
![dfc wireframe](https://dogfriendlycamping.herokuapp.com/static/images/dfc_wireframe.png)

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
The Lighthouse, W3C Markup Validator,and the Lighthouse report were used to determine whether there were any errors in the code. I ensured standards were met in design, and also accessibility.

-	W3C Markup Validator
-	W3C CSS Validator
-	Lighthouse report

# Testing User Stories from UX Section
##	First time visitor goals
- As a first time user I need to quickly and easily understand the purpose of the site.
  - The theme of the site is easily identifiable, and the purpose clearly displayed, the design is clean and simple with focus on the users experience.
![initial screen](https://dogfriendlycamping.herokuapp.com/static/images/userstory1.fw.png)

- As a first time user I need to be able to navigate the site easily.
  - navigation is clear and consistent throughout the site, with the use of a niviagtion bar that adjust depending on user access level.

![navbar screenshot](https://dogfriendlycamping.herokuapp.com/static/images/navscreenshot.PNG)  

- As a first time user I need to be able to view the website clearly on both tablet and mobile, as well as desktop.
  - the site is accesible across various device screen sizes and types , this was tested as part of the deisgn process.

- As a first time user I need to be able to easily register with the site.
  - registration is quick and simple for the user

- As a first time user I need to be able to find information quickly and intuitively.
  - information is easy to access, wih use of a consistent navigation, and searching for content is easy with the use of a seatch box, user added content is stored for editing or deletion under the My Profile Page.


## Returning Visitor Goals
- As a returning visitor I want to be able to log into the site easily
  - logging into the site is quick and easy with clear messages.
![login page](https://dogfriendlycamping.herokuapp.com/static/images/loginscreenshot.PNG)
- As a returning visitor I want to find venues i have added easily
  - venues are easy to find by using the My Profile page when a user is logged in 
![user profile page](https://dogfriendlycamping.herokuapp.com/static/images/userprofile.png)

- As a returning visitor I want to Create, Update and delete venues linked to me.
  - Options to add venues are done via the main menu bar, edit and delete of user created content is done within the profile page.

![edit and delete](https://dogfriendlycamping.herokuapp.com/static/images/editdelete.PNG)  

# Further Testing
- Python script was run through PEP8 compliance check to ensure free for errors. I installed the pypi.org PEP8 checker using "pip install pep8" the checker was then run against my app.py using the code "pep8 --show-source --show-pep8 app.py"
- CSS was run through W3C validation
- HTML was run through W3C validation 
- Manual testing was carried out, against my user stories.
- Family members provided user feedback, at very early stages it was considered the bran was unproffesional, so this was redesigned.

Testing has been a continous process, after every commit, the code was tested to ensure the site functioned as expected.

# Errors and Bugs
- Contrast issues identifed by Lighthouse Accessebility
changed the navigation bar colours so more of a contrast.

- Required form fields 
Had anissue with the form, and the required elements not being enforced, this was due to a bootstrap novalidate option being applied that is intended for custom forms.

- Error: Start tag body seen but an element of the same type was already open.
From line 56, column 1; to line 56, column 23
changed the base template to include the class, and removed the class form other pages

- PEP8 Compliance issues
Issues arround indentatation and whitespace resolved.

- Defensive Deletion
Use of Modal to delete and prpvide and added prompt to users, resulted in only the first record ever being deleted. Ammended code to ensure unique id was passed to the modal.

# Validation

- HTML - Validator used - https://validator.w3.org/ 

- Accessibility - Lighthouse Viewer chrome developer tools - https://developers.google.com/web/tools/lighthouse 
pages achieve between 84% - 97%, majority of errors were due to the Bootstrap CSS, and were an accepted trade off for using bootstrap.

- CSS - Jigsaw W3C Validator CSS - https://jigsaw.w3.org/css-validator/ 
CSS Errors due to Bootstrap CSS, all of my own custom CSS passed validation


# Technologies used
-	HTML
-	CSS
-	Python
-   JINJA Templating
-   Flask Framework
-   MongoDB (non relational DB)
-   Adobe Fireworks    

# Applications and Libraries 
-	Bootstrap: Bootstrap was used to assist with the responsiveness and styling of the website.
-	Google Fonts: Google fonts were used to import the Bebas Neueu.
-	Gitpod: Git add, commit and push commands were used to maintain version control.
-	GitHub: was used as my online repository to score code, commit messages and versioning
-	Heroku: was used to deploy my live site, and host my site
-	Balsamiq: Balsamiq was used to create the wireframes during the design process.
-   JINJA Templating
-   Flask Framework
-   MongDB
-	Chrome developer tools: Was used to inspect code, use of console was used to debug code, screen options were used to test on different screen sizes, different devices.
-   Mockup Generator - http://techsini.com/multi-mockup/index.php

# Credits
## Images
- Dog Cartoon Image - http://clipart-library.com/clipart/dog-clip-art-27.htm
- Tent Outline - http://clipart-library.com/tent-outline-cliparts.html
- Dog Cartoon Face  - https://www.gograph.com/vector-clip-art/dog-face.html
- Initial logo idea - https://looka.com/ , I then designed using Fireworks, so could cusomise to suit the brand.
- SVG Design for Peaks - https://www.youtube.com/watch?v=lPJVi797Uy0  
- Home Page main image - https://familyvacationist.com/camping-with-pets-and-kids-etiquette/
- Image Placeholder for venue image - https://i0.wp.com/bucketlistjourney.net/wp-content/uploads/2022/03/Take-Your-Dog-Camping-RF-1.jpg

# Acknowledgements and thanks.

## Spence Bariball (Mentor)
Helping to keep me motivated, and being supportive throughout. 

## Tutor Assistance
Kevin @ CI Tutor Support for helpign me to get modal to delete correct record, as part of defensive deletion. 

## Slack Community









