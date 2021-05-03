$(".headTop").click(function (e) {
    console.log("upper");
    scrollTo(0,0)
})
$(function ()  {
    function showArrow() {
        if ( window.pageYOffset > window.screen.availHeight) {
            document.querySelector(".head-to-top").setAttribute("style" , "display:block;")
        }else {
            document.querySelector(".head-to-top").setAttribute("style" , "display:none;")
        }

        window.addEventListener("scroll" , function (e) {
            if ( window.pageYOffset > window.screen.availHeight) {
                document.querySelector(".head-to-top").setAttribute("style" , "display:block;")
            }else {
                document.querySelector(".head-to-top").setAttribute("style" , "display:none;")
            }
        })
    }
    $(".headTop") != null ? showArrow():""

})

$(".headTop").click(function (e) {
    console.log("Hello");
    scrollTo(0,0)
})

function deleteQuestions(target , id) {
    var target = document.querySelector("."+target);
    var csrfT = document.querySelector(".tken").value;
    console.log(csrfT)
    try {
      var xmlhttp = new XMLHttpRequest();
    } catch (e) {
      var xmlhttp = new ActiveXObject();
    } finally {
      xmlhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) {
          target.remove();
        }
      }
      xmlhttp.open("POST"  , "/questions/deleteQuestion/", true );
      xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
      xmlhttp.setRequestHeader("X-CSRFToken" , csrfT);
      xmlhttp.send("Qid="+id);
    }
  }
function popM(cname) {
    var data = document.querySelector("."+cname);
    data.setAttribute("style" , "display:block;");
    // menu.classList.add("grid");
    hamIcon.classList.add("hide");
    closeIcon.classList.add("grid");
    editBtn.classList.remove('hide');
    deleteBtn.classList.remove('hide');
}
function adjustAnswer(target_id , target_element_id){
  var csrfT = document.querySelector(".tken").value;
  var content = document.querySelector("#editor").value;
  var target_element = document.querySelector("."+target_element_id);
  // timestamp
try {
  var xmlhttp = new XMLHttpRequest();
} catch (e) {
  var xmlhttp = new ActiveXObject();
} finally {
  xmlhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status) {
        var response = JSON.parse(this.responseText);
        if (response.Status) {
            target_element.innerHTML = content;
        }else{
          alert(response.Message);
        }
    }
  }
  xmlhttp.open("POST" , "/questions/editQuestion/" , true);
  xmlhttp.setRequestHeader("X-CSRFToken" , csrfT);
  xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
  xmlhttp.send("target_id="+target_id+"&content="+content);
  }
}
function dropdownbtn(target_element_class){

}
