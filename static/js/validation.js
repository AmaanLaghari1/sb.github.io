function removeErrors(){

    errors = document.getElementsByClassName('error');
    for(let item of errors)
    {
        item.innerHTML = "";
    }
}
function showError(id, error){
    element = document.getElementById(id);
    element.getElementsByClassName('error')[0].innerHTML = error;

}

function userLogin(){
    var returnval = true;
    removeErrors();

    var email = document.forms['signupForm']["email"].value;
    if (email.length>30){
        showError("email", "Email length exceeded!");
        returnval = false;
    }
    if (email.length == 0){
        showError("email", "Invalid email!");
        returnval = false;
    }

    var password = document.forms['login']["pwd"].value;
    if (password.length < 8){

        showError("pwd", "Atleast 8 characters!");
        returnval = false;
    }
    var cpassword = document.forms['login']["cpwd"].value;
    if (password != cpassword){

        showError("cpwd", "Passwords didn't match!");
        returnval = false;
    }

    return returnval;
}