$(document).ready(function() {
    var string1 = $('#string1');
    var temp = $('#temp');
	var display = $(".caltop");
    var finalstring = ""


    var clearData = function() {
        string1.val('');
        temp.val('')
    };


	 $('.eq').click(function() {

        $.post('/operation', {
            string1: JSON.stringify(finalstring)
        }, function(data) {
            display.html(data.result);
            clearData();
            temp.val(data.result);
        });
    });


    var clearOutput = function() {
        display.html('');
        finalstring = ""
    };

    $('.num').click(function() {

		if(string1.val()!=''){
			display.html('');
            finalstring = ""
		}

        if (display.html() == '0') {
            clearOutput()
            finalstring = ""
        }

        if (string1.val() !== '') {
            clearOutput()
            clearData();
            finalstring = ""
        }

        display.append($(this).val());
        // display.html(string1.val);
        finalstring += $(this).val()

    });

    $('.clear').click(function() {
        display.html('0');
        clearData();
    });

});