/*!
=========================================================
* Meyawo Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

document.addEventListener("DOMContentLoaded", function() {
    var isHomePage = window.location.pathname === '/'; // Adjust this if your homepage URL is different
    if (!isHomePage) {
        var navbar = document.getElementById('custom-navbar');
        navbar.style.backgroundColor = '#240046'
    } 
})


// navbar toggle
$('#nav-toggle').click(function(){
    $(this).toggleClass('is-active')
    $('ul.nav').toggleClass('show');
});

