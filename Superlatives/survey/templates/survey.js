
var residents = [
{% for resident in residents %}
 '{{ resident.name }}',
{% endfor %}
];

function initialize() {
  // code to make autocomplete work should go in here
}

$(initialize);

