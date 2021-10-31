$(document).ready(function() {
    $('#searchform').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: './scripts/wrtdata.php',
            data: {                            
                sku: $("#search").val(),
            },
       });
       $.ajax({
        url: './scripts/scraper.py',
   });
     });
});