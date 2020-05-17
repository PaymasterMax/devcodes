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
  function checkmesages() {
    try {
      var xmlobj = new XMLHttpRequest();
    } catch (e) {
      var xmlobj = new ActiveXObject();
    } finally {
      var msgcount = 0;
    }
  }

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

function elementCreator(questionobj) {
  // main holder for all questions
  var person_holder = document.getElementById("person-holder");
  // one message
  var oneQuestion = document.createElement("div");
  // set the class of the qholder
  oneQuestion.setAttribute("class" , "oneQuestion");
  // oneQuestion.innerHTML = "Hello Once a question"
  person_holder.appendChild(oneQuestion)

  // create the profilepic element
  var profilepic = document.createElement("div");
  // append cloudinary file here
  profilepic.innerHTML = "{% cloudinary questionobj.quid.profilepic.url className=\"myimg\" alt=questionobj.quid.username title=question.quid.username height=200 width=100 %}";
  oneQuestion.appendChild(profilepic);

  var question_container = document.createElement("div");
  // set new objects
  question_container.setAttribute("class","question-container");
  var udetailfrow = document.createElement("div");
  udetailfrow.setAttribute("class" , "user-details-first-row");
  udetailfrow.innerHTML = "{{questionobj.quid.username}}   @{{questionobj.time_posted | timemodifier}}";

  var qcontent = document.createElement("div");
  qcontent.setAttribute("class" , "question-content");
  var qtext = document.createElement("div");
  qtext.setAttribute("class" , "question-text");
  qtext.innerHTML = "Message Content";
  qcontent.appendChild(qtext);
  var qlangtag = document.createElement("div");
  qlangtag.setAttribute("class" , "languages-tagged");
  qlangtag.innerHTML = "{{questionobj.language}}"
  qcontent.appendChild(qlangtag);

  var replysec = document.createElement("div");
  replysec.setAttribute("class","reply-section");

  // children of replysec
  var like = document.createElement("div");
  like.setAttribute("class" , "like");
  var lkbtn = document.createElement("button");
  lkbtn.setAttribute("type","button");
  lkbtn.setAttribute("class","likebtn");
  // lkbtn.setAttribute("width","30px");
  // lkbtn.setAttribute("height","40px");
  lkbtn.setAttribute("style" , "width: 30px; height: 40px;");
  var btnimg = document.createElement("img");
  btnimg.setAttribute("src" , "{% static 'questions/images/coloredLike.svg' %}");
  btnimg.setAttribute("id" , "final");
  btnimg.setAttribute("class" , "final");
  btnimg.setAttribute("alt" , "like button");
  btnimg.setAttribute("style" , "width: 30px; height: 40px;");

  // span element
  var spancount = document.createElement("span");
  spancount.setAttribute("id" , "question{{questionobj.qid}}");
  spancount.innerHTML = "{{questionobj.question_liked.count}}";

  var message = document.createElement("div");
  message.setAttribute("class" , "message");
  var mimg = document.createElement("img");
  mimg.setAttribute("src" , "{% static 'questions/images/message.svg' %}");
  mimg.setAttribute("alt" , "message icon");
  message.innerHTML = "{{questionobj.no_of_answers}}";
  message.appendChild(mimg);

  var Click = document.createElement("div");
  Click.setAttribute("class" , "Click");
  var Clicklink = document.createElement("a");
  Clicklink.setAttribute("href" , "{% url 'questions:answers' questionobj.qid %}");
  Clicklink.innerHTML = " Click to view replies";
  Click.appendChild(Clicklink);

  lkbtn.appendChild(btnimg);
  lkbtn.appendChild(spancount);
  like.appendChild(lkbtn);
  replysec.appendChild(like);
  replysec.appendChild(message);
  replysec.appendChild(Click);
  // end of childred of replysec

  // add childre to parents
  question_container.appendChild(udetailfrow);
  question_container.appendChild(qcontent);
  oneQuestion.appendChild(question_container);
  oneQuestion.appendChild(replysec);
}
// end of element creator

//
// function updatermonster()
$(document).ready(function() {
  alert("Main alert");
  try {
    var xmlobj_messanger = new XMLHttpRequest();
  } catch (e) {
    var xmlobj_messanger = new ActiveXObject();
  } finally {
    xmlobj_messanger.onreadystatechange = function() {
      alert("Hello out eve");
      if (this.readyState == 4 && this.status==200) {
        alert("Hello in the if");
        var data = JSON.parse(this.responseText);
        for (var i = 0; i < data.new_questions.length; i++) {
          elementCreator(data[i]);
        }
      }
    }
    xmlobj_messanger.open("POST" , "{% url 'questions:updaterquestions' %}" , true);
    xmlobj_messanger.setRequestHeader("X-CSRFToken" , "{{csrf_token}}");
    xmlobj_messanger.setRequestHeader("Content-Type" , "application/x-www-form-urlencoded");
    xmlobj_messanger.send();
  }
});

// Check message
setInterval(function(){
  updatermonster();
} , 1000);
