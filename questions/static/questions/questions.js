//   added things

// getting the constants
const bdy = document.querySelector("body");
const hamIcon = document.querySelector(".menu-icon");
const hamHolder = document.querySelector(".menu-holder");
const closeIcon = document.querySelector("#close");

const menu = document.querySelector(".menu-lists");
const editBtn = document.querySelector(".edit-Btn");
const editPop = document.querySelector(".edit-pop");

const deleteBtn = document.querySelector(".delete-Btn");
const deletePop = document.querySelector(".confirmation");

const cancel = document.querySelectorAll(".cancel-Btn");
const editCancel = document.querySelector("#editCancel");
const delCancel = document.querySelector("#delCancel");


editCancel.addEventListener('click',function(){
    editPop.classList.remove('grid');
    closeIcon.classList.remove("grid");
    hamIcon.classList.remove("hide");
});

delCancel.addEventListener('click',function(){
    deletePop.classList.remove('grid');
    closeIcon.classList.remove("grid");
    hamIcon.classList.remove("hide");
});
function openMenu(cname) {
  var data = document.querySelector("."+cname);
  data.setAttribute("style" , "display:block;");
  // menu.classList.add("grid");
  hamIcon.classList.add("hide");
  closeIcon.classList.add("grid");
  editBtn.classList.remove('hide');
  deleteBtn.classList.remove('hide');
}
      // PAMINUS :)
// hamIcon.addEventListener('click',function(){
//     menu.classList.add("grid");
//     hamIcon.classList.add("hide");
//     closeIcon.classList.add("grid");
//     editBtn.classList.remove('hide');
//     deleteBtn.classList.remove('hide');
// });
closeIcon.addEventListener('click',function(){
    menu.classList.remove("grid");
    hamIcon.classList.remove("hide");
    closeIcon.classList.remove("grid");
    // editBtn.classList.add('hide');
    // deleteBtn.classList.add('hide');
    });

// PAMINUS code commented
// editBtn.addEventListener('click',function(){
//   editPop.classList.add('grid');
//   editBtn.classList.add('hide');
//   deleteBtn.classList.add('hide');
// });

function openeditpop(target){
  editPop.classList.add('grid');
  document.querySelector("#editor").value = document.querySelector("."+target).innerHTML;
  editBtn.classList.add('hide');
  deleteBtn.classList.add('hide');
}
deleteBtn.addEventListener('click',function(){
   deletePop.classList.add('grid');
   deleteBtn.classList.add('hide');
  editBtn.classList.add('hide');

});
// end of addition

  var up=document.getElementById('up');
  window.onscroll=function(){
  var scrollPos=window.pageYOffset;
  if(scrollPos<100){
      up.classList.add('hide');
  }
  else{
      up.classList.remove('hide');
  }
  }
  const openModalButtons = document.querySelectorAll('[data-modal-target]')
  const closeModalButtons = document.querySelectorAll('[data-close-button]')
  const overlay = document.getElementById('overlay')

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
    modal.classList.remove('active')
    overlay.classList.remove('active')
    }
  }
