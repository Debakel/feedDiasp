<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>feedDiasp*</title>
<link rel="stylesheet" href="static/bootstrap.min.css" />
<link rel="stylesheet" href="static/bootstrap-theme.min.css" />
<link rel="stylesheet" href="static/jquery-ui.css" />
<link rel="stylesheet" href="static/style.css" />

<script src="static/jquery-1.9.1.js"></script>
<script src="static/jquery.min.js"></script>

<script src="static//bootstrap.min.js"></script>
<script src="static/jquery-ui.js"></script>

	<script>
	function PostData() {
	$('#result').addClass('hide');
    // 1. Create XHR instance - Start
    var xhr;
    if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest();
    }
    else if (window.ActiveXObject) {
        xhr = new ActiveXObject("Msxml2.XMLHTTP");
    }
    else {
        throw new Error("Ajax is not supported by this browser");
    }
        
    // 2. Define what to do when XHR feed you the response from the server - Start
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status == 200 && xhr.status < 300) {
				var obj = JSON.parse(xhr.responseText);
				$("#result").show()
                document.getElementById('result').innerHTML = obj.message;
                if(obj.success){
					$("#result").removeClass('label-warning');
					$("#result").addClass('label-sucess');
				}
				else{
					$("#result").removeClass('label-sucess');
					$("#result").addClass('label-warning');		
				}		
                $("#result").removeClass('hide');
            }
        }
    }
    xhr.open('POST', 'add');
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send(get_postdata());
}
	function get_postdata()
	{
		var form = document.forms['form'];
		var pod = form.pod.value;
		var username = form.username.value;
		var password = form.password.value;
		var feed_url = form.feed_url.value;
		
		return 'pod='+escape(pod)+'&username='+escape(username)+'&password='+escape(password)+'&feed_url='+escape(feed_url);
	}

	</script>
  </head>

  <body>
   <div class="container">
		<form class="form-signin" name="form">
			<h1>feedDiasp*</h1>
			<div class="input-group">
				<input type="text" class="form-control" name="username" id="username" placeholder="Nutzername">
				<div class="input-group-addon">@</div>
				<input type="text" class="form-control" name="pod" id="pod" placeholder="Pod" >			
			</div>
			<input type="password" id="password" name="password" class="form-control" placeholder="Password"  autofocus>
			<input type="text" id="feed_url" name="feed_url" class="form-control" placeholder="https://example.org/feed.rss" >
			

		</form>
		<div class="form-signin">
			<button class="btn btn-lg btn-primary btn-block" onclick="PostData()">Eintragen</button>
			<div class="hide label" role="label" id="result"></div>
		</div>
		
	</div>
  </body>
</html>
