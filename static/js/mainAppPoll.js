var choice;
var showCorrect = false;
$(window).load(function(){
  $('#submitAnswerBtn').hide();
  $('#quiz-confirmation').hide();
});

var resetPoll = function(){
  $('#quiz').show();
  $('#submitAnswerBtn').hide();
  $('#quiz-confirmation').hide();
}
$(function(){
    var loading = $('#loadbar').hide();
    $(document)
    .ajaxStart(function () {
        loading.show();
    }).ajaxStop(function () {
    	loading.hide();
    });

    $("label.btn").on('click',function () {
    	choice = $(this).find('input:radio').val();
      $('#submitAnswerBtn').fadeIn();
    });

    $("#submitAnswerBtn").on('click',function () {
      $('#loadbar').show();
      $('#submitAnswerBtn').hide();
      $('#quiz').fadeOut();
      setTimeout(function(){
            if (showCorrect){$( "#answer" ).html(  $(this).checking(choice) );}
            $('#quiz-confirmation').fadeIn();
            $('#loadbar').fadeOut();
           /* something else */
      }, 1500);
    });

    $ans = 3;

    $.fn.checking = function(ck) {
        if (ck != $ans)
            return 'INCORRECT';
        else
            return 'CORRECT';
    };
});
