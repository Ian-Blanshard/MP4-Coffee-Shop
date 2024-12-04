/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
*/

function fadeToggle(element, duration = 100) {
  // Check the current display state of the element
  const isHidden = window.getComputedStyle(element).display === "none";

  if (isHidden) {
    // Show the element by setting display and starting opacity at 0
    element.style.display = "block";
    element.style.opacity = 0;

    // Gradually increase the opacity to 1
    let opacity = 0;
    const increment = 10 / duration;
    const fadeIn = setInterval(() => {
      opacity += increment;
      if (opacity >= 1) {
        element.style.opacity = 1;
        clearInterval(fadeIn);
      } else {
        element.style.opacity = opacity;
      }
    }, 10);
  } else {
    // Gradually decrease the opacity to 0
    let opacity = 1;
    const decrement = 10 / duration;
    const fadeOut = setInterval(() => {
      opacity -= decrement;
      if (opacity <= 0) {
        element.style.opacity = 0;
        clearInterval(fadeOut);
        // Hide the element after the fade-out
        element.style.display = "none";
      } else {
        element.style.opacity = opacity;
      }
    }, 10);
  }
}

// get key/secret from the html elements and create variables
console.log("js loaded");
var stripePublicKey = document.getElementById("stripe-public-key").dataset.stripePublicKey;
var clientSecret = document.getElementById("client-secret").dataset.clientSecret;

// initialise stripe passing the key
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
// set styles for input element
var style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
// create card input
var card = elements.create("card", { style: style });
// mount element to div with id
card.mount("#card-element");
// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
    errorDiv.innerHTML = html;
  } else {
    errorDiv.textContent = "";
  }
});

// get payment form element as a variable
var form = document.getElementById("payment-form");
// add event listener for submit and function when its pressed
form.addEventListener("submit", function (ev) {
  // prevent from submitting as normal
  ev.preventDefault();
  // Disable card and submit button during payment processing
  card.update({ disabled: true });
  document.getElementById("submit-button").disabled = true;
  // fade out payment for and in overly
  fadeToggle(document.getElementById("payment-form"), 100);
  fadeToggle(document.getElementById("loading-overlay"), 100);

  
  var saveInfoCheckbox = document.getElementById("id-save-info");

  // Check if the checkbox exists before trying to access its properties
  var saveInfo = saveInfoCheckbox ? saveInfoCheckbox.checked : false;

  var csrfToken = document.querySelector(
    'input[name="csrfmiddlewaretoken"]'
  ).value;
  var postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: saveInfo,
  };
  
  var url = "/checkout/cache_checkout_data/";

  // Make sure the fetch does not trigger a page reload or unnecessary intent creation
  fetch(url, {
    method: "POST",
    body: new URLSearchParams(postData),
  })
    .then(function (response) {
        
      if (response.ok) {
        
        // Confirm the payment with Stripe
        stripe
          .confirmCardPayment(clientSecret, {
            payment_method: {
              // card details entered by user
              card: card,
              billing_details: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                email: form.email.value.trim(),
                address: {
                  line1: form.street_address1.value.trim(),
                  line2: form.street_address2.value.trim(),
                  city: form.town_or_city.value.trim(),
                  country: form.country.value.trim(),
                  state: form.county.value.trim(),
                },
              },
            },
            shipping: {
              name: form.full_name.value.trim(),
              phone: form.phone_number.value.trim(),
              address: {
                line1: form.street_address1.value.trim(),
                line2: form.street_address2.value.trim(),
                city: form.town_or_city.value.trim(),
                country: form.country.value.trim(),
                postal_code: form.postcode.value.trim(),
                state: form.county.value.trim(),
              },
            },
          })
          .then(function (result) {
            // get div for displaying error as variable
            var errorDiv = document.getElementById("card-errors");
            // if there is an error log to console
            if (result.error) {
              errorDiv.innerHTML = `
                        <span class="icon" role="alert">
                            <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>
                    `;
              // fade payment loading overlay and reshow form
              fadeToggle(document.getElementById("payment-form"), 100);
              fadeToggle(document.getElementById("loading-overlay"), 100);
              // Re-enable card and submit button
              card.update({ disabled: false });
              document.getElementById("submit-button").disabled = false;
              // if payment succesful
            } else if (result.paymentIntent.status === "succeeded") {
              // Submit the form if payment is successful
              console.log("form submitted");
              form.submit();
            }
          });
      } else {
        
        var errorDiv = document.getElementById("card-errors");
        errorDiv.innerHTML = `
          <span class="icon" role="alert">
            <i class="fas fa-times"></i>
          </span>
          <span>There was an issue processing your payment. Please try again.</span>
        `;
        fadeToggle(document.getElementById("payment-form"), 100);
        fadeToggle(document.getElementById("loading-overlay"), 100);
        card.update({ disabled: false });
        document.getElementById("submit-button").disabled = false;
      }
    })
    .catch(function (error) {
      console.error("Fetch request failed:", error);
      location.reload(); // In case of failure, reload the page to reset state
    });
});
