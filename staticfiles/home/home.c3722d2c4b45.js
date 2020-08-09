document.querySelector(".buy-me-coffee").addEventListener("click" , function(e){
    var target = document.querySelector(".coffee-options")
    if (target.getComputedStyle().display=="none") {
        target.setAttribute("style" , "display:flex;");
        alert("Hello world")
    }
})
