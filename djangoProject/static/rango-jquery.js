$(document).ready( function() {
	$('.rating').each(function(){
  		if($(this).text() == "clean")$(this).parent().css('background-color','rgb(255,255,224)');
  		if($(this).text() == "low-risk")$(this).parent().css('background-color','rgb(135,206,250)');
  		if($(this).text() == "medium-risk")$(this).parent().css('background-color','rgb(255,255,0)');
  		if($(this).text() == "high-risk")$(this).parent().css('background-color','orange');
  		if($(this).text() == "malicious")$(this).parent().css('background-color','red');
	});

	$("#filterDate").change(function() {
	    var filterValue = $(this).val();

	    var row = $("[class='date']"); 
	    row.parent().hide();
	    row.each(function(i, el) {
	    	var date1 = new Date($(el).text());
		    var currentDate = new(Date)
			var timeStampCurrent = Math.round(new Date().getTime() / 1000);
			var timeStampDate1 = Math.round(date1.getTime() / 1000);
			var isWithin;
			if (filterValue === "24-hours"){
				isWithin = (timeStampCurrent - timeStampDate1) < 24 * 3600 && (timeStampCurrent - timeStampDate1) >0;
			}
			if (filterValue === "7-days"){
				isWithin = (timeStampCurrent - timeStampDate1) < 7 * 24 * 3600 && (timeStampCurrent - timeStampDate1) >0;
			}
			if (filterValue === "4-weeks"){
				isWithin = (timeStampCurrent - timeStampDate1) < 7* 4 * 24 * 3600 && (timeStampCurrent - timeStampDate1) >0;
			}
			if (filterValue === "all"){
				isWithin = true
			}
	    	if (isWithin === true) {
	    		$(el).parent().show();
	    	}
	    })
    });

    $('td:nth-child(1),th:nth-child(1)').hide();
});