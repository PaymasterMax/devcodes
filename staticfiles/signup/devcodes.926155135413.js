const mismatch = document.getElementById('mismatch');
const shortPass = document.getElementById('shortPass');

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

function spinnermanager()
{

	if(document.getElementById("uname").value != "" && document.getElementById("phone").value != "" &&
	 document.getElementById("ema").value != "" &&
	document.getElementById("pass1").value != "" &&  document.getElementById("pass2").value != "" &&
	 document.getElementById("pass2").value !="" && document.getElementById("profile").value != "")
	{

		document.getElementById("spin").setAttribute
		("class" , "fa fa-spinner fa-spin fa-1x");
	}
}


function form_manager()
{
	var flag = false;
	var favlang = document.getElementById("favlang");
	if(document.getElementById("uname").value == "")
	{

		alert("Username blank");
		favlang.setAttribute("style" , "display:none;");
	}

	else if(document.getElementById("phone").value == "")
	{

		alert("phone blank");
		favlang.setAttribute("style" , "display:none;");
	}
	else if(document.getElementById("ema").value == "")
	{

		alert("email blank");
		favlang.setAttribute("style" , "display:none;");
	}
	else if(document.getElementById("pass1").value == "" || document.getElementById("pass2").value == "")
	{

		alert("pass1 blank");
		favlang.setAttribute("style" , "display:none;");
	}

else if(document.getElementById("hobby").value == "")
	{
		favlang.setAttribute("style" , "display:block;");
	}
	else if(document.getElementById("profile").value == "")
	{

		alert("profile blank");
		favlang.setAttribute("style" , "display:none;");
	}
	else {
		favlang.setAttribute("style" , "display:none;");
	}
	spinnermanager();
}
	function passwordmaster(){
		var pass1 = document.getElementById("pass1").value;
		var pass2 = document.getElementById("pass2").value;
		var emp = document.getElementById("shortPass")
		var mis = document.getElementById("mismatch")
		if(pass1 != "" && pass2 != "")
			{
				if(pass1 == "" || pass2 == ""){
						document.getElementById("pass1").innerHTML = "";
						document.getElementById("pass2").innerHTML = "";
						emp.setAttribute("style" , "display:block;margin:0px auto")
						emp.innerHTML = "password cannot be empty";
						mis.setAttribute("style" , "display:none;");
					}
				else if(pass1 != pass2)
					{
						document.getElementById("pass1").innerHTML = "";
						document.getElementById("pass2").innerHTML = "";
						mis.setAttribute("style" , "display:block;margin:0px auto")
						mis.innerHTML = "Password mismatch";
						emp.setAttribute("style" , "display:none;");
					}

				else if(pass1.length < 10)
						{
							document.getElementById("pass2").innerHTML = "";
							document.getElementById("pass1").innerHTML = "";
							emp.setAttribute("style" , "display:block;margin:0px auto")
							mis.setAttribute("style" , "display:none;");
							emp.innerHTML = "Short password";
						}
						else{
							emp.setAttribute("style" , "display:none;");
							mis.setAttribute("style" , "display:none;");
						}
	}
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
