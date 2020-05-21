const full = document.getElementById('full');
console.log(full);
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

          //animating the like btn
          const emptyLikeBtn = document.querySelectorAll('#emptyLove');
          const Liked = document.querySelectorAll('#Love');
          console.log(emptyLikeBtn.length);
          console.log(Liked);
          let length = emptyLikeBtn.length - 1;


          function likeAct(array1,array2,i){
          array1[i].addEventListener('click',function(){
                  array1[i].style.display = 'none';
                  array2[i].style.display = "block";
          });
          array2[i].addEventListener('click',function(){
              array2[i].style.display = 'none';
              array1[i].style.display = 'block';
          });
          }

          for(x=0;x<=length;x++){
          likeAct(emptyLikeBtn,Liked,x);
          }
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


  // element creator


  // end of element creator

  function checkmesages() {
    try {
      var xmlobj = new XMLHttpRequest();
    } catch (e) {
      var xmlobj = new ActiveXObject();
    } finally {
      var msgcount = 0;
    }
  }
