#  Testing Ground
## Overview 
As this was a data driven project much of the testing was done using friends to check the performances of the 
#
## Validators used: 
- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)1
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
-   [PEP 8](http://pep8online.com/) 
- Lighthouse - I used this to check performance. However I have to be honest and say that there was alot I was unsure of but it was good to gage and will be useful in the future. [Lighthouse Chrome](https://developers.google.com/) 
- 

### Proof of final validation:

### HTML:
#### home.html 
![HTML Validator home](static/images/validators/home_w3_validator.png)

#### comics.html 
![HTML Validator comics](static/images/validators/comic_w3-validator.png)

#### profile.html 
![HTML Validator profile](static/images/validators/prof_w3_valid.png)

#### add_comic.html 
![HTML Validator add comic](static/images/validators/addcom_w3_valid.png)

#### signup.html 
![HTML Validator sign-up](static/images/validators/signup_w3_valid.png)

#### signin.html 
![HTML Validator sign-in](static/images/validators/signin_w3_valid.png)

### CSS:
#### style.css
![CSS Validator Jigsaw](static/images/validators/css_w3_.png)

### PEP 8 Compliant:
#### PEP-8
-  The PEP-8 online validator was used to check my python code and it proved fine. 

![PEP-8](static/images/validators/pep_8_valid.png)


![CSS Validator Jigsaw](images/validators/css_w3_valid.png)
### Lighthouse:
- Mobile
![CSS Validator Jigsaw](readme-files/CSS.png)

![Lighthouse Mobile](readme-files/light-mobile.png)
- Desktop

## Responsiveness

For the responsiveness I used Chrome Developer Tools to check how the website would behave. However saying this I must add that it did not always give a correct or real account on the device. Of course it is only a tool and not but I found one instance where it did not give me the correct response. This was an instance it was for mobile phone (iPhone X). On Dev tools it showed the main figure on the front-page was clearly visible but when I uploaded this on my device his head appeared cut-off by the jumbotron. The image looked too big. I did clear this up later by adding a media query and viewpoint height.  
For the responsiveness I used Chrome Developer Tools to check how the website would behave. However saying this I must add that it did not always give a correct or real account on the device. Of course it is only a tool and not but I found one instance where it did not give me the correct response. This was an instance it was for mobile phone (iPhone X). Unfortunately I had some issues with the response for the time and weather icons

I also used [Responsive Design Checker](www.responsivedesignchecker.com) and this was fairly accurate. The difference (niether good nor bad) this site has over Chrome Devoloper is that it has some sizes that Chrome does not such as the IMac Desktop 24". I us the 27" so when I opened my browser to Chrome it overstretched my image. Below is a responsiveness chart that shows the how each device responded. I added the surface duo because it has a perculiar screen so i can see how my site reacts. 
#
## Bugs
- script.js and slider.js <script> would not load in index.html.
Action: it was the incorrect path in the script. works now.


### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.


## User stories

### Client User GOALS
#### As a client I want set-up a website so that it will bring like-minded people together.
- The client in this case does not have a website but a page on facebook and although it is a place where fans can converse in one that will be solely dedicated to the band's fans. But the fact that it can evolve means that it may get bigger and become a bigger social platform. from my research there is not much out there.
#### As a client I want a better platform so that I can increase my fan base.
- Leading from the above, if you have a hub for this type of culture you will attract more, especially if they go with a narrative. 
#### As a client I want my users to easily navigate my site so that they have a better user experience and therefore will continue to visit.
- the website was designed to be easily navigated, that is mostly linear with a one branch. But it has scope that in the future it can evolve with more branches but it will always retain the ability to quickly get to where you want to go. even if you need to get out of an empass.
#### As a client I want the website to have room to evolve so that I will have a repeat fanbase that is not necessarily from the same genre.
- As discusssed above, having a narrative will bring in another crowd that is not necessarily death-metal fans. Also with the inclusion of humour (although you have to be careful), you will get fans who value the comedic value to. It shows that the band do not take themselves too seriously. 
#### As a client I want eye catching visiuals so that the first time users will want to want to investigate further. 
- The front page's Image does just that. It gets the attention of the user. It is more in line with a Nordic Noir theme- something you would see from the cover of a book and therefore is the reason i used it. I also used yello to catch the attention away from the black color. I also included a competition draw to attract fans. This draws them inside the website and a question about one of the band members leads the fans to scope out the band and their history, their narrative.

### First time User Stories
#### As a first time User I want to be able to hear the bands music on the first page so that that I decide to follow.
- This is the reason why I placed the sound bar. It is not on auto-play (I doubt anyone would continue to view the site if it was not). It is only a snippet so just enough to wet the appetite of the fan. Also I placed their best song so that it grabs a would-be fan straight away.
#### As a first time User I want to see where they are playing and the dates so I can see if i am  able to go view the concert.
- I placed the gig guide right and center so that it is easy to access 
#### As a first time User I want to see what the band is about, who they are so.
- The first time user can access this from the navbar or by simply scrolling down. there is also a competition that leads the user to sign up as part of the fan base and even before that, it will ask a question about a band member. this leads the user to look for the band memebr and acquire that information.
#### As a first time User I want to navigate easily throughout the site so that I can get to the pages efficently. 
- It is not a big sight at the moment, however thge links are easily accessed. 

### Frequent User
#### As a frequent user I want updates so that I can visit the website and it will keep me interested.
- This is the reason I added the fanmail, section. To make it easier for fans to be heard and see what aother fans are saying. It keeps the fans coming back. Also another reason for keeping the interest of the frequent fan is to keep the narrative going. So each new album that comes out will be a story (about the band essentially). It means also that the band does not run out of ideas.

### Festival organiser/ Concert organiser
#### As festival organiser/ Concert organiser I want to efficently contact them.
-There is also a Contact Us! modal at the top of the page visible at all times.
#### As festival organiser/ Concert organiser I want to see who account for their fans  so that i can see if they are are suitable for the content that I provide.
- As a Concert agent they can gage the newer fans and the frenquent fans by visiting the Fanwall. It will be up to date with what the band is doing. 
#
### Bug Fix

Backend
-   Was deploying on Heroku but showed an error pymongo Auth fail. I worked out that my MONGO_URI Connection was incorrect.
-   Tried to sign in as "admin" but was thrown an error "UnboundLocalError: local variable 'favorite' referenced before assignment". The reason for this was that the "favorite" value had been assigned to the user but not to the admin. Igor from Tutor support asssisted me with this.
-  Tried to add a flash as defensive design to inform User that the search yielded a no result. On the debugger it returned a "Typeerror ' comics ' not supported between instances of 'list' and 'int' in python. I did some research on Stack overflow and the resolved the issue with a len() method. It proved correct.

Frontend
- There were many frontend issues and although this is not conclusive, but possibly as a result of Materialize. Most of the time it was the comic card face content- that had shifted 50px to the left but this was fixed using DevTools on Google, testing the change and then applying iy directly into the HTML. 
- 


## User stories

## Side Notes
