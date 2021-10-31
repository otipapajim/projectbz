#!C:\Users\Sigma\AppData\Local\Programs\Python\Python39\python.exe
print("content-type: text/html\n\n" )
print("<!DOCTYPE html>")
print("<html lang='en'>")
#Begin Head
print("<head>")
print("<title> Log in Page </title>")
print("<meta charset='UTF-8'>")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("<link rel='stylesheet' href='./css/login.css'>")
print("<link rel='stylesheet' href='./vendor/font-awesome/css/font-awesome.min.css'>")
print("</head>")
#End Head

#Begin Body
print("<body>")

#Form Container
print("<div class='container' id='container'>")
print("<div class='form-container log-in-container'>")
print("<form id = 'loginform' method = 'POST'")
print("<h1>Login</h1>")				
print("<div class='social-container'>")				
print("<a href='#' class='social'><i class='fa fa-facebook fa-2x'></i></a>")					
print("<a href='#' class='social'><i class='fab fa fa-twitter fa-2x'></i></a>")					
print("</div>")
print("<span>or use your account</span>")				
print("<input type='email' id='email' placeholder='Enter Your Email' required/>")				
print("<input type='password' id='pwd' placeholder='Password' required />")				
print("<a href='#'>Forgot your password?</a>")				
#print("<button>Log In</button>")
print("<input type='submit' class = 'button' name='loginBtn' id='loginBtn' value='Login' />")				
print("</form>")			
print("</div>")

#Side Container
print("<div class='overlay-container'>")	
print("<div class='overlay'>")
print("<div class='overlay-panel overlay-right'>")				
print("<h1>Welcome Back!!</h1>")
print("	<p>We hope you enjoy using our website!.</p>")					
print("</div>")
print("</div>")
print("</div>")
print("</div>")
print("<script src='./vendor/jquery/jquery.min.js'></script>")
print("<script src='./js/login.js'></script>")
print("</body>")
#End Body
print("<html>")