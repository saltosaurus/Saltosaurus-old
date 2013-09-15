jQuery(document).ready ->
	$("a").click (e) ->
		e.preventDefault()
		$( this ).fadeOut()
		comment = $( this ).parent().parent().find(".comment")
		comment.find("input[type=text], textarea").val("")
		comment.slideDown()
		
validateComment = ->
	x = document.forms["newComment"]["comment"].value
	y = document.forms["newComment"]["author"].value
	alert "Validation being called."
	if x is null or x is "" or y is null or y is ""
		alert "You've left at least one field empty."
		false