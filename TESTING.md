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

My html showed a variety of errors during validation.

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


My JavaScript passed valiation, it had one undefined variable but this was Stripe which would be made available from the stripe cdn, which was contained in a html script, which isn't loaded because i was just copying the js code.

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

In my final design I havn't implemented links to social media, or a contact form, these would be features I would like to include in a future build. Having had many issues with deploying the site and with the deadline for the project looming, I decided to focus on the core components of the e-commerce store to ensure these were functioning correctly. Having done both of these features in previous projects I decided they were of lesser importance than the ones I focussed on completing.

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

As discussed above due to the time constraints I failed to implement the offers specific to certain users. I did manage to implement the offers feature in which the site superuser could add/ remove promotions from products and am please with managing to build this. In a future build expanding this feature to be able to target specific customers would be a nice way to imporve this feature.
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


***
