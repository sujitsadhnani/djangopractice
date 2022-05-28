var submit_button = document.getElementById("submit_button");
submit_button.style.display = "none";

var password = document.getElementById("password");
var confirm_password = document.getElementById("confirm_password");

function comparing_passwords(){
    console.log('hello');
    if (password.value == confirm_password.value){
        submit_button.style.display = "block";
    }
    else{
        submit_button.style.display = "none";
    }
};