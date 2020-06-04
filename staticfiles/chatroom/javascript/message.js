// home icon
const full = document.getElementById('full');
    const ex = document.getElementById('ex');
    const iLinks = document.getElementById('iLinks');
    full.addEventListener('click',function(){
        // full.classList.add('removeIcon');
        full.style.display = 'none';
        // ex.classList.add('showIcon');
        ex.style.display = 'flex';
        iLinks.style.display = 'flex';
    });
    ex.addEventListener('click',function(){
        // full.classList.remove('removeIcon');
        full.style.display = 'flex';
        // ex.classList.remove('showIcon');
        ex.style.display = 'none';
        iLinks.style.display = 'none';
    });
    // end of home icon
    // 
    // function updatermonster() {
    //   try {
    //     var xmlobj_messanger = new XMLHttpRequest();
    //   } catch (e) {
    //     var xmlobj_messanger = new ActiveXObject();
    //   } finally {
    //     xmlobj_messanger.onreadystatechange = function() {
    //       if (this.readyState == 4 && this.status==200) {
    //         var data = JSON.parse(this.responseText);
    //         for (var i = 0; i < data.all_messages.length; i++) {
    //           alert(data[i]);
    //         }
    //       }
    //     }
    //     xmlobj_messanger.open("POST" , "{% url 'chatroom:updatemessage' %}" , true);
    //     xmlobj_messanger.setRequestHeader("X-CSRFToken" , "{{csrf_token}}");
    //     xmlobj_messanger.setRequestHeader("Content-Type" , "application/x-www-form-urlencoded");
    //     xmlobj_messanger.send();
    //   }
    // }
    //
    // // Check message
    // setInterval(function(){
    //   updatermonster();
    // } , 1000);
