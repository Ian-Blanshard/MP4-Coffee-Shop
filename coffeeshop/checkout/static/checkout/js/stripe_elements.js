/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
*/
// get key/secret from the html elements and create variables
console.log('js loaded')
var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim().slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').textContent.trim().slice(1, -1);
// initialise stripe passing the key
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
// set styles for input element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// create card input
var card = elements.create('card', {style: style});
// mount element to div with id
card.mount('#card-element');
// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});
// get payment form element as a variable
var form = document.getElementById('payment-form');
// add event listener for submit and function when its pressed
form.addEventListener('submit', function(ev) {
    // prevent from submitting as normal
    ev.preventDefault();
    // Disable card and submit button during payment processing
    card.update({ 'disabled': true });
    document.getElementById('submit-button').disabled = true;
    // Confirm the payment with Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            // card details entered by user
            card: card,
        }
    }).then(function(result) {
        // get div for displaying error as variable
        var errorDiv = document.getElementById('card-errors');
        // if there is an error log to console
        if (result.error) {
            console.error('Payment failed:', result.error.message);
            // Show error message if payment fails
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `;
            errorDiv.innerHTML = html;
            // Re-enable card and submit button
            card.update({ 'disabled': false });
            document.getElementById('submit-button').disabled = false;
        } else {
            // if payment succesful
            if (result.paymentIntent.status === 'succeeded') {
                // Submit the form if payment is successful
                console.log('form submitted')
                form.submit();
            }
        }
    });
});