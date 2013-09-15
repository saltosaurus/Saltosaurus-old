jQuery(document).ready ->
	$("a").click (e) ->
		e.preventDefault()
		$( this ).fadeOut()
		comment = $( this ).parent().parent().find(".comment")
		comment.find("input[type=text], textarea").val("")
		comment.slideDown()
		
		comment.find("#newComment").click (e) ->
			e.preventDefault()
			$.ajax {
				type: "POST"
				url: "newComment"
				data: $("form").serialize()
				success: ->
					comment.slideUp()
					numCom = $("#numComm")
					numCom.fadeOut( ->
						numCom.text(parseInt(numCom.text()) + 1)
						)
					numCom.fadeIn()
				}