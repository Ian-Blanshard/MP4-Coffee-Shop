# MP4-Coffee-Shop

![Screenshot of store](/static/images/site_hompage.jpg)

Coffee shop is a fictional e-commerce store, created to practice my full-stack web development skills. 

Live version of site hosted on Heroku [here](https://coffee-shop-mp4-a883163ad215.herokuapp.com/)

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

![Screenshot database schema](/static/images/database_schema.jpg)

The initial schema was what I began with when designing the site, But there ended up being some changes. I put this down to my experience as having never built out a full e-commerce store I hadn't understood some of the challenges I would be faced with if I had stuck rigourously to this design.

***

### Wireframes <a name="wireframes"></a>

The wireframes for the site were my starting point, as the project progressed I decided to make some changes from the initial designs as I thought they were more user friendly and provided easier customer navigation of the site.

#### Homepage

![Homepage wireframe](/static/images/homepage-wireframe.jpg)

***

#### Products page

![Products page wireframe](/images/products_wireframe.jpg)

***

#### Single product page

![Products page wireframe](/static/images/single_product_wireframe.jpg)

***

#### Shopping bag page

![Shopping bag page wireframe](/static/images/shopping_bag_wireframe.jpg)

***

#### Submit review page

![Submit review page wireframe](/static/images/submit_review_wireframe.jpg)

***

#### Product reviews page

![Submit review page wireframe](/static/images/product_reviews_wireframe.jpg)

***

#### Profile page

![Profile page wireframe](/static/images/profile_wireframe.jpg)

***

### Colour Scheme and Font <a name="styles"></a>

#### The color scheme for the site

The colour scheme for the site is a simple black and white style, this was what I began building the site with and as I added features I thought it looked nice and kept the store user friendly. Although if I had more time I would have like to experiment with other options. I chose to focus on building the features of the store.

#### The fonts used for the site

The fonts used for the site were from google fonts.

I chose a serif font 'Lobster' for some of the titles.

I chose a sans-serif font 'Lato' for the majority of the site, including the part in which readability was of high importance, such as checkout pages.

Both fonts have fallbacks of serif and sans-serif in case there was an issues with font loading or support.

<br>

## Features <a name="features"></a>

### Database <a name="database"></a>

#### CRUD Functionality 

My app demonstrates CRUD functionality as outlined below:

#### Create:

- Creating users accounts
- Creating users orders
- Creating products
- Creating reviews

#### Read:

- Reading user orders to display to user
- Reading products to display to user
- Reading reviews to display to user

#### Update:

- Allowing users to edit their reviews
- Allowing superuser to update product info
- Allowing users to update their saved delivery info

#### Delete:

- Allowing superuser to delete products
- Allowing superuser to delete reviews

***

### Feature <a name="feature"></a>

### All user features

***

#### Navbar

![Full screen navbar](/static/images/full_screen_navbar.jpg)
The nave bar allows user to navigate the page, the coffee shop logo will return users to the homepage, the profile icon contains a dropdown with all the profile related links and the shopping basket contains one with all the shopping bag related links.

The superuser will have additonal links avaiable to them inside these menus, these are not visible to other users and even if the url is typed in directly they are not accessible to to others.

There is also quick links to the products of each category in a secondary bar.

***

#### Mobile navbar

![Mobile navbar](/static/images/mobile_navbar_collapsed.jpg)

![Mobile navbar](/static/images/mobile_navbar_expanded.jpg)

The mobile navbar is designed differently to allow users to better navigate the site on mobile devices and consists of a series of dropdown menus, all of the functionality of the normal navbar is available.

***
#### Homepage

The home page contains a hero image and some introductory text for the user which explains the purpose of the site.

![Full screen Homepage](/static/images/home_page.jpg)

It also contains three sections containing information about the store allowing users to see information about the business.

![Full screen Homepage 2](/static/images/home_page1.jpg)

These stack on mobile screen sizes due to the responsive design.

![Mobile Homepage](/static/images/home_page_mobile.jpg)

***

#### Products page

The products page display all products to the user.

It also contains features to view products by category or to search for terms which will display products which have the search term in both there name and description.

![Products page](/static/images/products_page.jpg)

The user can see the following product details for each prodcut displayed:
product image, its price (including any discounts), its average review rating and category. The user can click the view products details page to see further information on the product.

The product page also has a sort button which will sort product either by price or ratings in both descending and ascending orders.

![Products page](/static/images/products_page_2.jpg)

***

#### Products detail page

The products detail page contains more information on the product for the customer in the description, it also displays the average customer ratings as stars and a link to view all the customer reviews for this product.

![Products detail page](/static/images/products_detail_page.jpg)

If the product is a current promotion product a star is visible which contains the text of how much the product is reduced by as a percentage.

On this page the customer can select a quantity and add this selected quantity to their shopping bag.

There is a button to return back to the product page.

***

#### Customer reviews page

The customer reviews page displays all the reviews from that current product, it shows the stars of the review and also the comment if one was left. 

![customer reviews page](/static/images/customer_reviews_page.jpg)

If the customer is logged in they have a button which can take them to a form to leave there own review of the product. They are also able to edit previous reviews of theirs.

At the bottom of the page a button is available to navigate back to the product.

***

#### Shopping bag

![shopping bag page](/static/images/shopping_bag.jpg)

The shopping bage page allows users to see a summary of all the items in their bag, update quantities or delete itemes from thier bag. 

They can also continue to the checkout page or return to the products page to continue shopping

***

#### Checkout page

![checkout page](/static/images/checkoutpage.jpg)

The checkout page is the page where the user can fill out all the required details to complete thier order, it has a stripe card field which allows payment to be taken.

There is a summary of the order so they can ensure the correct items are in the bag.

![checkout page](/static/images/checkoutpage1.jpg)

***

#### Checkout success page

![checkout success page](/static/images/checkout_success.jpg)

The checkout success page is displayed when the user has successfully purchased their products in contains all the details about the order for them to view.

***

#### Toasts 

Toasts are used across the site to ensure users are aware that actions they have taken have been succesful, user feedback is essential to the functioning of the site.
Below are a small example of some of them

![toast](/static/images/toast.jpg)
![toast](/static/images/toast1.jpg)
![toast](/static/images/toast2.jpg)
![toast](/static/images/toast3.jpg)

***

#### 404 page

The 404 page is designed to show when the page the user is trying to view can't be returned, for example if they enter an incorrect URL, the page has been moved or deleted, or there is a broken link. The 404 page contains some simple text and a button to return the user to the homepage. 

![404 page](/static/images/404_page.jpg)

#### Stripe webhook handlers

To ensure the integrity of the checkout process, I implemented custom webhook handlers that monitor payment events from Stripe. Even if an error occurs during the order submission, such as a failure in processing the checkout or saving order details, the webhook ensures that the order is still created, provided the payment was successful.

***

### Users with accounts features 

#### My profile page 

The my profile is a page for users which have set up logins, it contains a place for them to enter/ update their default delivery details which will be automatically entered for them at the checkout.

It also contains details of all their previous orders, which have links that take them to the checkout success page which they were shown after completing the purchase which has all the details.

![profile page](/static/images/profile.jpg)

***

#### Add product reviews

![add review page](/static/images/add_review_page.jpg)

The add product reviews page is the form for users to add a review for products which all other users on the site can see to help them decide on which products to purchase.

They can enter a rating of the product and also an optional text comment about the product.

***

### Superuser features

#### Manage promotions

![manage promotions page](/static/images/manage_promotions.jpg)

The manage promotions page is a page specific to superusers it allows the owner of the site to change products which are on offer, applying a percentage discount to their price.

They are taken to a seperate page with a form when they have chosen which product they would like to edit the price of.

![manage promotions page](/static/images/manage_promotions1.jpg)

***

#### Add products to store page

![add products](/static/images/add_product.jpg)

The add products page is a form for superusers to add products to the store, it also allows them to upload product images. The same form is used for the edit product page, but in these instances it loads the form with all the product details already filled.

***

#### Manage reviews

![manage reviews](/static/images/manage_reviews.jpg)


The manage reviews page is a page in which the superuser can view all current product reviews and delete or edit ones they see fit, it allows the store owner to make sure only suitable reviews are visible to customers.

***

<br>


## Technologies used <a name="technologies-used"></a>


This Project uses the following languages:

* HTML
* CSS
* JavaScript
* Python

[PostgreSQL](https://www.postgresql.org/) was used as the database to store and manage application data.

[Amazon webservices s3](https://aws.amazon.com/s3/) was used to store static files and media for my site.

[Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control and as a repository.

[Google Fonts](https://fonts.google.com/) was used to browse, select and as a source of the font I used on this site.

[FontAwesome](https://fontawesome.com/) was used for social media icons in the footer.

[favicon.io](https://favicon.io/) was used to create the favicon for my site.

Please see the requirements.txt for a full list of the packages used and versions in my project.

<br>

## Credits <a name="credits"></a>

When creating my project I frequently used the docs for

- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

- [Django allauth](https://django-allauth.readthedocs.io/en/latest/)

- [Django](https://docs.djangoproject.com/en/5.1/)

- [Django GitHub](https://github.com/django/django)

- [Stripe](https://docs.stripe.com/)


In addition to these the following sites/tutorials/blogs were useful:

[This codepen](https://codepen.io/akku_186/pen/BaGRQwg) code was useful to learn how to create the mobile collapsing navbar, the code was modified to suit my specific needs.

[This tutorial](https://www.geeksforgeeks.org/how-to-change-hamburger-toggler-color-in-bootstrap/) was useful for customising the hamburger toggler.

The image for the background of index.html is by Raymond Petrik Devlin from [Pexels](https://www.pexels.com/photo/rich-roasted-coffee-beans-texture-background-28742831/)

I used [chatGPT](https://chatgpt.com/) to create the product images by giving it the prodcut descriptions as prompts.

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