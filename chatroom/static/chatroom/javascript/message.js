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
// var wsS = "ws://";
// var loc = window.location;
// if (loc.protocol == "https:") {
//   wsS = "wss://"
// }
// var endpoint = wsS + loc.host //+ loc.pathname;
// var webS = new WebSocket(endpoint);
//
// webS.onopen = function(e){
//   console.log("Open", e);
// }
//
// webS.onclose = function(e){
//   console.log("Disconnecting ", e);
// }
//
// webS.onerror = function(e){
//   console.log("Error ", e);
// }
//
// webS.onmessage = function(e){
//   console.log("Message ", e);
// }
