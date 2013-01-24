<?php ?>

<!DOCTYPE html>
<html lang="en">
<head>
<title>Audiophile</title>
<link rel=stylesheet href=styles.css />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<!--<script src="mousetrap.js"></script>-->
<script>
$(document).ready(function(){
	oldData = $('#content').html();
	window.setInterval(function(){
	   $.get("api.php", function(newData)
	   {
	      if (!(oldData == newData))
	      {
		 oldData = newData;         
		 $('#content').fadeOut('slow', function(){$(this).html(newData).fadeIn('slow')});
	      }
	   });
	}, 3000);
	
	
});
</script>
</head>
<body>
<div id=content>
</div>
</body>
</html>
