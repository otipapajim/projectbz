$(document).ready(function() {
    $('#loginform').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: './scripts/login.php',
            data: {                            
                myemail: $("#email").val(),
                mypassword: $("#pwd").val()
            },
            success: function(response)
            {
                var jsonData = JSON.parse(response);
 
                // user is logged in successfully in the back-end
                // let's redirect
                if (jsonData.success == "1")
                {
                    location.href = './standard.py';
                }
                else
                {
                   alert('Invalid Credentials!');
                }
           }
       });
     });
});