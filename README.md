## social-media-app
# A social media website using Django web framework

![dashboard.png](bookmarks%2Faccount%2Fstatic%2Fdashboard.png)
![login.png](bookmarks%2Faccount%2Fstatic%2Flogin.png)
![register.png](bookmarks%2Faccount%2Fstatic%2Fregister.png)
![images.png](bookmarks%2Faccount%2Fstatic%2Fimages.png)

### 🚀 Overview
The social media app allows user to register to the website, share images, get and send likes and 
have an activity stream systems to track user's interactions between eatch other.

### 🍁 Model definition
![db.png](bookmarks%2Faccount%2Fstatic%2Fdb.png)

### ✨ Features
 - Create/register an account using both Oauth integration through facebok/twitter or using django authentication framework
 - Login/logout, edit/update profile, update profile picture using custom model
 - Password reset mechanism using django email backend
 - Use a bookmarklet js to save images from different websites and have them loaded on backend
 - Defined asynchronous "send/get likes" system using AJAX calls to send/receive likes interacting with the DOM
 - Implemented infinite scrolling/paginator to list images on the same page
 - Defined proper modelling to allow users to be followed by multiple friends and vice/versa
 - Implemented generic activity stream to follow user's daily activities who they followed/what they liked
 - Implemented generic foreign key model and contenttypes defining a verb like 'follow' 'likes' to be able to interact with multiple models
 - Utilized django signals to receive updates on total likes count coming from m2m model update and modify global counter consequently
 - Optimised django queries using multiple techniques like indexes, select related and prefetch
 - used redis as in memory storage to collect data about total views on single images and ranking displaying the most viewed images

### 🚀 Technology Stack
- python 3.9
- django 4.0
- sqlite
- html/css/javascript/AJAX
- docker
- redis
- Werkzeug
- django-social-auth "Oauth"
- thumbnails
- Pillow 
- django debug toolbar


### 🔎 TODO
- re-style using Tailwind
- implement proper frontend using react