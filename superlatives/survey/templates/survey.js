
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
  var textinps = $(form).find('.inp_resident');
  var entered = true;
  textinps.each(function(i, textinp) {
    checkIfResident(textinp);
    entered = entered && $(textinp).val()
  });
  if( entered ) {
    // disable input and flash opacity a little
    textinps.attr("disabled", "disabled");
    $(form).effect('highlight', {}, "slow");

    // AJAX submit question
    var ansdata = {
      'qid': $(form).find('.question_id').val(),
      'resident': $(textinps[0]).val()
    };
    if(textinps.length == 2) {
      ansdata['resident2'] = $(textinps[1]).val();
    }
    $.ajax('survey/', {
      type: 'POST',
      data: ansdata,
      dataType: 'json',
      success: function(data, textStatus, jqXHR) {
        setTimeout(function() {
          $(form).fadeOut('fast');
        }, 500);
      }
    });
  }
  return false;
}

// Suppress enter submissions
function rerouteEnter(e) {
  if ( e.which == 13 ) { // enter key
    var textinps = $(e.target).closest('form').find('.inp_resident');
    var form = $(e.target).closest('form');
    var clean = true;
    textinps.each(function (i, inp) {
      if($(inp).val() == '') {
        $(inp).focus();
        clean = false;
      }
    });
    if(!clean) {
      if(textinps.length == 1) {
        $(form).next().find('.inp_resident').focus()
      }
      return false;
    }
    $(form).next().find('.inp_resident:first').focus()
    ajaxQSubmit(form);
    return false;
  }
  return true;
}

function inputsfilled (question) {
  inps = $(question).find('.inp_resident');
  return inps.toArray().every(function(inp) { return !!inp.value; });
}

function initialize() {
  $('.inp_resident').blur(function(e) { checkIfResident(e.target) });
  $('.question_form').submit(function(e) { ajaxQSubmit(e.target) });
  $('.inp_resident').keypress(rerouteEnter);

  // disable and hide filled in answers
  $('.question_form').each(function(i, question) {
    if ( inputsfilled(question) ) {
      $(question).find('.inp_resident').attr('disabled', true);
      $(question).hide();
    }
  });

  // code to make autocomplete work
  $('.inp_resident').autocomplete({
    source: residents,
    autoFocus: true,
    delay: 50
  });

  $('#showallbutton').click(function() {
    $('.question_form:hidden').fadeIn('fast');
  });
  $('#hideallbutton').click(function() {
    $('.question_form').filter(':visible').each(function(i,form) {
      if( inputsfilled(form) ) { $(form).fadeOut('fast'); }
    });
  });
}

$(initialize);

