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


### Bugs <a name="bugs"></a>

#### Bug fixes


***

### Testing User Stories <a name="testing-user-stories"></a>
