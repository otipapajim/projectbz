#!C:\Users\Sigma\AppData\Local\Programs\Python\Python39\python.exe

print("content-type: text/html\n\n" )
print("<!DOCTYPE html>")
print("<html lang='en'>")
#Begin Head
print("<head>")
print("<title> Run a Test </title>")
print("<meta charset='UTF-8'>")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("<link rel='stylesheet' href='./css/standard.css'>")
print("<link rel='stylesheet' href='./vendor/font-awesome/css/font-awesome.min.css'>")
print("</head>")
#End Head

print("<body>")
print(" <div class='wrapper'>")
#Top Menu
print("<div class='sidebar'>")
#profile image and text
print("<div class='profile'>")
print("<img src='./src/img/faceimg.jpg' alt='profile_picture'>")
print("<h3>This Guy</h3>")
print("<p>Designer</p>")
print("</div>")
#menu item
print("<div>")
print("<ul>")

print("<li>")
print("<a href='./standard.py' >")
print("<span class='icon'><i class='fa fa-home'></i></span>")
print("<span class='item'>Home</span>")
print("</a>")
print("</li>")

print("<li>")
print("<a class='active' href='./test.py'>")
print("<span class='icon'><i class='fa fa-flask'></i></span>")
print("<span class='item'>Run a Test</span>")
print("</a>")
print("</li>")

print("<li>")
print("<a href='results.py'>")
print("<span class='icon'><i class='fa fa-folder-open'></i></span>")
print("<span class='item'>Test Results</span>")
print("</a>")
print("</li>")

print("<li>")
print("<a href='reports.py'>")
print("<span class='icon'><i class='fa fa-line-chart'></i></span>")
print("<span class='item'>Reports</span>")
print("</a>")
print("</li>")

print("<li>")
print("<a href='admin.py'>")
print("<span class='icon'><i class='fa fa-shield'></i></span>")
print("<span class='item'>Administration</span>")
print("</a>")
print("</li>")

print("<li>")
print("<a href='settings.py'>")
print("<span class='icon'><i class='fa fa-cog'></i></span>")
print("<span class='item'>Settings</span>")
print("</a>")
print("</li>")

print("<li>")
print("<a href='index.py'>")
print("<span class='icon'><i class='fa fa-sign-out'></i></span>")
print("<span class='item'>Logout</span>")
print("</a>")
print("</li>")

print("</ul>")
print("</div>")
print("</div>")
print("</div>")
print("</div>")

print("<div>")
print("<p class='notecolor'> Enter Item SKU </p>")
print("<div class='search-container'>")
print("<form method = 'POST' id = 'searchform'>")
print("<input type='text' id='search' minlength='19' maxlength='19' placeholder='Ex...PO667MP0DFGILNAFAMZ' class='search-input'>")
print("<a href='#' class='search-btn'>")
print("<i class='fa fa-search'></i>")
print("</a>")
print("</div>")
print("<br>")
print("<br>")
print("<input type='submit' class = 'button' name='searchBtn' id='searchBtn' value='Search' />")
print("</form")
print("<br>")
print("<br>")
print("</div>")


#scraper



print("<script src='./vendor/jquery/jquery.min.js'></script>")
print("<script src='./js/initscraper.js'></script>")
print("</body>")
#End Body
print("<html>")