
var residents = [
{% for resident in residents %}
 '{{ resident.name }}',
{% endfor %}
];

function submitQuestion(question) {
  if $(question).val() in residents {
    // disable input and flash opacity a little
    onTimeout(function() {
      // do submission
    }, 1000);
  }
}

function initialize() {
  // code to make autocomplete work should go in here
}

$(initialize);

