
var residents = [
{% for resident in residents %}
 '{{ resident.name }}',
{% endfor %}
];

function checkIfResident(question) {
  if ($.inArray($(question).val(), residents) == -1) {
    $(question).val('');
  }
  return true;
}

function ajaxQSubmit(form) {
  var question = $(form).find('[type="text"]:first')[0];
  checkIfResident(question);
  if( $(question).val() ) {
    // disable input and flash opacity a little
    $(question).attr("disabled", "disabled");
    $(form).find(':submit:first').attr("disabled", "disabled");
    $(form).effect('highlight', {}, "slow");

    // AJAX submit question
    var ansdata = {
      'qid': $(form).find(':hidden:first').val(),
      'resident': $(question).val()
    };
    $.ajax('/survey/', {
      type: 'POST',
      data: ansdata,
      dataType: 'json',
      success: function(data, textStatus, jqXHR) {
        setTimeout(function() {
          $(form).fadeOut(1000);
        }, 1500);
      }
    });
  }
  return false;
}

// Suppress enter submissions
function rerouteEnter(e) {
  if ( e.which == 13 ) {
    $(e.target).closest('form').next().find('.inp_resident').focus();
    ajaxQSubmit($(e.target).closest('form')[0]);
    return false;
  }
  return true;
}

function initialize() {
  $('.inp_resident').blur(function(e) { checkIfResident(e.target) });
  $('.question_form').submit(function(e) { ajaxQSubmit(e.target) });
  $('.inp_resident').keypress(rerouteEnter);

  // code to make autocomplete work
  $('.inp_resident').autocomplete({
    source: residents,
    autoFocus: true,
    delay: 50
  });
}

$(initialize);

