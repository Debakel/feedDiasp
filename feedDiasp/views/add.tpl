<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>feedDiasp*</title>
<link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" />
<link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-theme.min.css" />
<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />

<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
	<style>
		body {
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #eee;
}

.form-signin {
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .form-signin-heading,
.form-signin .checkbox {
  margin-bottom: 10px;
}
.form-signin .checkbox {
  font-weight: normal;
}
.form-signin .form-control {
  position: relative;
  height: auto;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: 1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  }
  .form-signin button[type="submit"] {
  margin-top: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

	</style>
	<script>
	function PostData() {
		
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
					$("#result").removeClass('alert-warning');
					$("#result").addClass('alert-sucess');
				}
				else{
					$("#result").removeClass('alert-sucess');
					$("#result").addClass('alert-warning');		
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
			<div class="hide alert alert-info form-signin" role="alert" id="result">Hallo</div>
		</div>
	</div>
  </body>
</html>
