document.querySelector(".buy-me-coffee").addEventListener("click" , function(e){
    var target = document.querySelector(".coffee-options")
    if (getComputedStyle(target).display=="none") {
        target.setAttribute("style" , "display:flex;");
        alert("Hello world")
    }
});
document.querySelector(".close").addEventListener("click" , function(e){
  alert("Hellow");
})
