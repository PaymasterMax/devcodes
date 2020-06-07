const mismatch = document.getElementById('mismatch');
const shortPass = document.getElementById('shortPass');
document.getElementById("pass1").addEventListener("keypress" , function(e){
	var password = document.getElementById("pass1").value;
	var target_element = document.querySelector(".pass");
	if (password.length<8) {
		target_element.setAttribute("style" , "color:#f00f00;display:block;");
	}
	else {
		target_element.setAttribute("style" , "color:#f00f00;display:none;");
	}
});

document.getElementById("pass2").addEventListener("focusout" , function(e){
	var password1 = document.getElementById("pass1").value;
	var password2 = document.getElementById("pass2").value;
	var target_element = document.querySelector(".miss");
	if (password1 != password2) {
		target_element.setAttribute("style" , "color:#f00f00;display:block;");
	}
	else {
		target_element.setAttribute("style" , "display:none;");
	}
});


function showMismatch(){
mismatch.classList.add('showAlert');
}
function removeMismatch(){
	mismatch.classList.remove('showAlert');
}
function showShort(){
shortPass.classList.add('showAlert');
}
function removeShort(){
	shortPass.classList.remove('showAlert');
}
 // Listen for when everything has loaded
 window.addEventListener("load", removePage, false);
        const loader = document.getElementById('ld');
        function removePage(){
          loader.classList.add('shrink');
}
function cancel(){
	alert("Hello world");
	document.getElementById("spin").setAttribute("class" , "");
}
function spinnermanager(){
	if(document.getElementById("uname").value != "" && document.getElementById("phone").value != "" &&
	 document.getElementById("ema").value != "" &&
	document.getElementById("showpass").value != "" &&  document.getElementById("mismatch").value != "" &&
	 document.getElementById("mismatch").value !="" && document.getElementById("profile").value != ""){
	document.getElementById("spin").setAttribute("class" , "fa fa-spinner fa-spin fa-1x");
	}
}
function form_manager(){
	var flag = false;
	var favlang = document.getElementById("favlang");
	if(document.getElementById("uname").value == ""){
		alert("Username blank");
		favlang.setAttribute("style" , "display:none;");
	}

	else if(document.getElementById("phone").value == ""){

		alert("phone blank");
		favlang.setAttribute("style" , "display:none;");
	}
	else if(document.getElementById("ema").value == "")
	{

		alert("email blank");
		favlang.setAttribute("style" , "display:none;");
	}
	else if(document.getElementById("showpass").value == "" || document.getElementById("mismatch").value == ""){

		alert("pass1 blank");
		favlang.setAttribute("style" , "display:none;");
	}

else if(document.getElementById("hobby").value == ""){
		favlang.setAttribute("style" , "display:block;");
	}
	else if(document.getElementById("profile").value == ""){

		alert("profile blank");
		favlang.setAttribute("style" , "display:none;");
	}
	else {
		favlang.setAttribute("style" , "display:none;");
	}
	spinnermanager();
}
// Verifcation
function showpass() {
	var elpass = $(".passfield");
	var stats = $("#stats")
	if (elpass.attr("type") === "password") {
		elpass.attr("type" ,"text");
		stats.attr("class" , "fa fa-eye-slash");
	}
	else {
		elpass.attr("type","password");
		stats.attr("class" , "fa fa-eye");
	}
}
