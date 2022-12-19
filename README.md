[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9569051&assignment_repo_type=AssignmentRepo)

![CD](https://github.com/software-students-fall2022/
final-project-project5-team4/actions/workflows/docker-image.yml/badge.svg)
![web-app](https://github.com/software-students-fall2022/
final-project-project5-team4/actions/workflows/web-app.yml/badge.svg)

# Final Project

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.

## Introduction

This web-app is an apartment searching app just like Streeteasy but better. (Think of streeteasy + ratemyprofessor!) We allow users to search for apartments in New York based on different filters such as boroughs or price range and more. However, the most important feature that we provide is for users to check the ratings and reviews of the apartments uploaded by the previous tenants. Users can check those reviews from the previous tenants and save the apartments that fit their conditions and interest.

## Deployed Web App

- [Admin] (https://rate-my-apartment-nyc-admin-3g66f.ondigitalocean.app/)
- [User] (https://rate-my-apartment-nyc-o3klv.ondigitalocean.app/)

## DockerHub Container

- [Admin] (https://hub.docker.com/repository/docker/viczzzzz/ratemyapartmentnycadmin)
- [User] (https://hub.docker.com/repository/docker/viczzzzz/ratemyapartmentnyc)

## Features for Web App (User)

- Signup & Login
  - Users can register for a new account and login to use every feature of the service. Users can also continue as guest and still have access to the apartments. Some of the features will be only available to logged in users, however.
- Search for apartments
  - Users can search for apartments specifying the boroughs and price range.
  - User can also search for specific apartments using the address.
- List of apartments
  - Once the users search apartments using its address or its price and boroughs, it'll show the apartments that fulfill those conditions.
- Search More (Advanced Search)
  - If users want to reset the filters, they can click Search More button.
  - A modal window will allow users to reset the boroughs and price as well as some of the advanced search options such as elevator, pet-friendly, laundry, doorman etc.
- View Apartment Info
  - Users can click a single card and this will direct to a page that shows all information about that single apartment.
  - In this page, we have several other features such as see all reviews and ratings, add reviews, and save as favorite.
- Reviews & Ratings
  - Users will be able to see the reviews and ratings from other tenants or users.
  - Since the price for the apartment can vary, once the reviewers add the price and rating, it will show the avarage price and avarage rating for all added reviews.
- Add Reviews
  - Logged in users can also add a new review for a single apartment.
  - Once they click Add Review button, it'll direct the users to a page where they can leave comments, price, and rating.
- Save favorite apartments
  - Logged in users can also save the apartments that they are interested in by clickinng the heart icon.
- Account (Only available to logged in users)
  - Loggied in users can click the Account button and see all apartments they saved and all reviews they have added.

## Features for Web App (Admin)

- Signup & Login
  - It is required for any admin who wants to add their apartments that are not on the listing to make a new account and sign in.
- Add Apartments
  - Admins can make add a new apartment that would show on the web app for user if their apartments are not on the list of the current apartments.
  - Admin users type in the information for the apartment and click a add button. Then it will show up on the apartment list for the web app for users.

## How to Run Pytests

### 1. Go to the directory you want to test

#### Web app

Go to the web-app directory

```
cd web-app
```

#### Web App Admin

Go to the web app admin directory

```
cd web-app-admin
```

### 3. Install dependencies

Install the dependencies to run pytest by using the following command line

```
pip install -r requirements.txt
```

### 4. Run pytest

Run the following command line. Make sure pytest is downloaded (`pip install pytest`)

```
coverage run --omit */site-packages/* -m pytest
```

### 5. Check the code coverage report

Run the following commannd line to see the code coverage report

```
coverage report -m
```

## Authors

- Victoria Zhang: [Github](https://github.com/Ruixi-Zhang)
- Jenny Shen: [Github](https://github.com/JennyShen10792)
- Tiffany Lee: [Github](https://github.com/les5185)
- Leah Durrett: [Github](https://github.com/howtofly-lab)
- Ian Liao: [Github](https://github.com/ian-Liaozy)
- Charlie Xiang: [Github](https://github.com/xiang-charlie)
