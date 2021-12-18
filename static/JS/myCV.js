function checkIfGood(){
    let phoneOK = document.getElementById("Telephon").checkValidity()
    let phMsg = ""
    if (phoneOK){
        phMsg = "Thank you";
    }
    else{
        phMsg = "Pattern should be 05XXXXXXX";
    }
    document.getElementById("phoneV").innerHTML = phMsg;

    let emailOK = document.getElementById("EmailIn").checkValidity()
    let emailMsg = ""
    if (emailOK){
        emailMsg = "Thank you";
    }
    else{
        emailMsg = "Pattern should be XXX@XXXX.com"
    }
    document.getElementById("emailVM").innerHTML = emailMsg;

    if (emailOK && phoneOK){
        alert("Information OK!")
    }
}

