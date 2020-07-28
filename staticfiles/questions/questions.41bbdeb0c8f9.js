function deleteQuestion(target , id) {
    alert("Hello world");
    var target = document.querySelector("."+target);
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
      xmlhttp.setRequestHeader("X-CSRFToken" , "{{csrf_token}}");
      xmlhttp.open("POST"  , "{% url 'questions:deleteQuestion' %}", true );
      xmlhttp.send("Qid="id);
    }
  }
