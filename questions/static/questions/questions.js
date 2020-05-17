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

  const initailLike = document.getElementById('initial');
  const finalLike = document.getElementById('final');
  const holder = document.querySelector('.like');

//   holder.addEventListener('click',function(){
// initailLike.classList.toggle('clicked');
// finalLike.classList.toggle('clicked');
//   });
  holder.addEventListener('click',function(){
if(initailLike.classList.contains('clicked')){
  finalLike.classList.add('showClicked');
  initailLike.classList.remove('clicked');
}
else{
  initailLike.classList.add('clicked');
  finalLike.classList.remove('showClicked');
}
  });
// function fr shwing up icn
  var up=document.getElementById('up');
  window.onscroll=function(){
  var scrollPos=window.pageYOffset;
  if(scrollPos>100){
      up.classList.add('show');
  }
  else{
      up.classList.remove('show');
  }
  }
  const openModalButtons = document.querySelectorAll('[data-modal-target]')
  const closeModalButtons = document.querySelectorAll('[data-close-button]')
  const overlay = document.getElementById('overlay')
  const question = document.getElementById('modal');
  // const modal = document.querySelector(button.dataset.modalTarget)
  let x = document.getElementById('Xbtn');
  openModalButtons.forEach(button =>{
    button.addEventListener('click', () => {
      const modal = document.querySelector(button.dataset.modalTarget)
      openModal(modal)
    })
  })
  overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    modals.forEach(modal =>{
      closeModal(modal)
    })
  })
  closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
      const modal = button.closest('.modal')
      closeModal(modal)
    })
  })
  function openModal(modal){
    if(modal == null) {return}
    else{
    modal.classList.add('active')
    overlay.classList.add('active')
    }
  }
  function closeModal(modal){
    if(modal == null) {return}
    else{
    question.classList.remove('active')
    overlay.classList.remove('active')
    }
  }
x.addEventListener("click",function(){
  modal.classList.remove('active');
  overlay.classList.remove('active');
  }
);
  function updatemonster(qid) {
    var quid = "question"+qid
    document.getElementById(quid).disabled = true;
    try {
        var xmlhttp = new XMLHttpRequest();
    } catch (e) {
      var xmlhttp = new ActiveXObject();
    }
    finally {
      xmlhttp.open("POST" , "{% url 'questions:updatelikes' %}" , true);
      xmlhttp.setRequestHeader("Content-Type" , "application/x-www-form-urlencoded");
      xmlhttp.setRequestHeader("X-CSRFToken" , "{{csrf_token}}");
      xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
          var data = JSON.parse(this.responseText)
          if (data.is_logged) {
            // $("#"+qid).text(data.counter)
            $(".mytoast").css("display" , "block");
            $(".mytoast").css("background-color" , "red");
            $(".mytoast").css("z-index" , "5");
            document.getElementById("question"+qid).innerHTML = data.counter;
            alert(data.liked);
          } else {
            $(location).attr("href" , "{% url 'login:login' %}")
          }
        }
      }
      xmlhttp.send("qid=" + qid);
    }
  }

// element creator


// end of element creator

//
// function newmessmonster() {
//   alert("Main alert");
//   try {
//     var xmlobj_messanger = new XMLHttpRequest();
//   } catch (e) {
//     var xmlobj_messanger = new ActiveXObject();
//   } finally {
//     xmlobj_messanger.onreadystatechange = function() {
//       alert("Hello out eve");
//       if (this.readyState == 4 && this.status==200) {
//         alert("Hello in the if");
//         var data = JSON.parse(this.responseText);
//         for (var i = 0; i < data.new_questions.length; i++) {
//           elementCreator(data[i]);
//         }
//       }
//     }
//     xmlobj_messanger.open("POST" , "{% url 'questions:updaterquestions' %}" , true);
//     xmlobj_messanger.setRequestHeader("X-CSRFToken" , "{{csrf_token}}");
//     xmlobj_messanger.setRequestHeader("Content-Type" , "application/x-www-form-urlencoded");
//     xmlobj_messanger.send();
//   }
// };
//
// // Check message
// setInterval(function(){
//   updatermonster();
// } , 1000);

function checkmesages() {
  try {
    var xmlobj = new XMLHttpRequest();
  } catch (e) {
    var xmlobj = new ActiveXObject();
  } finally {
    var msgcount = 0;
  }
}
