# The PC Hobbyist Website

## Table of contents

- [The PC Hobbyist Website](#the-pc-hobbyist-website)
    - [Table of contents](#table-of-contents)
    - [Overview](#overview)
        - [What and Who is this website for?](#what-and-who-is-this-website-for)
    - [UX](#ux)
        - [Persona #1](#persona-1)
        - [Persona #2](#persona-2)
        - [Persona #3](#persona-3)
        - [Actions the personas may carryout](#actions-the-personas-may-carryout)
        - [Mockups](#mockups)
    - [Features](#features)
        - [Existing Features](#existing-features)
        - [Features left to implement](#features-left-to-implement)
        - [Known Issues](#known-issues)
    - [Technologies Used](#technologies-used)
    - [Testing](#testing)
        - [Scenario One: User Registration](#scenario-one-user-registration)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Two: User changes Avatar](#scenario-two-user-changes-avatar)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Three: User changes password](#scenario-three-user-changes-password)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Four: User Donation](#scenario-four-user-donation)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Five: Blog](#scenario-five-blog)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Six: Forum](#scenario-six-forum)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Seven: About Page](#scenario-seven-about-page)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Eight: Contact Form](#scenario-eight-contact-form)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Nine: Logging Out](#scenario-nine-logging-out)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
        - [Scenario Ten: User can't access donations if not authenticated](#scenario-ten-user-cant-access-donations-if-not-authenticated)
            - [Scenario Steps](#scenario-steps)
            - [Desired Outcomes](#desired-outcomes)
    - [Deployment](#deployment)
        - [Separated Online code from Offline code](#separated-online-code-from-offline-code)
        - [Setting up Heroku](#setting-up-heroku)
        - [Hosting the MySQL database](#hosting-the-mysql-database)
        - [Static files](#static-files)
    - [Credits](#credits)
        - [Content](#content)
        - [Acknowledgements](#acknowledgements)

## Overview

### What and Who is this website for?

This is my Stream Three project for [Code Institute](https://www.codeinstitute.net/). The project scope is to website using both the front end and back end technologies learnt throughout the entire course.

## UX

The idea is that the website will be used by PC enthusiasts of all levels from beginner to expert. The website will be mainly used as a place for PC enthusiasts to build a community where newbies can get help on building computers/problems and experts can provide their knowledge as well as blog about any current projects they are working on or anything they feel worthy of sharing with the websites community.

I created several personas with this website in mind:

### Persona #1

- **Fictional name:** Jordyn Dach
- **Age:** 14
- **Education:** Secondary School
- **Ethnicity:** White British
- **Family Status:** Single
- **Job title:** N/A
- **IT/ domain experience:** Good, Can use a computer competently but is keen to learn more about computers.
- **Personality:** Young and eager to learn, loves to play computer games.
- **The goals and tasks they are trying to complete using the site:** Jordyn wants to find out how to build his very first PC and learn more about computers.
- **How often are they likely to use the site?** Jordyn will visit the site frequently whilst building his first PC.
- **A quote that sums up what matters most to the persona as it relates to your site.** Jordyn is young and eager to learn how to build his first computer.

### Persona #2

- **Fictional name:** River Jacobs
- **Age:** 40
- **Education:** University Educated
- **Ethnicity:** White British
- **Family Status:** Married.
- **Job title:** Radio Engineer
- **IT/ domain experience:** Excellent has been using computers since he was 5 years old.
- **Personality:** Computer Hobbyist
- **The goals and tasks they are trying to complete using the site:** River, wants to be able to offer his knowledge to other users on the site, he is also a collector of the computers from his childhood.
- **How often are they likely to use the site?** River may visit the site a couple of nights a week.
- **A quote that sums up what matters most to the persona as it relates to your site.** River wants to help teach the young computer enthusiasts on the site.

### Persona #3

- **Fictional name:** Holly Ratke
- **Age:** 25
- **Education:** College Educated
- **Ethnicity:** White British
- **Family Status:** In a relationship.
- **Job title:** Computer Builder for a local computer store
- **IT/ domain experience:** Excellent has been using computers since she was 8 years old.
- **Personality:** Computer Enthusiast.
- **The goals and tasks they are trying to complete using the site:** Holly, wants to be able to offer her knowledge on how to build computers to other users on the site, she also wants a place to share of her computer builds.
- **How often are they likely to use the site?** Holly will sign in, frequently throughout the week
- **A quote that sums up what matters most to the persona as it relates to your site.** Holly wants to show off her cool computer builds on the website.

### Actions the personas may carryout

- As a computer enthusiast/builder, I want to create a blog and share my computer building experience as the builds progress.
- As a computer enthusiast/builder, I want to have a place where I can get Q&A on computers in general as well as any difficulties I’m having with my computer.
- As a computer enthusiast/builder, I want to be able to support the website by donating to the creators.
- As a computer enthusiast/builder, I want the ability to have a profile on the site.
- As a computer enthusiast/builder, I want an easy way to log in and out of the website.

### Mockups

I also created some mockups of the site which can be viewed in the folder named 'mockups' of this GitHub repository.

## Features

### Existing Features

- Authentication mechanism.
- E-commerce functionality
- SQL database connection using Django's ORM
- Responsive UI
- Disqus Integration
- Blog functionality
- Forum functionality

### Features left to implement

- None

### Known Issues

As per the guidelines I used Disqus to integrate comments into the blog, however even though as you will see it is setup correctly in my settings
Disqus has an issue loading. I tried a number of troubleshooting guidelies however none seemed to work, such as added the website URL to the trusted domains.

I therefore contacted Tutor support and spoke to Nakita who advised that Disqus is know to have issues and experienced herself it working for one user
and not another. Nakita also advised that this is why it has been taken out of the new LMS.


## Technologies Used

- HTML5
  - This provides the basic layout for the pages.
- CSS3
  - I have used some custom css to build on top the styling provided by Bootstrap.
- [Bootstrap](https://getbootstrap.com)
  - I have used bootstrap to give my website a clean and responsive layout.
- JavaScript
  - I have used JavaScript to enhance the users interaction with the website.
- [Django](https://www.djangoproject.com/)
  - I have used the Django framework to build this website as using a framework provides several advantages such as:
    - Frameworks reduce time and effort acquired from common and repetitive tasks.
    - Django incorporates the Don't Repeat Yourself (DRY) philosophy.
    - Frameworks speed up development.
- [Python](https://www.python.org/)
- [Heroku](https://www.heroku.com/)
  - Used to deploy and host the dashboard.
- [gunicorn](http://gunicorn.org/)
  - Used for running HTTP servers on UNIX based operating systems as Heroku uses Ubuntu Server.
- [ClearDB MySQL](https://elements.heroku.com/addons/cleardb)
  - I used ClearDB MySql to host my database on Heroku.
- django-flatpages app
  - I used flatpages for my about page.
- [Amazon AWS S3](https://aws.amazon.com/)
  - I used an AWS s3 bucket to host my static files and user uploaded images as I ran into difficulties with Heroku.
- [Disqus API](https://disqus.com/)
  - I used disqus for the blog comments.
- [Stripe](https://stripe.com/gb)
  - I used Stripe so that users can make donations to the website. This is only setup however to take test payments so please use one of
    test cards found [here](https://stripe.com/docs/testing#cards).
- [django-contact-form](https://django-contact-form.readthedocs.io/en/latest/index.html)
  - I used this so that users are able to send me an email using a contact form.
- [django-tinymce](https://django-tinymce.readthedocs.io/en/latest/)
  - I used this module to enhance the textareas of the forum
- [django-emoticons](https://pypi.org/project/django-emoticons/)
  - I used this so that when a user types a smiley face they will be presented with an emoticon.
- [django-forms-bootstrap](https://pypi.org/project/django-forms-bootstrap/)
  - I used this module to provide better looking forms on the site.
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
  - I used this during development to aid in debugging.

## Testing

For the dashboard I haven't automated any tests however I carried out scenario based tests to ensure that the site works as user may expect it to. The scenarios are listed below:

### Scenario One: User Registration

#### Scenario Steps

1. From the home page, click register
2. fill in the form and press "create account"
3. user should then be redirected to their profile page.

#### Desired Outcomes

If successful the user should be able to register and be redirected to their user profile.

### Scenario Two: User changes Avatar

#### Scenario Steps

1. From their profile page, user clicks on upload new avatar
2. User will then be presented with an upload field.
3. User selects new image and selects "upload new image" button.
4. User is then redirected back to profile page with new avatar displayed.

#### Desired Outcomes

If successful the user should be able to upload a new avatar and be redirected to their home page.

### Scenario Three: User changes password

#### Scenario Steps

1. From their profile page, user fills in "Update Password" form and selects "Update Password" button.
2. User will then be asked to re-authenticate their credentials.
3. User is then redirected back to their profile.

#### Desired Outcomes

If successful the user should be able to reset their password.

### Scenario Four: User Donation

#### Scenario Steps

1. User clicks on Donate button from navigation bar.
2. User fills in form using the [stripe test details](https://stripe.com/docs/testing#cards) and presses confirm donation.
3. User is taken back to their profile page.

#### Desired Outcomes

If successful the user should be able to make a donation.

### Scenario Five: Blog

#### Scenario Steps

1. User clicks on Blog button from navigation bar.
2. Use is presented with blog posts from other users.
3. User should not be able to see their profile picture next to the blog posts if they are not the author.
4. User clicks on "Read more" button and should be taken to post detail. If they are not the author they should not be able to edit the post.
5. User clicks back to blog, once there clicks on "New post".
6. User should be able to fill in new form, upload a picture, set a tag and then after pressing "Save" be taken to the post they just created.
7. As this is their post they should also be able to edit the post.

#### Desired Outcomes

If successful the user should be able to carry out the actions above without any errors.

### Scenario Six: Forum

#### Scenario Steps

1. User clicks on Forum button from navigation bar.
2. Use is presented with forum subject along with the number of threads and posts in each subject.
3. If a user clicks on subject they should be taken to a page where they can see a subjects threads.
4. If they select a thread they will be taken to a "posts page" where they should be able to see details about the thread and any comments.
5. They should be able to click "New post" and submit a comment.
6. They will then be redirected to the "Posts" page and they should be able to only edit or delete their own comments.

#### Desired Outcomes

If successful the user should be able to carry out the actions above without any errors.

### Scenario Seven: About Page

#### Scenario Steps

1. User clicks on About button from navigation bar.
2. User can see the about page.

#### Desired Outcomes

If successful the user should be able to see the about page.

### Scenario Eight: Contact Form

#### Scenario Steps

1. User clicks on the Contact button from the navigation bar.
2. User is presented with a contact form.
3. If the user clicks submit they should be asked to fill in forms marked with a red asterisks.
4. If the user fills in the form they should be presented with a success message.

#### Desired Outcomes

If successful the user should be able to carry out the actions above without any errors and I should receive an email.

### Scenario Nine: Logging Out

#### Scenario Steps

1. User clicks on profile > logout from the navigation bar.
2. User is taken to the home page with a success message that they are logged out.

#### Desired Outcomes

If successful the user should be logged out.

### Scenario Ten: User can't access donations if not authenticated

#### Scenario Steps

1. Whilst logged out of the site user selects "Donate" from the Navigation Bar.
2. User is redirected to the login page.

#### Desired Outcomes

If successful the user should be redirected to the login page.

## Deployment

For this project I deployed the code to Heroku using the steps below.

### Separated Online code from Offline code

So to begin with I created a new settings directory at the root of the project. This directory holds 4 files:

- `__init__.py`: This is an empty file that informs Python that the directory should be considered a Python package.
- `base.py`: This file contains our base settings
- `dev.py`: This imports the base settings and adds settings for the development environment.
- `staging.py`: This imports the base settings and adds settings for the staging environment.

I then went on to create the necessary requirements files placing them in a new directory called requirements. I also added a requirements.txt to the project
for deployment to Heroku.

### Setting up Heroku

1. I headed over to Heroku and set up a new app called "the-pc-hobbyist".
2. Once that was completed I updated my `staging.py` settings to include the app url.
3. I added gunicorn to my `requirements/base.txt`.
4. I ran `pip install -r requirements/dev.txt` to make sure that all of the development dependencies were installed.
5. I created a new file called Procfile and added `web: gunicorn stream3_prj.wsgi:application`.
6. I created a runtime.txt file and added `python-2.7.15`.
7. I then created a Procfile.local and added `web: gunicorn stream3_prj.wsgi:application`.
8. Then I ran the following command in Bash: `export DJANGO_SETTINGS_MODULE=settings.dev`
9. Then I ran `heroku local -f Procfile.local` to test that I could still see the website on localhost.
10. I then pushed my changes to GitHub, connected Heroku to Github as the deployment method and enbaled automatic deploys.
11. From the command line, I logged into Heroku and ran the following commands:
    1. `heroku config:set DJANGO_SETTINGS_MODULE=settings.staging --app the-pc-hobbyist` to set the environment on Heroku.
    2. `heroku config:set DISABLE_COLLECTSTATIC=1 --app YOUR_HEROKU_APP` to prevent static collection.
    3. `heroku ps:scale web=1 --app YOUR_HEROKU_APP` to start my dyno.
12. I was then able to run `heroku open --app the-pc-hobbyist` and see the project open in my browser.

### Hosting the MySQL database

To host he MySQL database I did the following:

1. On heroku I provisioned ClearDB MySQL. Once provisioned I deleted `reconnect=true` from the `CLEARDB_DATABASE_URL` config variables.
2. I then added `dj-database-url==0.2.1` to requirements/staging.txt and updated the settings/staging.py for my `DATABASES` setting.
3. From the command line I then logged into Heroku and ran the following command to run migrations and generate the tables: `heroku run --app the-pc-hobbyist python manage.py migrate --settings=settings.staging`.
4. Then to populat the database I ran this command to dump the data from the local database into a json file: `python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission --indent=4 > db.json --settings=settings.dev`.
5. Once that was completed I pushed the newly created `db.json` file up to GitHub and ran this command `heroku run --app the-pc-hobbyist python manage.py loaddata db.json --settings=settings.staging` to load the data into the hosted database.

### Static files

In order to organise my static files I carried out the following steps:

1. I added `whitenoise==3.2` to requirements/base.txt and ran `pip install -r requirements/base.txt` to install it.
2. I then altered the `wsgi.py` file to use `whitenoise`.
3. Finally I ran the following from the command line: `heroku config:unset DISABLE_COLLECTSTATIC=1 --app the-pc-hobbyist` so that on the next build Heroku will run the `collectstatic` command.

## Credits

### Content

- The font was provided by [Google fonts](https://fonts.google.com/) and can be found [here](https://fonts.google.com/specimen/Press+Start+2P).
- All the icons were provided by [Font Awesome](https://fontawesome.com/).

### Acknowledgements

In my acknowledgements no code was copied from these sources and all code was written by me. These are a mention of people/websites that provided me with guidance and I was able to adapt the knowledge of their lessons into my own code.

- [Code Institute](https://www.codeinstitute.net/) and my Mentor for providing me the skills, inspiration and direction to build this Dashboard.
- Code Institute students - They were very helpful at pointing me in the right direction when I couldn't get something working. All code is my own.
- [Dan Poirier's AWS guide](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/) - This was instrumental in getting AWS to work.
- [This](https://stackoverflow.com/questions/22567320/django-edit-user-profile) Stack Overflow post for guiding me in the right direction for the password reset form again no code was copied.
- [This](https://stackoverflow.com/questions/28504753/html5-img-tag-alternative-image#28504867) Stack Overflow post for inspiring me on to setup an alternative image function.
- [This](https://stackoverflow.com/questions/20010108/checking-if-username-exists-in-django) Stack Overflow post for inspiring me on how to check if a username exists in my current database.