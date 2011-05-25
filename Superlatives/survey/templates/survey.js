
var residents = [
{% for resident in residents %}
 '{{ resident.name }}',
{% endfor %}
];

function submitQuestion(question) {
  if ($.inArray($(question).val(), residents)) {
    // disable input and flash opacity a little
    onTimeout(function() {
      // do submission
    }, 1000);
  } else {
    $(question).val('');
  }
}

function initialize() {
  // code to make autocomplete work should go in here
  $('.inp_resident').autocomplete({
    source: residents,
    autoFocus: true,
    delay: 50
  });
}

$(initialize);

