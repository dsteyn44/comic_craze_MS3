<h1 align="center">Kapow! Comic Collection</h1>

[View the live project here.](https://kapow-comics.herokuapp.com/)

Kapow Comic Collection is a hub where comic collectors can add the data of recent comics they have read or actually have in their possession such as rare types. Users will be able to sign up to their own profile page. Perhaps they wish to tag comics that they like or wish to add their own comics that they read in the collection. In addition to this Users will be able to edit or delete any of they added comics on the website.  As more users subscribe so the database will increase. Links will eventually be  added to eBay or a website where they can purchase the comics. 

As the base grows the site will extend to include some extra features such as: a blog, a fan page that extends to social network. A database of Superheroes will also be included.

![mock-up](static/images/kapow_responsive.png)

## User Experience (UX)

-   ### User stories

    -   #### First Time User Goals

        1. As a First Time User, I want to easily understand the main purpose of the site and learn more about the concept.
        2. As a First Time User, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time User, I would like to sign in easily

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to see .
        2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.
        3. As a Returning Visitor, I want to find community links.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.
        2. As a Frequent User, I want to check to see if there are any new blog posts.
        3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.

     -   #### Admin User Goals
        1. As an Admin User, I want to check in my profile any new added comics.
        2. As a Frequent User, I want to check to see if there are any new blog posts.

-   ### Design
    -   #### Colour Scheme
    
        - I have opted for a comic theme of bright colors echoing the comics from yesteryear.
        - The use of black as the main color of the type is important - mimicing the type of those ink drawn comics.
        - #fffde7 yellow lighten-5 (from Materialize): This was used for the forms and echo the color of the pages comics and how old they become.
        - #00bcd4 cyan (from Materialize): This was used to represent superman's uniform. Maybe a bit of a cliche but something the User will immediatly identify with.
        - The cards( the below being an amber rating card) were all colored differently to distinguish between tagged cards, comic collection cards (added by users)and as ponted out the ratings card.
        - [Purple Comic Card](static/images/ppl_comic_card.png)
        - [Cyan Profile Card](static/images/cyan_prof_card.png)
        - [Amber Rating Card](static/images/amber_rate_card.png)

    -   #### Typography
        - In regards to the text, again I have tried to follow the traditional comic fonts where possible and where it does not intervene with the readibility.  
        - The main logo is set in "Permanent Marker" from google fonts. At first I used Bungee Shade but I felt tghis did not reflect totally the comic feel of old styled comics of yesteryear. I also used "Permanent Marker" for some of the main copy such as below the headlins on the comics page and Sign-in Sign-up ppages. However for the main copy of the synopsis of the "comic cards", i opeted for Roboto to me clearer.
        - In terms of the icons, I have gone with a mixture of Materialize and Font Awesome icons. 


    -   #### Imagery
        - As this project is about comics the typical imagery of comic art is important. The home page reflects this with an image of comics in the background. the rest of the imagery was taken from the website [League of Comic Geeks](https://leagueofcomicgeeks.com/)



 *  ### Wireframes

    -   Home Page Wireframe - [View](static/images/wireframes/home.png)

    -   Comics Wireframe - [View](static/images/wireframes/comics.png)

    -   Profile Page Wireframe - [View](static/images/wireframes/profile.png)

    -   Add Comics Page Wireframe - [View](static/images/wireframes/add_comic.png)

    -   Edit Comics Page Wireframe - [View](static/images/wireframes/edit_comic.png)

    -   Sign Up Page Wireframe - [View](static/images/wireframes/signup.png)

    -   Sign in Page Wireframe - [View](static/images/wireframes/signin.png)

## Features
### Current Features
-   Responsive on all device sizes

-   Interactive elements such as edit and remove buttons. Tag buttons on the comic cards.

### Left to implement
-   More defensive design elements such as verifying logging out/deletion of information.
-   Add more CRUD aspects to Profile information eg: delete and editing Profile Information.
-   Adding social media elements such as a blog.  

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JQuery](https://jquery.com/)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Regex](https://regex101.com/)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Affinty:](https://www.adobe.com/ie/products/photoshop.html)
    - Affinity similar to Photoshop but is tuned for MAC.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [RandomKeygen:](https://randomkeygen.com/)
    - RandomKeygen was used to create a random password (https://github.com/) during the coding process.
1. [Material Bootstrap:](https://mdbootstrap.com/)
    - Material bootstrap is a hybrid 
1. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)- 
    - Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.
1. [Materialize](https://materializecss.com/)
    - Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology.   
1. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

## Testing



-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and a "Learn More" Call to action button.
        2. The main points are made immediately with the hero image
        3. The user has two options, click the call to action buttons or scroll down, both of which will lead to the same place, to learn more about the organisation.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. At the bottom of the first 3 pages there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page.
        3. On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

    3. As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their following on social media to determine how trusted and known they are.
        1. Once the new visitor has read the About Us and What We Do text, they will notice the Why We are Loved So Much section.
        2. The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
        3. At the bottom of the Contact Us page, the user is told underneath the form, that alternatively they can contact the organisation on social media which highlights the links to them.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new programming challenges or hackathons.

        1. These are clearly shown in the banner message.
        2. They will be directed to a page with another hero image and call to action.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
    
    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
c

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.


### Known Bugs

-   On some mobile devices the Edit Comic page pushes the size of screen out more than any of the other content on the page.
    -   A white gap can be seen to the right of the footer and navigation bar as a result. This is only temporary. as far as i can assess it is a result of a div with a class of .hidden_div - assume that it is from materialize.

 
    
## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Creating a MongoDgit commit -m "b account and collection and wiring it up

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Setting-Up Mongo Db

- Open up mongoldb.com
- Click on try free as this will be enough to hold our information.
- Enter our email address, whether it's a work or personal email, it doesn’t matter.
- First and last name, and then a password which has to meet certain requirements.
- Agree to the terms and privacy policy, then finally   click on 'Get StartedFree'.
- You need to start by creating a Cluster.(A cluster is, as its name suggests, a cluster of service that our database will run on).
- The 'Shared Clusters' offers a free service, which is perfectly suitable for your purposes,
- Click to 'create a Free Cluster'.
- Next, select a Cloud provider. Amazon Web Services, or AWS, is an excellent cloud service, is fine to have as a default.
- For the region, you want to select the region closest, I am based in Sweden so Belgium. <strong>Please note, it might show you that some regions are not part of the 'free' tier support, sobe sure to select the closest region to you that offers free service.</strong>
- On my screen, all of these regions don't specify any pricing, so they all support the freetier.
- Next, choose a Cluster Tier. Choose the M0 Tier, which is the 'free forever' tier. Then, we can scroll down to the bottom, and select 'Cluster Name'.
Leave the cluster name as the default Cluster0, but I'm going to rename mine to'myFirstCluster' using the camelCase naming convention.
- Finally, click on the 'Create Cluster' button. This is going to take a few minutes to provision and create our database.
- While that's happening, click on 'Database Access' under the Security section on the left, in order to create our database user credentials.
- Click on 'Add New Database User', and use the default SCRAM authentication method by creating a username and password.
- Please note, even though the example shows special characters, we need to be sure to only use a combination of letters and numbers, otherwise this will cause issues on future
- <strong>Remember to keep your own username and password significantly more secure. They should never appear in any GitHub repository, otherwise you're giving away full access to your database.</strong>
- Finally, we need to make sure that our user privileges are set to 'Read and Write to the Database', and click 'Add User'.
- Once the user is added, click on 'Network Access' within the Security menu, in order to whitelist the IP address and make sure that it has access to our database.
- Click 'Add IP Address', and for now, select 'Allow Access From Anywhere’, partly because you may be accessing this from our workspace, and then later on Heroku. Ideally, you should put the IP addresses of your hosts here, as this acts as a further security feature, and can help to prevent unauthorized access to your data.
- By now,the cluster should hopefully be provisioned, then go back to the Clusters tab.
- Once it's fully provisioned, everything will change, and the buttons will become enabled.
- That's ready from this side, so now click on the 'Collections' button.
- You may wish to create our own data, instead of loading an existing dataset, so click 'AddMy Own Data'.
- This is where we can create our database.
- Use camelCase such as MyFirstCluster.

### Setting up Heroku
This project is deployed using Heroku. The following steps were taken;

- Within GitPod, create the .gitignore and env.py files.
- In the .gitignore file, set it to ignore the env.py file and pycache/ directory.
- Within the env.py file, set the following environmental variable;
    - os.environ.setdefault(“IP”, “0.0.0.0”)
    - os.environ.setdefault(“PORT”, “5000”)
    - os.environ.setdefault(“SECRET_KEY”, “YOUR_SECRET_KEY”)
    - os.environ.setdefault(“MONGO_URI”, “mongo db link to go here”)
    - os.environ.setdefault(“MONGO_DBNAME”, “YOUR_DATABASE_NAME”)
- Make sure that the env.py file has been saved correctly and open the app.py file. Import OS, Flask and the env.py file.
- Create a requirements.txt file by typing in the terminal; pip3 freeze –local > requirements.txt.
- For Heroku, you will also need a Procfile. Create this by using the terminal and typing; echo web: python app.py > Procfile. Access the Procfile and delete the bottom empty line to avoid any issues in the future.
- Go to the Heroku site, and log in or create a profile. From the dashboard, select “New App”. Create a name for your app, select the correct region and click “Create App”.
- Navigate over to the “Deploy” tab and go to the “Deployment method” section. Click on GitHub.
- Search for your repository name, and click “Connect” next to your repository name.
- Next, go to the “Settings” tab, and scroll down to “Config Vars”. Click “Reveal config vars”.
- Enter the Key and Value pairs as per your env.py file;
    - IP : 0.0.0.0
    - PORT : 5000
    - SECRET_KEY : YOUR_SECRET_KEY
    - MONGO_URI : “mongo db link to go here”
    - MONGO_DBNAME : “your database name”
- Finally, go back to the “Deploy” tab, and scroll down to “Automatic deploys”. Click on “Enable Automatic Deploys” then “Deploy Branch”.
- The app will now be built and upon completion, you will receive a message saying “Your app was successfully deployed”.
- You can now click on “Open App” which will launch the deployed app.

## Credits

### Code

-   The majority of the code was taken from the Task-Manager Mini project. It was then adjusted for a comic card instead of a task card. 

-   The full-screen hero image code came from this [StackOverflow post](https://stackoverflow.com)

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   Not all content was written by the developer. Some of the content such as the synopsis of the comic books were taken from the wewbsite [League of Comic Geeks](https://leagueofcomicgeeks.com/)

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   Freep

### Acknowledgements

-   My Mentor Precious for continuous helpful feedback.

-   Tutor support at Code Institute for their support - Fatima, Igor, Jo and John. Thank you for being so patient.

-   Talyor Brookes, thanks for the help with the creating a favorites tag. Hope it goes well with your MS4.

-   All the guys in my Slack group. Thank you for the support.

-   My wife Sofia and sons August & Adam for having to put up with me during this course. Love you to the moon and back.  

### Disclaimer

This project is for educational purposes only. strictly forbidden for public use. If there is an issue with the copyright or the content, please contact me: d_steyn@yahoo.com.
