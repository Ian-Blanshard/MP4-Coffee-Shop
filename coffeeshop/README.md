# MP4-Coffee-Shop

![Screenshot of store on different devices]()

Coffee shop is a  

Live version of site hosted on Heroku [here]()

***

## Contents

1 [User Experience (UX)](#UX)

  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Database schema](#database-schema)
  * [Wireframes](#wireframes)
  * [Color Scheme and Font](#styles)


2 [Features](#features)

 * [Database](#database)
 * [Feature](#feature)



3 [Technologies Used](#technologies-used)

4 [Credits](#credits)

4 [Testing](#testing)

5 [Deployment](#deployment)

<br>
<br>

## User Experience (UX) <a name="UX"></a>

### Project Goals <a name="project-goals"></a>

***

### User stories <a name="user-stories"></a>

#### Site Visitor

A site visitor is someone who has found the site and is not yet decided whether they are going to be a customer, ultimately the site goal is to convert this type of user into a customer.

As a | I want to |  So that I can 
-------|-------|-------
Visitor | Understand the purpose of the site immediately upon visiting | Decide whether to stay on the site and become a shopper.
Visitor | Find information about the company and its values and products | Decide whether their values and products are suitable for me to purchase 
Visitor | Use a site which has a responsive design | I can use the site on all of the devices I own 
Visitor | Be able to easily understand what information is available on the site and how to find it  | Navigate to the information/ services which interest me
Visitor | Be presented with eaily recongisable links to the companies social media | Connect with the company on social media to learn about the latest information 
Visitor | Easily find a method to contact the company should I have further queries about products or services | Get a quick response to my queries, enabling me to make decisions 
Visitor | Receive feedback when using features of the site | Know whether the actions I have taken on the site have been succesful

#### Casual Customer

A casual customer is someone who wants to purchase an item from the site as a first purchase and/or a one off, the site goal is to convert these types of customers to return/ regular customers

As a | I want to |  So that I can 
-------|-------|-------
Casual customer | View all products available | Select products to purchase
Casual customer | View product by categories | Browse a selection of products which i may be interested in without having to look through all products
Casual customer | Search for a product | Quickly purchase a particular product 
Casual customer | View full details for a single product | See an image, description, reviews and price of a product before purchase
Casual customer | Be able to see all products which have offers on them | Purchase product which have an offer price
Casual customer | Add items to a shopping bag | Purchase a number of items at once
Casual customer | View the content of my shopping bag | review and make changes to my selections prior to purchase
Casual customer | Be able to checkout securely without making a user account | Quickly make a purchase from the site
Casual customer | View a confirmation of my order after purchase | Ensure the purchase has been succesful and contains the correct items
Casual customer | Receive a confirmation email on the completion of my order | Keep a record of the succesful order and the items it contains
Casual customer | Have the options to use my details to create an account during checkout | Become a regular customer if I decide to 

#### Regular Customer

A regular customer is someone who uses the site often, having multiple purchases. They have many of the same requirements as a casual customer but want a more in depth experience. The site goal is to keep these customers engaged and retain their custom. 

As a | I want to |  So that I can 
-------|-------|-------
Regular customer | Register for a user account | Have a profile to use while browsing and purchasing from the site
Regular customer | Be able to log in and out of my account | Securely access my account information
Regular customer | Receive a confirmation email upon account registration | Verify that my account was created correctly and linked to my email 
Regular customer | Recover my password | Regain access to my account if i lose/forget my password
Regular customer | Save my personal information required when ordering | Checkout more easily when I am making further purchases
Regular customer | Update my user profile | Keep my personal details up to date
Regular customer | See a history of my previous orders | Quickly locate and purchase again items I have previously purchased
Regular customer | Be able to review products I have purchased | Give feedback on products for other users to see
Regular customer | Be able to delete/edit my reviews | Change my review if I made mistakes and/or change my view
Regular customer | Receive recommendations of products I may be interested in | Purchase products which are recommended for customers who have purchased products which I have
Regular customer | Have exclusive offers for being a regular customer | Feel valued as a regular customer and make savings 


#### Site Admin

The site admin is the user who is using the site to sell their products, they want a simple interface to deal with managing the e-commerce side of thier business

As a | I want to |  So that I can 
-------|-------|-------
Site admin | Add a product | Update my store with new products as I source them
Site admin | Edit a product | Update details/price for a product if they need changing
Site admin | Delete a product | Remove a product from the store if I no longer want to sell it
Site admin | Add offers to products | Promote a product of my choice to customers
Site admin | See the stock levels for products | Correctly manage my inventory and order stock as required
Site admin | Review customer product reviews | Ensure reviews are appropriate for the site and are not malicious


<br>

***

### Database schema <a name="database-schema"></a>

[Lucid chart](www.lucidchart.com) was used to create a database schema and wireframes for the project. This ensured I had a clear vision for the project before beginning to write code.

As I am using django/ django allauths models for managing users and login. The schema focusses on modals I created for managing products, shopping bags and reviews.

![Screenshot database schema](/coffeeshop/static/images/database_schema.jpg)

***

### Wireframes <a name="wireframes"></a>

#### Homepage

![Homepage wireframe](/coffeeshop/static/images/homepage-wireframe.jpg)

***

#### Products page

![Products page wireframe](/coffeeshop/static/images/products_wireframe.jpg)

***

#### Single product page

![Products page wireframe](/coffeeshop/static/images/single_product_wireframe.jpg)

***

#### Shopping bag page

![Shopping bag page wireframe](/coffeeshop/static/images/shopping_bag_wireframe.jpg)

***

#### Submit review page

![Submit review page wireframe](/coffeeshop/static/images/submit_review_wireframe.jpg)

***

#### Product reviews page

![Submit review page wireframe](/coffeeshop/static/images/product_reviews_wireframe.jpg)

***

#### Profile page

![Profile page wireframe](/coffeeshop/static/images/profile_wireframe.jpg)

***

### Colour Scheme and Font <a name="styles"></a>

#### The color scheme for the site

#### The font used for the site

<br>

## Features <a name="features"></a>



### Database <a name="database"></a>

#### CRUD Functionality 

My app demonstrates CRUD functionality as outlined below:

#### Create:

#### Read:

#### Update:

#### Delete:

***

### Feature <a name="feature"></a>

***

#### 404 page

The 404 page is designed to show when the page the user is trying to view can't be returned, for example if they enter an incorrect URL, the page has been moved or deleted, or there is a broken link. The 404 page contains the navbar, some simple text and a button to return the user to the homepage. 

![404 page]()

<br>


## Technologies used <a name="technologies-used"></a>


This Project uses the following languages:

* HTML
* CSS
* JavaScript
* Python

[PostgreSQL](https://www.postgresql.org/) was used as the database to store and manage application data.

Please see the requirements.txt for a full list of the packages used and versions in my project.

<br>

## Credits <a name="credits"></a>

When creating my project I frequently used the docs for
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

In addition to these the following sites/tutorials/blogs were useful:

<br>

## Testing  <a name="testing"></a>

Testing was performed and documented in detail in a separate file.

The testing documentation can be viewed [here](/TESTING.md)

<br>

## Deployment

This project was developed using Microsoft Visual Studio Code, committed to Git and pushed to GitHub using the terminal with in VS code.

The final Live version of site is hosted on Heroku and can be found [here]()

###  Deploying to Heroku

The project was deployed to Heroku, below are the steps taken:

1. Create a requirements.txt file.
pip freeze --local > requirements.txt

2. Create a Procfile details on [heroku here](https://devcenter.heroku.com/articles/procfile#:~:text=The%20Procfile%201%20Procfile%20naming%20and%20location%20The,type%20examples%20...%207%20Procfile%20and%20heroku.yml%20).

3. Add and commit the changes with git, and push the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the new button in your dashboard. 

5. Confirm the linking of the Heroku app to the correct GitHub repository.

6. In the Heroku dashboard for the application, click on settings then reveal config vars and set up the configs.

7. From the Heroku dashboard of your newly created application, click deploy then deployment Method and select GitHub.

8. In the manual deployment section of this page, make sure the master branch is selected and then click deploy branch.

9. On the Heroku dashboard, click deploy.

10. Open the console on Heroku and run a python3 terminal, create the db using db.create_all()