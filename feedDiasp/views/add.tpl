<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>feedDiasp*</title>

    <!-- Bootstrap core CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">


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
  </head>

  <body>

    <div class="container">
	
      <form class="form-signin" action="add" method="post">
		<h1>feedDiasp*</h1>
		<div class="input-group">
				<input type="text" class="form-control" name="username" id="username" placeholder="Nutzername">
				<div class="input-group-addon">@</div>
				<input type="text" class="form-control" name="pod" id="pod" placeholder="Pod" >
				
		</div>
		<input type="password" id="password" name="password" class="form-control" placeholder="Password" required autofocus>
        <input type="text" id="feed_url" class="form-control" placeholder="https://example.org/feed.rss" required>
      
        <button class="btn btn-lg btn-primary btn-block" type="submit">Eintragen</button>
       
      </form>

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
