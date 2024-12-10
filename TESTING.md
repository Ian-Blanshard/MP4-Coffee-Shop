  # Testing Coffee shop
  ***
  ## Contents
  
  * [Code Validation](#code-validation)
    * [CSS code validation](#css-validation)
    * [HTML code validation](#html-validation)
    * [JavaScript validation](#javascript-validation)
    * [python code validation](#python-validation)

  * [Manual Testing](#manual-testing)
    * [Testing across different devices and browsers](#testing-across-different-devices-and-browsers)
    * [Testing user stories](#testing-user-stories)
  * [Bugs](#bugs)

  * [Testing Stories](#testing-user-stories)

***

### Code validation <a name="code-validation"></a>

#### CSS validation <a name="css-validation"></a>

My CSS code passed validation with no errors

![CSS validation](/static/images/css_validation.jpg)

#### HTML validation <a name="html-validation"></a>

My HTML showed a variety of errors during validation.

One img element didn't have a alt.

![HTML validation before 1](/static/images/html_code_validation2.jpg)

One of the select elements in a cripsy form had a placeholder.

![HTML validation before 2](/static/images/html_code_validation3.jpg)

I had a duplicate ID because of the way i was using cripsy forms with in a template loop.

![HTML validation before 3](/static/images/html_code_validation4.jpg)

I had a anchor element in a ul which wasn't contained with in a li element.

![HTML validation before 3](/static/images/screenshot_html_validation.jpg)

I rectified all these issues and my code passed as can be seen below

![HTML validation after](/static/images/html_code_validation.jpg)


#### JavaScript validation <a name="javascript-validation"></a>


My JavaScript passed validation, it had one undefined variable, but this was Stripe which would be made available from the stripe cdn, which was contained in a HTML script, which isn't loaded because i was just copying the JS code.

![JavaScript validation pass](/static/images/js_validation.jpg)

#### Python validation

The [Code Institute](https://pep8ci.herokuapp.com/#) python linter was used to ensure my
python code was PEP8 compliant

There were a number of errors which all related to either extra whitespace, lines of code which were too long or missing/excessive blank lines.

![python validation](/static/images/python_code_validation.jpg)

These were rectified and my code passed with no errors.

![python validation pass](/static/images/python_code_validation_passed.jpg)

***

### Manual testing <a name="manual-testing"></a>

#### Testing across different devices and browsers  <a name="testing-devices-browsers"></a>

Browser | Outcome | Pass/Fail  
--- | --- | ---
Google Chrome | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Microsoft Edge | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Mozilla Firefox | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Apple Safari | Site functioned as expected, design appearance correct and responsive across different screen sizes, tested only on mobile screen size (iphone 12) | Pass

#### Testing site features  <a name="testing-site-features"></a>

##### Testing Navbar  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Login button | Clicking the login button loads the login form successfully | Pass  
Logout button | Clicking the logout button logs the user out and reloads the homepage | Pass  
Add product to store button | Clicking the button loads the add product form for the admin user | Pass  
Manage promotions button | Clicking the button loads the manage promotions page for the admin user | Pass  
Manage reviews button | Clicking the button loads the manage reviews page for the admin user | Pass  
My profile button | Clicking the button loads the user's profile page | Pass  
View shopping bag button | Clicking the button loads the shopping bag page | Pass  
Coffee shop logo link | Clicking the logo link reloads the homepage | Pass  
Search bar | Entering a query and pressing enter loads the search results page | Pass  
Ground coffee link | Clicking the link loads the ground coffee category page | Pass  
Coffee beans link | Clicking the link loads the coffee beans category page | Pass  
Accessories link | Clicking the link loads the accessories category page | Pass  
Special offers link | Clicking the link loads the special offers category page | Pass  

***

##### Testing Homepage  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
View all products button | Clicking the button loads the products page displaying all available products | Pass  
Page content | Page content loaded correctly and is visible to the user | Pass  
Store info cards | Store information cards are displayed correctly and provide relevant information to the user | Pass  

***
##### Testing Products Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Sort button (high to low) price | Clicking the button sorts products by price from highest to lowest | Pass  
Sort button (low to high) price | Clicking the button sorts products by price from lowest to highest | Pass  
Sort button (high to low) rating | Clicking the button sorts products by rating from highest to lowest | Pass  
Sort button (low to high) rating | Clicking the button sorts products by rating from lowest to highest | Pass  
Page content | Page content loaded correctly and is visible to the user | Pass  
View all products button | Clicking the button reloads the page displaying all available products | Pass  
View product details button | Clicking the button loads the product details page for the selected product | Pass  
Product image link (takes to product details page) | Clicking the product image link loads the product details page for the selected product | Pass  

***

##### Testing Products Detail Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page content loaded correctly and is visible to the user | Pass  
View customer reviews button | Clicking the button displays customer reviews for the product | Pass  
Add to shopping bag button | Clicking the button adds the selected product to the shopping bag | Pass  
Item quantity input | User can input and update the quantity of the product before adding it to the shopping bag | Pass  
Back to products button | Clicking the button navigates back to the products page | Pass  

***

##### Testing Customer Reviews Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page content loaded correctly and is visible to the user | Pass  
Customer reviews | Customer reviews load if they exist; if no reviews are available, a message stating "No reviews" is displayed | Pass  
Add review button | Clicking the button allows the user to add a new review for the product | Pass  

***

##### Testing Shopping Bag Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page content loaded correctly and is visible to the user | Pass  
Shopping bag items | Items in the shopping bag are displayed with correct details (name, price, quantity) | Pass  
Item quantity input | Users can update the quantity of an item directly in the shopping bag | Pass  
Delete item button | Clicking the delete button removes the corresponding item from the shopping bag | Pass  
Keep shopping button | Clicking the button redirects the user back to the products page to continue shopping | Pass  
Secure checkout button | Clicking the button takes the user to the secure checkout page | Pass  

***

##### Testing Checkout Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page content loaded correctly and is visible to the user | Pass  
Bag details | Bag details (items, prices, quantities, totals) are displayed accurately | Pass  
Checkout form | Users can fill out the checkout form with their delivery and payment information | Pass  
Save delivery information checkbox | Checking this box saves the user's delivery information for future use | Pass  
Edit bag button | Clicking the button redirects the user back to the shopping bag page to make changes | Pass  
Complete order button | Clicking the button submits the order and processes payment | Pass  
Order successfully created in admin | Order is visible in the admin panel after successful checkout | Pass  

***

##### Testing Checkout Success Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page content loaded correctly and is visible to the user | Pass  
Order successful toast | A toast message is displayed confirming the order was successful | Pass  
Order details correct | Order details (items, quantities, prices, totals, and delivery info) are displayed accurately | Pass  

***

##### Testing Webhook Handler  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Payment intent succeeded but order form not submitted | Order is still created successfully despite form submission failure | Pass  

***

##### Testing My Profile Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page loads correctly and displays all relevant information | Pass  
Default delivery information displayed | Default delivery information is shown correctly | Pass  
Default delivery information editing | User can edit and save changes to delivery information | Pass  
Order history | Order history is displayed correctly and links work to order details | Pass  

***

##### Testing Add Review Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page loads correctly and displays review form | Pass  
Review form | User can fill out and submit review form | Pass  
Add review button | Clicking the button successfully adds the review | Pass  

***

##### Testing Manage Promotions Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page loads correctly and displays promotions management options | Pass  
Edit discount button | Clicking the button opens the edit discount form | Pass  
Edit discount form | Form allows updating of discount details and saves changes correctly | Pass  

***

##### Testing Add to Store Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page loads correctly and displays options to add products | Pass  
Add a product form | Form displays fields for adding a new product | Pass  
Image uploading widget | Image widget allows user to upload product images successfully | Pass  
Add product button | Button successfully adds product to the store and saves the data | Pass  

***

##### Testing Manage Reviews Page  

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Page loads correctly and displays all reviews | Pass  
Delete review button | Button allows admin to delete reviews and updates list | Pass  

***

### Testing User Stories <a name="testing-user-stories"></a>

#### Testing for Site Visitor

A site visitor is someone who has found the site and is not yet decided whether they are going to be a customer. Ultimately, the site's goal is to convert this type of user into a customer.

| As a                | I want to                                               | So that I can                                                            | Pass/Fail |
|---------------------|--------------------------------------------------------|---------------------------------------------------------------------------|-----------|
| Visitor             | Understand the purpose of the site immediately upon visiting | Decide whether to stay on the site and become a shopper                   | Pass      |
| Visitor             | Find information about the company and its values and products | Decide whether their values and products are suitable for me to purchase  | Pass      |
| Visitor             | Use a site which has a responsive design                | I can use the site on all of the devices I own                             | Pass      |
| Visitor             | Be able to easily understand what information is available on the site and how to find it | Navigate to the information/services which interest me                    | Pass      |
| Visitor             | Be presented with easily recognizable links to the company's social media | Connect with the company on social media to learn about the latest information | Fail      |
| Visitor             | Easily find a method to contact the company should I have further queries about products or services | Get a quick response to my queries, enabling me to make decisions         | Fail     |
| Visitor             | Receive feedback when using features of the site        | Know whether the actions I have taken on the site have been successful    | Pass      |

In my final design I haven't implemented links to social media, or a contact form, these would be features I would like to include in a future build. Having had many issues with deploying the site and with the deadline for the project looming, I decided to focus on the core components of the e-commerce store to ensure these were functioning correctly. Having done both of these features in previous projects I decided they were of lesser importance than the ones I focussed on completing.

***

#### Testing for Casual Customer

A casual customer is someone who wants to purchase an item from the site as a first purchase and/or a one-off. The site's goal is to convert these types of customers to return/regular customers.

| As a                | I want to                                               | So that I can                                                            | Pass/Fail |
|---------------------|--------------------------------------------------------|---------------------------------------------------------------------------|-----------|
| Casual customer      | View all products available                            | Select products to purchase                                                | Pass      |
| Casual customer      | View product by categories                             | Browse a selection of products which I may be interested in without having to look through all products | Pass      |
| Casual customer      | Search for a product                                  | Quickly purchase a particular product                                      | Pass      |
| Casual customer      | View full details for a single product                 | See an image, description, reviews, and price of a product before purchase | Pass      |
| Casual customer      | Be able to see all products which have offers on them  | Purchase products which have an offer price                               | Pass      |
| Casual customer      | Add items to a shopping bag                           | Purchase a number of items at once                                         | Pass      |
| Casual customer      | View the content of my shopping bag                   | Review and make changes to my selections prior to purchase                | Pass      |
| Casual customer      | Be able to checkout securely without making a user account | Quickly make a purchase from the site                                     | Pass      |
| Casual customer      | View a confirmation of my order after purchase        | Ensure the purchase has been successful and contains the correct items    | Pass      |
| Casual customer      | Receive a confirmation email on the completion of my order | Keep a record of the successful order and the items it contains          | Pass      |
| Casual customer      | Have the option to use my details to create an account during checkout | Become a regular customer if I decide to                                  | Pass      |


***

#### Testing for Regular Customer

A regular customer is someone who uses the site often, having multiple purchases. They have many of the same requirements as a casual customer but want a more in-depth experience. The site goal is to keep these customers engaged and retain their custom.

| As a                | I want to                                               | So that I can                                                            | Pass/Fail |
|---------------------|--------------------------------------------------------|---------------------------------------------------------------------------|-----------|
| Regular customer     | Register for a user account                           | Have a profile to use while browsing and purchasing from the site         | Pass      |
| Regular customer     | Be able to log in and out of my account                | Securely access my account information                                    | Pass      |
| Regular customer     | Receive a confirmation email upon account registration | Verify that my account was created correctly and linked to my email      | Pass      |
| Regular customer     | Recover my password                                   | Regain access to my account if I lose/forget my password                  | Pass      |
| Regular customer     | Save my personal information required when ordering    | Checkout more easily when I am making further purchases                    | Pass      |
| Regular customer     | Update my user profile                                | Keep my personal details up to date                                       | Pass      |
| Regular customer     | See a history of my previous orders                   | Quickly locate and purchase again items I have previously purchased       | Pass      |
| Regular customer     | Be able to review products I have purchased            | Give feedback on products for other users to see                          | Pass      |
| Regular customer     | Be able to delete/edit my reviews                      | Change my review if I made mistakes and/or change my view                 | Pass      |
| Regular customer     | Receive recommendations of products I may be interested in | Purchase products which are recommended for customers who have purchased products which I have | Pass      |
| Regular customer     | Have exclusive offers for being a regular customer    | Feel valued as a regular customer and make savings                         | Fail      |

As discussed above due to the time constraints I failed to implement the offers specific to certain users. I did manage to implement the offers feature in which the site superuser could add/ remove promotions from products and am please with managing to build this. In a future build expanding this feature to be able to target specific customers would be a nice way to improve this feature.
***

#### Testing for Site Admin

The site admin is the user who is using the site to sell their products, they want a simple interface to deal with managing the e-commerce side of their business.

| As a            | I want to                                  | So that I can                                                              | Pass/Fail |
|-----------------|-------------------------------------------|-----------------------------------------------------------------------------|-----------|
| Site admin      | Add a product                             | Update my store with new products as I source them                          | Pass      |
| Site admin      | Edit a product                            | Update details/price for a product if they need changing                    | Pass      |
| Site admin      | Delete a product                          | Remove a product from the store if I no longer want to sell it              | Pass      |
| Site admin      | Add offers to products                    | Promote a product of my choice to customers                                | Pass      |
| Site admin      | See the stock levels for products         | Correctly manage my inventory and order stock as required                   | Fail      |
| Site admin      | Review customer product reviews           | Ensure reviews are appropriate for the site and are not malicious            | Pass      |

Another feature which didn't make the cut for this current build was having a stock inventory and implementing features by which the superuser could manage inventory. As the project grew it became clear that whilst this would be a nice feature to have I needed to first build a functioning store. I am happy with the store I did build with in the project time frame and have a good idea of future features I would like to add.

***

### Bugs <a name="bugs"></a>

#### Bug fixes

Fixed a bug in which sort by ratings included product with no current ratings and put them at the top above products with highest rating.

Fixed a bug in which the products home button on products page would be located incorrectly in instances of product searches with a low amount of results.

Fixed a bug in which styles were not applied to allauth verify email address page.

Fixed a bug in which order history page buttons were overflowing into each other.

Fixed a bug in which empty quotation marks were visible for reviews which contained no text review.

The main issues I faced during this project was during deploying the page and using AWS S3 bucket to store static files, this was due to my experience of learning this process using older versions of many of the technologies used. When it came to producing my own project I decided to use the most recent versions as I thought this would be a valuable learning process for me as a developer. Technologies change rapidly and being up to date and able to update projects to use the most recent version of technologies is a useful skill. I'm glad I chose to do this but it has also lowered the quality of other aspects of my project, features I would have liked to include and better styling of the site, had i had longer to work on it. But overall I'm happy I managed to get a deployed version working, and tested, with the features it has. I plan to implement further features after the deadline and continue to build upon these skills I have learnt. 

***
