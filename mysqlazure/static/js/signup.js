var if_doctor = document.getElementById("if_doctor");
var med_details = document.getElementById("med_details");
var submit_button = document.getElementById("submit_button");

med_details.style.display = "none";
submit_button.style.display = "none";


function if_doc_function() {
    if (if_doctor.checked == true) {
        med_details.style.display = "block";

    }
    else {
        med_details.style.display = "none";

    }
};

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

// password.onchange = comparing_passwords();
// confirm_password.onkeyup = comparing_passwords();