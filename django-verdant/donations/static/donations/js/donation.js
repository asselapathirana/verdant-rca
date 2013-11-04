$.fn.serializeObject = function(){
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};


function stripeResponseHandler(status, response) {
  var $form = $('#payment-form');

  if (response.error) {
    // Show the errors on the form
    $form.find('.payment-errors').text(response.error.message);
    $form.find('button').prop('disabled', false);
  } else {
    // token contains id, last4, and card type
    var token = response.id;
    // Set the token so it gets submitted to the server
    $form.find('[name="stripe_token"]').val(token);

    // let's not submit credit card details to our server because we don't need them
    $form.find('[data-stripe="number"], [data-stripe="cvc"], [data-stripe="exp-month"], [data-stripe="exp-year"]').val("");

    // and re-submit without javascript
    // TODO: currently this doesn't trigger the jquery submit event but it might in the future
    $form.get(0).submit();
  }
}

jQuery(function($) {
  $('[data-stripe="number"]').payment('formatCardNumber');
  $('[data-stripe="cvc"]').payment('formatCardCVC');
  $('[name="amount"]').keypress(function(eve) {
    if ((eve.which != 46 || $(this).val().indexOf('.') != -1) && (eve.which < 48 || eve.which > 57)  ) {
        eve.preventDefault();
    }
  }).keyup(function(eve) {
    // this part is when left part of number is deleted and leaves a . in the leftmost position.
    // For example, 33.25, then 33 is deleted
    if($(this).val().indexOf('.') == 0) {
        $(this).val($(this).val().substring(1));
    }
  });


  $('#payment-form').submit(function(e) {
    var $form = $(this);

    var error = false;

    var ccNum = $('[data-stripe="number"]').val(),
        cvcNum = $('[data-stripe="cvc"]').val(),
        expMonth = $('[data-stripe="exp-month"]').val(),
        expYear = $('[data-stripe="exp-year"]').val();

    if (!Stripe.validateCardNumber(ccNum)) {
        error = true;
        $form.find('.payment-errors').text('The credit card number appears to be invalid.');
    }
    if (!Stripe.validateCVC(cvcNum)) {
        error = true;
        $form.find('.payment-errors').text('The CVC number appears to be invalid.');
    }
    if (!Stripe.validateExpiry(expMonth, expYear)) {
        error = true;
        $form.find('.payment-errors').text('The expiration date appears to be invalid.');
    }
    if(error){
        return false;
    }



    // Disable the submit button to prevent repeated clicks
    $form.find('button').prop('disabled', true);
    var name = "";
    var title = $form.find("[name=title]").val();
    var first_name = $form.find("[name=first_name]").val();
    var last_name = $form.find("[name=last_name]").val();
    if(title){
        name += title + " ";
    }
    if(first_name){
        name += first_name+ " ";
    }
    if(last_name){
        name += last_name;
    }
    // we have to serialise the form and make sure the correct attributes are set
    var formData = $form.serializeObject();
    var params = $.extend(formData, {
        exp_month: $form.find('[data-stripe="exp-month"]').val(),
        exp_year: $form.find('[data-stripe="exp-year"]').val(),
        name: name
    });

    Stripe.createToken(params, stripeResponseHandler);
    // Stripe.createToken($form[0], stripeResponseHandler);

    // Prevent the form from submitting with the default action
    return false;
  });
});